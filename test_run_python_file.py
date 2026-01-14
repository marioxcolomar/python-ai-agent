import unittest

from functions.run_python_file import run_python_file


class TestRunPythonFile(unittest.TestCase):
    def test_run_python_file(self):
        res = run_python_file("calculator", "main.py")
        print(res)

    def test_run_python_file_with_args(self):
        res = run_python_file("calculator", "main.py", ["3 + 5"])
        print(res)

    def test_run_python_file_tests(self):
        res = run_python_file("calculator", "tests.py")
        print(res)

    def test_run_python_file_error_main(self):
        res = run_python_file("calculator", "../main.py")
        print(res)

    def test_run_python_file_non_existent(self):
        res = run_python_file("calculator", "nonexistent.py")
        print(res)

    def test_run_python_file_lorem(self):
        res = run_python_file("calculator", "lorem.txt")
        print(res)


if __name__ == "__main__":
    unittest.main()
