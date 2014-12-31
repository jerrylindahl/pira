
from jira.client import JIRA
from jira.client import GreenHopper

class JiraInterface:
    def __init__(self, config):
        self.jira_server = None
        self.jira_user = None
        self.jira_password = None

        self.config = config
        self.jira_server = self.config.get('Jira', 'server')
        self.jira_user = self.config.get('Jira', 'user')
        self.jira_password = self.config.get('Jira', 'password')


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
