import unittest
import configparser
from unittest.mock import Mock

from src.ChatRouter import ChatRouter


class ChatTest(unittest.TestCase):
    def setUp(self):
        config = configparser.RawConfigParser()
        config.add_section('Chat')
        config.set('Chat', 'issue-regex', "(ABC-\d+)")

        self.mock = Mock()
        self.cr = ChatRouter(self.mock, config)

    def test_init(self):
        self.cr.chat.callBack = self.mock

    def test_message_recieve(self):
        pass

    def test_get_issues(self):
        result = self.cr.get_issues("piraBot: Check ABC-123 please. Also ABC-42 and AbC-2")
        self.assertListEqual(result, ["ABC-123", "ABC-42", "ABC-2"])

if __name__ == '__main__':
    unittest.main()