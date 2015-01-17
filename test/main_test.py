import unittest

from src.main import Main


class ChatTest(unittest.TestCase):
    def setUp(self):
        self.main = Main()

    def test_settings(self):
        config = self.main.get_config('pira.example.cfg')
        self.assertEqual(config.get('Chat', 'type'), "jabber")