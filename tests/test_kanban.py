import unittest
from click.testing import CliRunner
from kanban.cli import cli

class TestKanban(unittest.TestCase):
    """Test Cases kanban command"""

    def setUp(self):
        self.runner = CliRunner()

    def test_help(self):
        """It should return help"""
        result = self.runner.invoke(cli, ["--help"])
        self.assertEqual(result.exit_code, 0)

    ######################################################################
    # Create test cases
    ######################################################################

    def test_create_help(self):
        """It should return create help"""
        result = self.runner.invoke(cli, ["-t=1", "-p=1", "create", "--help"])
        self.assertEqual(result.exit_code, 0)

    def test_create_help_no_token(self):
        """It should return an error for create help without a token"""
        result = self.runner.invoke(cli, ["-p=1", "create", "--help"])
        self.assertNotEqual(result.exit_code, 0)
        assert (
            "Error: Missing option '-t' / '--token'." in result.output
        )

    def test_create_help_no_project(self):
        """It should return an error for create help without a project"""
        result = self.runner.invoke(cli, ["-t=1", "create", "--help"])
        self.assertNotEqual(result.exit_code, 0)
        assert (
            "Error: Missing option '-p' / '--project'." in result.output
        )


    ######################################################################
    # Get test cases
    ######################################################################

    def test_get_help(self):
        """It should return get help"""
        result = self.runner.invoke(cli, ["-t=1", "-p=1", "get", "--help"])
        self.assertEqual(result.exit_code, 0)

    def test_get_help_no_token(self):
        """It should return an error for get help without a token"""
        result = self.runner.invoke(cli, ["-p=1", "create", "--help"])
        self.assertNotEqual(result.exit_code, 0)
        assert (
            "Error: Missing option '-t' / '--token'." in result.output
        )

    def test_get_help_no_project(self):
        """It should return an error for get help without a project"""
        result = self.runner.invoke(cli, ["-t=1", "create", "--help"])
        self.assertNotEqual(result.exit_code, 0)
        assert (
            "Error: Missing option '-p' / '--project'." in result.output
        )
