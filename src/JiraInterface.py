from jira.client import JIRA
from jira.exceptions import JIRAError


class JiraInterface:
    def __init__(self, config):
        self.config = config
        self.jira_server = self.config.get('Jira', 'server')
        self.jira_user = self.config.get('Jira', 'user')
        self.jira_password = self.config.get('Jira', 'password')

        # The jira communications class
        self.jira = None

    def issue(self, id):
        if self.jira is None:
            self.jira = JIRA(options={'server': self.jira_server}, basic_auth=(self.jira_user, self.jira_password))

        try:
            return self.jira.issue(id)
        except JIRAError as err:
            print(err.args)
            return "Error finding issue, \"" + err.args[1] + "\""