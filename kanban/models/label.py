"""
Label Class

This model manipulates a Label in GitLab
"""
import logging
from .gitlab import GitLab

logger = logging.getLogger()

HTML_COLORS = [
    "black", "silver", "gray", "white", "maroon", "red", "purple", 
    "fuchsia", "green", "lime", "olive", "yellow", "navy", "blue", "teal", "aqua"
]

class Label():
    """Manipulates Labels in GitLab"""

    gitlab: GitLab = None

    def __init__(self, gitlab: GitLab):
        """Constructor"""
        self.gitlab = gitlab

    def create(self, data: dict ):
        """Creates a label in GitLab"""
        results = self.gitlab.post('labels', data)
        if not results:
            logger.error(f"Create failed!")


    @classmethod
    def find_by_name(cls, name: str) -> list:
        """Find a label by it's name"""
        labels = Label.gitlab.get('labels')
        result = [label for label in labels if label["name"] == name]
        return result
