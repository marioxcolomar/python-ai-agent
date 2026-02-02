# Python AI Agent

Current implementation uses examples within this codebase but with little adjustments more locals files and directories can be exposed to the agent. Small improvements to be made when getting an output from the agent to easily follow the steps being taken.

## Motivation

I build this small agentic AI for learning how to work with models and getting into the potential flows for tooling that can help development. The agent has available functions and is able to iterate through results from the first input from the user. The functions help the agent get an overview of the files available that it can read and also write to. Additionally the agent is able to execute python files with optional arguments.

## Quick Start

Setup environment with:
```
uv venv
source .venv/bin/activate
uv add google-genai==1.12.1
uv add python-dotenv==1.1.0
```

## Usage
Once the environment is ready use `uv` to run the `main.py` application:
```
uv run main.py
```

## Contributing

Any ideas for improving the core functionality reach out and we can come up with a plan.
