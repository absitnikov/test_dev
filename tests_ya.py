import unittest
from ya_func import ya_folder


class TestSomething(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Start of test")

    def test_ya_folder_200(self):
        self.assertEqual("2", str(ya_folder())[0])

    def test_ya_folder_400(self):
        self.assertEqual("4", str(ya_folder())[0])

    @classmethod
    def tearDownClass(cls):
        print("End of the test")


if __name__ == '__main__':
    unittest.main()
