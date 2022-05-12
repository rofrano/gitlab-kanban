"""
GitLab Module

This module contains the GitLab class which implements
the HTTP calls GET, POST, PUT, and DELETE to GitLab
"""
import logging
import requests

logger = logging.getLogger()

######################################################################
# G I T L A B   W R A P P E R   C L A S S
######################################################################
class GitLab():
    """A GitLab Wrapper"""

    def __init__(self, project:str, token: str, url: str="https://gitlab.com"):
        self.project = project
        self.token = token
        self.url = url
        self.headers = {'Authorization': f'Bearer {self.token}'}

    def __repr__(self):
        return '<GitLab %r>' % self.project

    def get(self, path: str) -> dict:
        """GET the GitLab URL for the path"""
        payload = []
        result = requests.get(
            f'{self.url}/api/v4/projects/{self.project}/{path}', 
            headers=self.headers
        )
        if result.status_code == 200:
            payload = result.json()
        else:
            logger.error(f"GET failed: RC={result.status_code} message={result}")
        return payload


    def post(self, path: str, data: dict) -> dict:
        """POST to the GitLab URL for the path"""
        payload = {}
        headers = self.headers | {'Content-Type': 'application/json'}
        result = requests.post(
            f'{self.url}/api/v4/projects/{self.project}/{path}', 
            json=data,
            headers=headers
        )
        if result.status_code == 201:
            payload = result.json()
        else:
            logger.error(f"POST failed: RC={result.status_code} message={result.text}")
        return payload

    def put(self, path: str, data: dict) -> dict:
        """PUT the GitLab URL for the path"""
        payload = {}
        headers = self.headers | {'Content-Type': 'application/json'}
        result = requests.put(
            f'{self.url}/api/v4/projects/{self.project}/{path}', 
            json=data,
            headers=headers
        )
        if result.status_code == 200:
            payload = result.json()
        else:
            logger.error(f"PUT failed: RC={result.status_code} message={result}")
        return payload


    def delete(self, path: str) -> None:
        """DELETE from the GitLab URL for the path"""
        result = requests.delete(
            f'{self.url}/api/v4/projects/{self.project}/{path}', 
            headers=self.headers
        )
        if result.status_code != 204:
            logger.error(f"DELETE failed: RC={result.status_code} message={result}")
