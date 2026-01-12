import unittest

from functions.get_file_content import get_file_content


class TestGetFileContent(unittest.TestCase):
    def test_get_file_content_main(self):
        main = get_file_content("calculator", "main.py")
        print(f"main.py: {main}")

    def test_get_file_content_pkg_calculator(self):
        pkg_calculator = get_file_content("calculator", "pkg/calculator.py")
        print(f"pkg/calculator.py: {pkg_calculator}")

    def test_get_file_content_bin_cat(self):
        bin = get_file_content("calculator", "/bin/cat")
        print(f"/bin/cat: {bin}")

    def test_get_file_content_file_does_not_exist(self):
        does_not_exist = get_file_content("calculator", "pkg/does_not_exist.py")
        print(f"pkg/does_not_exist.py: {does_not_exist}")


if __name__ == "__main__":
    unittest.main()
