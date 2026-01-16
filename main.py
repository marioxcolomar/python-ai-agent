import argparse
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from call_function import available_functions, call_function
from prompts import system_prompt

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError("gemini api key is missing")

client = genai.Client(api_key=api_key)


parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]


def call_model(client, model_name, messages):
    return client.models.generate_content(
        model=model_name,
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )


function_results = []


for _ in range(20):
    response = call_model(client, "gemini-2.5-flash", messages)

    if response.usage_metadata is None:
        raise RuntimeError("usage error when calling generate_content")

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    if response.candidates:
        for candidate in response.candidates:
            messages.append(candidate.content)

    # Call functions if they are in the response
    if response.function_calls:
        for function_call in response.function_calls:
            function_call_result = call_function(
                function_call,
            )

            if function_call_result.parts[0].function_response.response is None:
                raise Exception("no response from calling the function")

            function_results.append(function_call_result.parts[0])

            if args.verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")

    else:
        print(response.text)

if function_results:
    messages.append(types.Content(role="user", parts=function_results))
