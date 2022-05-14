"""
Issue Class

This model manipulates a Issue in GitLab
"""
import logging
import urllib.parse
from .gitlab import GitLab

logger = logging.getLogger()


class Issue():
    """Manipulates a Issue in GitLab"""

    gitlab: GitLab = None

    def __init__(self, gitlab: GitLab):
        """Constructor"""
        self.gitlab = gitlab

    def create(self, data: dict ):
        """Creates a issue in GitLab"""
        results = self.gitlab.post('issues', data)
        if not results:
            logger.error(f"Create Issue failed!")

    def delete_by_id(self, issue_id: str ):
        """Deletes a issue in GitLab by id"""
        self.gitlab.delete(f'issues/{issue_id}')

    def delete(self, data: dict):
        """Deletes a issue in GitLab"""
        issues = self.find_by_title(data["title"])
        for issue in issues:
            self.delete_by_id(issue['iid'])

    def delete_all(self):
        """Deletes all issue in the Project"""
        issues = self.all()
        for issue in issues:
            self.delete_by_id(issue['iid'])

    def all(self) -> list:
        return self.gitlab.get('issues')

    def find_by_title(self, title: str) -> list:
        """Find a issue by it's title"""
        issues = self.all()
        result = [issue for issue in issues if issue["title"] == title]
        return result
