import unittest
import configparser

from unittest.mock import Mock
from unittest.mock import call

from src.IssueController import IssueController
from src.IssueController import Issue


class TestIssueTest(unittest.TestCase):
    def setUp(self):
        self.config = configparser.RawConfigParser()
        self.config.add_section('Jira')
        self.config.set('Jira', 'server', "https://project.server.com/jira")
        self.config.set('Jira', 'user', "user")
        self.config.set('Jira', 'password', "bla")

    def test_get_issue(self):
        ids = ["ABC-123", "ABC-321", "ABC-42"]

        interface_mock = Mock()

        ic = IssueController(self.config)
        ic.jira = interface_mock

        ic.get_issues(ids)
        print(interface_mock.mock_calls)

        calls = [call.issue('ABC-123'), call.issue('ABC-321'), call.issue('ABC-42')]
        interface_mock.issue.assert_has_calls(calls)

    def test_issue(self):
        issue = Issue("ABC-123", "Some summary", self.config)
        self.assertEqual(
            issue.html,
            "<p><a href='https://project.server.com/jira/browse/ABC-123'>ABC-123</a> Summary: Some summary</p>")