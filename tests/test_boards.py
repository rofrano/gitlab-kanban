import os
from unittest import TestCase
from kanban.models import GitLab, Board, gitlab

GITLAB_TOKEN = os.getenv("GITLAB_TOKEN")
GITLAB_PROJECT = os.getenv("GITLAB_PROJECT")

class TestBoards(TestCase):
    """Test Kanban Boards"""

    gitlab: GitLab

    @classmethod
    def setUpClass(cls):
        cls.gitlab = GitLab(GITLAB_PROJECT, GITLAB_TOKEN)

    def test_create_board(self):
        """It should create a Kanban board"""
        board = Board("Testing")
        board.init(self.gitlab)
        data = Board.find_by_name("Development")
        raise Exception(data)
        # board.create()
        # self.assertIsNone(board.id)