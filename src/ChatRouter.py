import re


class ChatRouter:

    def __init__(self, chat, config):
        self.chat = chat
        self.chat.callBack = self
        self.regex = config.get('Chat', 'issue-regex')

        self.config = config
        self.DataStore = None
        self.IssueController = None
        self.quotes = None

    def run(self):
        self.chat.run()

    # Interface methods:
    def msg_rec(self, room, nick, body):
        if "sirjenkins" in nick:
            return
        if body[0:2] == "42":
            if self.quotes:
                self.chat.send_message(
                    mto=room,
                    mbody=self.quotes.get_random(),
                    mtype='groupchat')
        else:
            self.reply_to_issues(room, nick, body)

    def reply_to_issues(self, room, nick, body):
        issue_ids = self.get_issues(body)

        issues = []
        if len(issue_ids):
            issues = self.IssueController.get_issues(issue_ids)

        for issue in issues:
            if issue.error:
                self.chat.send_message(
                    mto=room,
                    mbody=issue.id + " " + issue.error,
                    mtype='groupchat')
            else:
                self.chat.send_message(
                    mto=room,
                    mbody=issue.id + " Summary: " + issue.summary,
                    mtype='groupchat',
                    mhtml=issue.slackMarkupSimple) #temporarily break jabber func. while on hackathon

    def get_issues(self, body):
        result = []
        m = re.findall(self.regex, body.upper())
        for match in m:
            result.append(match)

        return result


