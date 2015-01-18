import unittest

from src.Quotes import Quotes


class QuoteTest(unittest.TestCase):
    def setUp(self):
        self.q = Quotes()

    def test_get(self):
        quote = self.q.get_random()
        self.assertTrue(isinstance(quote, str))