"""
GitLab Module

This module contains the GitLab class which implements
the HTTP calls GET, POST, PUT, and DELETE to GitLab
"""
import requests

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


    def get(self, path: str) -> dict:
        """GET the GitLab URL for the path"""
        payload = []
        result = requests.get(
            f'{self.url}/api/v4/projects/{self.project}/{path}', 
            headers=self.headers
        )
        if result.status_code == 200:
            payload = result.json()
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
        return payload


    def delete(self, path: str) -> None:
        """DELETE from the GitLab URL for the path"""
        result = requests.delete(
            f'{self.url}/api/v4/projects/{self.project}/{path}', 
            headers=self.headers
        )
        if result.status_code != 204:
            raise Exception("Delete failed")
