class APIClient:
    def __init__(self, base_url, bearer_token):
        self.base_url = base_url
        self.bearer_token = bearer_token

    def _get_headers(self):
        return {
            "Authorization": f"Bearer {self.bearer_token}",
            "Content-Type": "application/json",
        }

    def get_data(self, endpoint):
        import requests

        url = f"{self.base_url}/{endpoint}"
        headers = self._get_headers()

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def post_data(self, endpoint, data):
        import requests

        url = f"{self.base_url}/{endpoint}"
        headers = self._get_headers()

        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 201:
            return response.json()
        else:
            response.raise_for_status()
