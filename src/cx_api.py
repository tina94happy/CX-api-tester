# cx_api.py

import requests


class CXAPI:
    def __init__(self, cx_config):
        self.cx_config = cx_config
        self.base_url = 'https://sng.ast.checkmarx.net/api'
        self.login_base_url = 'https://sng.iam.checkmarx.net'
        self.access_token = self.login()

    def login(self):
        url = f'{self.login_base_url}/auth/realms/{self.cx_config["tenant_name"]}/protocol/openid-connect/token'
        data = {
            'client_id': self.cx_config['client_id'],
            'grant_type': "client_credentials",
            'client_secret': self.cx_config['client_secret']
        }
        headers = {
            'Accept': 'application/json'
        }
        response = requests.post(url=url, data=data, headers=headers)

        access_token = response.json()['access_token']
        return access_token

    def get_project_count(self):
        # 使用 CX API 取得專案數量
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Accept': 'application/json'
        }
        response = requests.get(f'{self.base_url}/projects', headers=headers)
        project_count = response.json()['totalCount']
        return project_count
