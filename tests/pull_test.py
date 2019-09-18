import unittest


class TestPull(unittest.TestCase):

    def test_upper(self):
        self.assertEqual("foo", "foo")


if __name__ == "__main__":
    unittest.main()
