import requests
import datetime

import pandas as pd

from src.api.energy_data import parse_energy_data
from src.config.settings import settings


class APIClient:
    def __init__(self):
        self.base_url = settings.api_host
        self.history_url = self.base_url + settings.api_endpoint_history
        self.bearer_token = settings.BEARER_TOKEN
        self.timeout = settings.timeout

    def _get_headers(self):
        return {
            "Authorization": f"Bearer {self.bearer_token}",
            "Content-Type": "application/json",
        }

    def get_history_data(self, start_date: datetime) -> pd.DataFrame:
        if not start_date:
            date = datetime.datetime.now().strftime("%Y-%m-%d")
        else:
            date = start_date

        request_params = "?filter_entity_id=sensor.myenergi_home_zappi_hub_generated_today_2&minimal_response=true"

        response = requests.get(
            self.history_url + date + request_params,
            headers=self._get_headers(),
            timeout=self.timeout,
        )

        if response.status_code == 200:
            return parse_energy_data(response.json())

        else:
            response.raise_for_status()

    def post_data(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        headers = self._get_headers()

        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 201:
            return response.json()
        else:
            response.raise_for_status()
