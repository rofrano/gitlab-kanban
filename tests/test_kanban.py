######################################################################
# Copyright 2022 John Rofrano. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
######################################################################

import os
import unittest
from unittest.mock import patch
from click.testing import CliRunner
from kanban.cli import cli
from kanban.cli import csv_to_dict

class TestKanban(unittest.TestCase):
    """Test Cases for kanban commands"""

    def setUp(self):
        self.runner = CliRunner()

    def test_help(self):
        """It should return help"""
        result = self.runner.invoke(cli, ["--help"])
        self.assertEqual(result.exit_code, 0)

    def test_csv_to_dict(self):
        """It should convert a CSV file to dictionary format"""
        results = csv_to_dict("tests/fixtures/test_board_labels.csv")
        self.assertIsNotNone(results)
        self.assertEqual(len(results), 4)
        self.assertIsInstance(results[0], dict)

    ######################################################################
    # Boards test cases
    ######################################################################

    def test_boards_help(self):
        """It should return board help"""
        result = self.runner.invoke(cli, ["-t=1", "-p=1", "boards", "--help"])
        self.assertEqual(result.exit_code, 0)

    def test_boards_create_help(self):
        """It should return board create help"""
        result = self.runner.invoke(cli, ["-t=1", "-p=1", "boards", "create", "--help"])
        self.assertEqual(result.exit_code, 0)

    def test_boards_delete_help(self):
        """It should return board delete help"""
        result = self.runner.invoke(cli, ["-t=1", "-p=1", "boards", "delete", "--help"])
        self.assertEqual(result.exit_code, 0)

    def test_boards_list_help(self):
        """It should return board list help"""
        result = self.runner.invoke(cli, ["-t=1", "-p=1", "boards", "list", "--help"])
        self.assertEqual(result.exit_code, 0)

    @patch.dict(os.environ, {}, clear=True)
    def test_boards_create_help_no_token(self):
        """It should return an error for boards create help without a token"""
        result = self.runner.invoke(cli, ["-p=1", "boards", "create", "--help"])
        self.assertNotEqual(result.exit_code, 0)
        self.assertIn("Error: Missing option '-t' / '--token'.", result.output)

    @patch.dict(os.environ, {"GITLAB_TOKEN": "foo"}, clear=True)
    def test_boards_create_help_with_token(self):
        """It should return boards create help with token from environment"""
        result = self.runner.invoke(cli, ["-p=1", "boards", "create", "--help"])
        self.assertEqual(result.exit_code, 0)

    @patch.dict(os.environ, {}, clear=True)
    def test_boards_create_help_no_project(self):
        """It should return an error for boards create help without a project"""
        result = self.runner.invoke(cli, ["-t=1", "boards", "create", "--help"])
        self.assertNotEqual(result.exit_code, 0)
        self.assertIn("Error: Missing option '-p' / '--project'.", result.output)

    @patch.dict(os.environ, {"GITLAB_PROJECT": "foo"}, clear=True)
    def test_boards_create_help_with_project(self):
        """It should return boards create help with project from environment"""
        result = self.runner.invoke(cli, ["-t=1", "boards", "create", "--help"])
        self.assertEqual(result.exit_code, 0)


    ######################################################################
    # Issues test cases
    ######################################################################

    def test_issues_help(self):
        """It should return issues help"""
        result = self.runner.invoke(cli, ["-t=1", "-p=1", "issues", "--help"])
        self.assertEqual(result.exit_code, 0)

    def test_issues_create_help(self):
        """It should return issues create help"""
        result = self.runner.invoke(cli, ["-t=1", "-p=1", "issues", "create", "--help"])
        self.assertEqual(result.exit_code, 0)

    def test_issues_delete_help(self):
        """It should return issues delete help"""
        result = self.runner.invoke(cli, ["-t=1", "-p=1", "issues", "delete", "--help"])
        self.assertEqual(result.exit_code, 0)

    def test_issues_list_help(self):
        """It should return issues list help"""
        result = self.runner.invoke(cli, ["-t=1", "-p=1", "issues", "list", "--help"])
        self.assertEqual(result.exit_code, 0)

    @patch.dict(os.environ, {}, clear=True)
    def test_issues_create_help_no_token(self):
        """It should return an error for boards create help without a token"""
        result = self.runner.invoke(cli, ["-p=1", "issues", "create", "--help"])
        self.assertNotEqual(result.exit_code, 0)
        self.assertIn("Error: Missing option '-t' / '--token'.", result.output)

    @patch.dict(os.environ, {"GITLAB_TOKEN": "foo"}, clear=True)
    def test_issues_create_help_with_token(self):
        """It should return issues create help with token from environment"""
        result = self.runner.invoke(cli, ["-p=1", "issues", "create", "--help"])
        self.assertEqual(result.exit_code, 0)

    @patch.dict(os.environ, {}, clear=True)
    def test_issues_create_help_no_project(self):
        """It should return an error for boards create help without a project"""
        result = self.runner.invoke(cli, ["-t=1", "issues", "create", "--help"])
        self.assertNotEqual(result.exit_code, 0)
        self.assertIn("Error: Missing option '-p' / '--project'.", result.output)

    @patch.dict(os.environ, {"GITLAB_PROJECT": "foo"}, clear=True)
    def test_issues_create_help_with_project(self):
        """It should return issues create help with project from environment"""
        result = self.runner.invoke(cli, ["-t=1", "issues", "create", "--help"])
        self.assertEqual(result.exit_code, 0)

    ######################################################################
    # Issues test cases
    ######################################################################

    def test_labels_help(self):
        """It should return labels help"""
        result = self.runner.invoke(cli, ["-t=1", "-p=1", "labels", "--help"])
        self.assertEqual(result.exit_code, 0)

    def test_labels_create_help(self):
        """It should return labels create help"""
        result = self.runner.invoke(cli, ["-t=1", "-p=1", "labels", "create", "--help"])
        self.assertEqual(result.exit_code, 0)

    def test_labels_delete_help(self):
        """It should return labels delete help"""
        result = self.runner.invoke(cli, ["-t=1", "-p=1", "labels", "delete", "--help"])
        self.assertEqual(result.exit_code, 0)

    def test_labels_list_help(self):
        """It should return labels list help"""
        result = self.runner.invoke(cli, ["-t=1", "-p=1", "labels", "list", "--help"])
        self.assertEqual(result.exit_code, 0)

    @patch.dict(os.environ, {}, clear=True)
    def test_labels_create_help_no_token(self):
        """It should return an error for boards create help without a token"""
        result = self.runner.invoke(cli, ["-p=1", "labels", "create", "--help"])
        self.assertNotEqual(result.exit_code, 0)
        self.assertIn("Error: Missing option '-t' / '--token'.", result.output)

    @patch.dict(os.environ, {"GITLAB_TOKEN": "foo"}, clear=True)
    def test_labels_create_help_with_token(self):
        """It should return labels create help with token from environment"""
        result = self.runner.invoke(cli, ["-p=1", "labels", "create", "--help"])
        self.assertEqual(result.exit_code, 0)

    @patch.dict(os.environ, {}, clear=True)
    def test_labels_create_help_no_project(self):
        """It should return an error for boards create help without a project"""
        result = self.runner.invoke(cli, ["-t=1", "labels", "create", "--help"])
        self.assertNotEqual(result.exit_code, 0)
        self.assertIn("Error: Missing option '-p' / '--project'.", result.output)

    @patch.dict(os.environ, {"GITLAB_PROJECT": "foo"}, clear=True)
    def test_labels_create_help_with_project(self):
        """It should return labels create help with project from environment"""
        result = self.runner.invoke(cli, ["-t=1", "labels", "create", "--help"])
        self.assertEqual(result.exit_code, 0)

