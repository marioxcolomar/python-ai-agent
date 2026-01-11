import unittest

from functions.get_files_info import get_files_info


class TestGetFilesInfo(unittest.TestCase):
    def test_get_current_files(self):
        cur = get_files_info("calculator", ".")
        print(cur)
        self.assertNotIn("Error", cur)

    def test_get_pkg_files(self):
        pkg = get_files_info("calculator", "pkg")
        print(pkg)
        self.assertNotIn("Error", pkg)

    def test_outside_directory(self):
        def base_error(err_path):
            return f"Error: Cannot list '{err_path}' as it is outside the permitted working directory"

        parent = get_files_info("calculator", "../")
        print(parent)
        self.assertEqual(parent, base_error("../"))

        bin = get_files_info("calculator", "/bin")
        print(bin)
        self.assertEqual(bin, base_error("/bin"))


if __name__ == "__main__":
    unittest.main()
