import unittest
from unittest.mock import patch
from src.api.home_assistant_client import APIClient


class TestAPIClient(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://test.com"
        self.bearer_token = "test_token"
        self.client = APIClient(self.base_url, self.bearer_token)

    def test_get_headers(self):
        expected_headers = {
            "Authorization": "Bearer test_token",
            "Content-Type": "application/json",
        }
        self.assertEqual(self.client._get_headers(), expected_headers)

    @patch("requests.get")
    def test_get_data_success(self, mock_get):
        # Mock successful response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"data": "test"}

        result = self.client.get_data("endpoint")

        mock_get.assert_called_once_with(
            "http://test.com/endpoint", headers=self.client._get_headers()
        )
        self.assertEqual(result, {"data": "test"})

    @patch("requests.get")
    def test_get_data_error(self, mock_get):
        # Mock error response
        mock_get.return_value.status_code = 404
        mock_get.return_value.raise_for_status.side_effect = Exception("Not Found")

        with self.assertRaises(Exception):
            self.client.get_data("endpoint")
