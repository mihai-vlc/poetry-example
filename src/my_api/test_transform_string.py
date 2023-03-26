import unittest

from my_api.transform_string import transform


class TestClass(unittest.TestCase):

    def test_name(self):
        self.assertEquals("A", transform("a"))

    @unittest.skip("demonstrating skipping")
    def test2_name(self):
        self.assertEquals("B", transform("b"))
