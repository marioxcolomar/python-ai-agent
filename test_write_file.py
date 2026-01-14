import unittest

from functions.write_file import write_file


class TestWriteFile(unittest.TestCase):
    def test_write_file_not_lorem(self):
        res = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        print(res)

    def test_write_file_pkg_lorem(self):
        res = write_file(
            "calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"
        )
        print(res)

    def test_write_file_error(self):
        res = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        print(res)


if __name__ == "__main__":
    unittest.main()
