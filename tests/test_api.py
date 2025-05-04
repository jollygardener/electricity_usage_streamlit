import pytest
from src.api.home_assistant_client import APIClient


@pytest.fixture
def api_client():
    return ApiClient(base_url="http://example.com/api", token="your_token_here")


def test_get_data_success(api_client):
    response = api_client.get_data()
    assert response.status_code == 200
    assert "data" in response.json()


def test_get_data_failure(api_client):
    api_client.base_url = "http://invalid-url.com"
    response = api_client.get_data()
    assert response.status_code != 200


def test_handle_response(api_client):
    response = api_client.handle_response({"data": "test"})
    assert response == "test"  # Adjust based on actual response handling logic


def test_api_client_initialization():
    client = ApiClient(base_url="http://example.com/api", token="your_token_here")
    assert client.base_url == "http://example.com/api"
    assert client.token == "your_token_here"
