import signal
import time

import configparser

from jira.client import JIRA
from jira.client import GreenHopper

from src.ChatFactory import ChatFactory
from src.ChatRouter import ChatRouter


class Main():
    def __init__(self):
        self.chat = None
        self.config = None
        self.jira_server = None
        self.jira_user = None
        self.jira_password = None


    def receive_signal(self, signum, _):
        if signum == signal.SIGINT:
            self.shutdown()
        else:
            print('Unknown signal', signum)
            signal.getsignal()

    def main(self):
        signal.signal(signal.SIGINT, self.receive_signal)
        #ds = DataStore()
        #ds.mongo()

        self.config = self.get_config('pira.cfg')
        self.jira_server = self.config.get('Jira', 'server')
        self.jira_user = self.config.get('Jira', 'user')
        self.jira_password = self.config.get('Jira', 'password')

        #issue()
        #board()
        self.init_chat()
        chatRouter = ChatRouter(self.chat, self.config)
        chatRouter.run()
        print("chat initeddb")
        self.main_loop()
        self.shutdown()

    def main_loop(self):
        while True:
            time.sleep(1)

    def shutdown(self):
        print('Shutting down.')
        self.chat.disconnect()
        exit(0)

    def init_chat(self):
        cf = ChatFactory()
        self.chat = cf.getJabberChat(self.config)

    def board(self):
        gh = GreenHopper({'server': self.jira_server}, basic_auth=(self.jira_user, self.jira_password))
        board_id = 709
        sprint_id = 1630


        sprints = gh.sprints(board_id)
        issues = gh.incompleted_issues(board_id, sprint_id)

        print(*issues)

        #for sprint in sprints:
        #    sprint_id = sprint.id
        #    print("Sprint: %s" % sprint.name)
        #    incompleted_issues = gh.incompleted_issues(board_id, sprint_id)
        #    print("Incomplete issues: %s" % ', '.join(issue.key for issue in incompleted_issues))

    def issue(self):
        jira = JIRA(options={'server': self.jira_server}, basic_auth=(self.jira_user, self.jira_password))


        issue = jira.issue('MFOL-18539')
        print("issue " + issue.__str__())
        for comment in issue.fields.comment.comments:
            print("Comment" + comment.__str__())



        print("summary " + issue.fields.summary)

        jra = jira.project('MFOL')
        print("Jra " + jra.__str__())

        versions = jira.project_versions(jra)
        [v.name for v in reversed(versions)]
        for v in versions:
            print("version " + v.__str__())

    def get_config(self, file):
        config = configparser.RawConfigParser()
        config.read(file)
        return config



if __name__ == "__main__":
    main = Main()
    main.main()
