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
import logging
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

    ######################################################################
    # Boards test cases
    ######################################################################
