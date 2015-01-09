import unittest
import configparser
from unittest.mock import Mock

from src.ChatRouter import ChatRouter
from src.IssueController import Issue

class ChatRouterTest(unittest.TestCase):
    def setUp(self):
        self.config = configparser.RawConfigParser()
        self.config.add_section('Chat')
        self.config.set('Chat', 'issue-regex', "(ABC-\d+)")
        self.config.add_section('Cache')
        self.config.set('Cache', 'enabled', '0')
        self.config.add_section('Jira')
        self.config.set('Jira', 'server', "")
        
        self.mock = Mock()
        self.cr = ChatRouter(self.mock, self.config)
        
        self.issue_controller_mock = Mock()
        self.cr.IssueController = self.issue_controller_mock

    def test_init(self):
        self.cr.chat.callBack = self.mock

    def test_message_receive(self):
        self.issue_controller_mock.get_issue = Mock(return_value=Issue("ABC-123", "Such summary", self.config))
        self.cr.msg_rec("room", "someone", 'piraBot: ABC-123, ABC-32')
        self.issue_controller_mock.get_issue.assert_called_with("ABC-123")

    def test_get_issues(self):
        result = self.cr.get_issues("piraBot: Check ABC-123 please. Also ABC-42 and AbC-2")
        self.assertListEqual(result, ["ABC-123", "ABC-42", "ABC-2"])

if __name__ == '__main__':
    unittest.main()