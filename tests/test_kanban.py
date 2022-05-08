import os
import unittest
from unittest.mock import patch
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

    @patch.dict(os.environ, {}, clear=True)
    def test_create_help_no_token(self):
        """It should return an error for create help without a token"""
        result = self.runner.invoke(cli, ["-p=1", "create", "--help"])
        self.assertNotEqual(result.exit_code, 0)
        self.assertIn("Error: Missing option '-t' / '--token'.", result.output)

    @patch.dict(os.environ, {"GITLAB_TOKEN": "foo"}, clear=True)
    def test_create_help_with_token(self):
        """It should return create help with token from environment"""
        result = self.runner.invoke(cli, ["-p=1", "create", "--help"])
        self.assertEqual(result.exit_code, 0)

    @patch.dict(os.environ, {}, clear=True)
    def test_create_help_no_project(self):
        """It should return an error for create help without a project"""
        result = self.runner.invoke(cli, ["-t=1", "create", "--help"])
        self.assertNotEqual(result.exit_code, 0)
        self.assertIn("Error: Missing option '-p' / '--project'.", result.output)

    @patch.dict(os.environ, {"GITLAB_PROJECT": "foo"}, clear=True)
    def test_create_help_with_project(self):
        """It should return create help with project from environment"""
        result = self.runner.invoke(cli, ["-t=1", "create", "--help"])
        self.assertEqual(result.exit_code, 0)


    ######################################################################
    # Get test cases
    ######################################################################

    def test_get_help(self):
        """It should return get help"""
        result = self.runner.invoke(cli, ["-t=1", "-p=1", "get", "--help"])
        self.assertEqual(result.exit_code, 0)

    @patch.dict(os.environ, {}, clear=True)
    def test_get_help_no_token(self):
        """It should return an error for get help without a token"""
        result = self.runner.invoke(cli, ["-p=1", "get", "--help"])
        self.assertNotEqual(result.exit_code, 0)
        self.assertIn("Error: Missing option '-t' / '--token'.", result.output)

    @patch.dict(os.environ, {"GITLAB_TOKEN": "foo"}, clear=True)
    def test_get_help_with_token(self):
        """It should return get help with token from environment"""
        result = self.runner.invoke(cli, ["-p=1", "get", "--help"])
        self.assertEqual(result.exit_code, 0)

    @patch.dict(os.environ, {}, clear=True)
    def test_get_help_no_project(self):
        """It should return an error for get help without a project"""
        result = self.runner.invoke(cli, ["-t=1", "get", "--help"])
        self.assertNotEqual(result.exit_code, 0)
        self.assertIn("Error: Missing option '-p' / '--project'.", result.output)

    @patch.dict(os.environ, {"GITLAB_PROJECT": "foo"}, clear=True)
    def test_get_help_with_project(self):
        """It should return get help with project from environment"""
        result = self.runner.invoke(cli, ["-t=1", "get", "--help"])
        self.assertEqual(result.exit_code, 0)
