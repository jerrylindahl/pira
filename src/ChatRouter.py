import re

class ChatRouter:

    def __init__(self, chat, config):
        self.chat = chat
        self.chat.callBack = self
        self.regex = config.get('Chat', 'issue-regex')

        self.DataStore = None

    def run(self):
        self.chat.run()

    # Interface methods:
    def msg_rec(self, nick, body):
        print("Rec msg:", body)

    def get_issues(self, body):
        result = []
        m = re.findall(self.regex, body.upper())
        for match in m:
            print("Found match", match)
            result.append(match)

        return result


