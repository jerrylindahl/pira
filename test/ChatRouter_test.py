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

    def test_ci_ignore(self):
        result = self.cr.msg_rec("room", "sirjenkins", "Some long message with ABC-123")
        self.assertEqual(self.issue_controller_mock.get_issues.call_count, 0)
        self.assertEqual(result, None)

    def test_42(self):
        qmock = Mock()
        self.cr.quotes = qmock
        result = self.cr.msg_rec("room", "dude", "42")
        qmock.get_random.assert_called_with()

    def test_message_receive(self):
        issues = [Issue("ABC-123", "Such summary", self.config), Issue("ABC-32", "Such summary", self.config)]
        self.issue_controller_mock.get_issues = Mock(return_value=issues)
        self.cr.msg_rec("room", "someone", 'piraBot: ABC-123, ABC-32')
        self.issue_controller_mock.get_issues.assert_called_with(["ABC-123", "ABC-32"])

    def test_get_issues(self):
        result = self.cr.get_issues("piraBot: Check ABC-123 please. Also ABC-42 and AbC-2")
        self.assertListEqual(result, ["ABC-123", "ABC-42", "ABC-2"])