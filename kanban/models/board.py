"""
Kanban Board
"""
from .gitlab import GitLab

class Board():
    """Represents a Kanban Board in GitLab"""

    gitlab: GitLab = None

    def __init__(self, name: str):
        """Constructor"""
        self.name = name
        self.id = None
        self.lists = []
        self.data = {}

    def __repr__(self):
        return '<Board %r>' % self.name

    def init(self, gitlab: GitLab) -> None:
        """Sets the GitLab instance"""
        Board.gitlab = gitlab

    def serialize(self) -> dict:
        """Serializes the class as a dictionary"""
        return {
            "id": self.id,
            "name": self.name,
            "lists": self.lists
        }

    def deserialize(self, data: dict) -> None:
        """Sets attributes from a dictionary"""
        for key, value in data.items():
            setattr(self, key, value)

    def create(self):
        """Creates a kanban board in GitLab"""
        board = self.serialize()
        # Create the board first
        results = self.gitlab.post('boards', board)
        if results:
            self.id = results["id"]
            self.data = results
            # Update the lists
            if self.lists:
                path = f"boards/{self.id}"
                data = self.serialize()
                data["lists"] = [label["name"] for label in self.lists]
                results = self.gitlab.put(path, data)
                print(results)

    @classmethod
    def find_by_name(cls, name: str) -> list:
        """Find a board by it's name"""
        boards = Board.gitlab.get('boards')
        result = [board for board in boards if board["name"] == name]
        return result
