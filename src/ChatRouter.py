import re

from src.IssueController import Issue

class ChatRouter:

    def __init__(self, chat, config):
        self.chat = chat
        self.chat.callBack = self
        self.regex = config.get('Chat', 'issue-regex')
        self.cache_enabled = config.getboolean('Cache', 'enabled')

        self.config = config
        self.DataStore = None
        self.IssueController = None

    def run(self):
        self.chat.run()

    # Interface methods:
    def msg_rec(self, room, nick, body):
        if "sirjenkins" in body:
            return

        issues = self.get_issues(body)
        issue = None
        
        if len(issues):
            if self.cache_enabled:
                pass
            else:
                issue = self.IssueController.get_issue(issues[0])

        if isinstance(issue, str):
            self.chat.send_message(mto=room, mbody=issue, mtype='groupchat')
        elif isinstance(issue, Issue):
            self.chat.send_message(
                mto=room,
                mbody=issue.id + " Summary: " + issue.summary,
                mtype='groupchat',
                mhtml=issue.html)
        else:
            print("Invalid issue from issue controller")

    def get_issues(self, body):
        result = []
        m = re.findall(self.regex, body.upper())
        for match in m:
            result.append(match)

        return result


