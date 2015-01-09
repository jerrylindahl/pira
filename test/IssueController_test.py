import unittest
import configparser

from unittest.mock import Mock


from src.IssueController import Issue

class IssueTest(unittest.TestCase):
    def setUp(self):
        self.config = configparser.RawConfigParser()
        self.config.add_section('Chat')
        self.config.set('Jira', 'server', "https://project.server.com/jira")
        

    
    def issue_test(self):
        issue = Issue("ABC-123", "Some summary", self.config)
        self.assertEqual(issue.html, '<p><a href="https://project.server.com/jira/browse/ABC-123">ABC-123</a> Summary: Some summary</p>')