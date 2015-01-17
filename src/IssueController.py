from src.JiraInterface import JiraInterface


class IssueController:
    def __init__(self, config):
        self.config = config
        self.jira = JiraInterface(self.config)

    def get_issues(self, ids):
        return [self.make_issue(jid, self.jira.issue(jid)) for jid in ids]

    def make_issue(self, jid, jira_result):
        if isinstance(jira_result, str):
            return Issue(jid, error=jira_result)
        else:
            return Issue(jid, summary=jira_result.fields.summary, config=self.config)


class Issue:
    def __init__(self, id, summary=None, config=None, error=None):
        self.id = id
        self.summary = summary
        self.error = error

        if config:
            jira = config.get('Jira', 'server')
            self.html = "<p><a href='%(jira)s/browse/%(id)s'>%(id)s</a> Summary: %(summary)s</p>" % {
                "jira": jira, "id": self.id, "summary": self.summary
            }