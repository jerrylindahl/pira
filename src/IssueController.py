from src.JiraInterface import JiraInterface


class IssueController:
    def __init__(self, config):
        self.config = config
        self.jira = JiraInterface(self.config)
    
    def get_issue(self, id):
        jira_issue = self.jira.issue(id)
        issue = Issue(id, jira_issue.fields.summary, self.config)
        return issue


class Issue:
    def __init__(self, id, summary, config):
        self.id = id
        self.summary = summary
        
        jira = config.get('Jira', 'server')
        self.html = "<p><a href='%(jira)s/browse/%(id)s'>%(id)s</a> Summary: %(summary)s</p>" % {
            "jira": jira, "id": self.id, "summary": self.summary
        }