import pytest
from pathlib import Path
import yaml
from src.config.settings import HomeAssistantEntity, Settings
from unittest.mock import patch, mock_open


@pytest.fixture
def sample_yaml_config():
    return """
    api_host: "test.api.com"
    api_endpoint_history: "/history"
    timeout: 60
    retry_attempts: 5
    log_level: "DEBUG"
    entities:
      - id: "sensor1"
        display_name: "Sensor 1"
      - id: "sensor2"
        display_name: "Sensor 2"
    """


@pytest.fixture
def sample_yaml_with_entities():
    return """
    api_host: "test.api.com"
    entities:
        - id: "sensor.electricity_meter"
          display_name: "Main Electricity Meter"
        - id: "sensor.solar_production"
          display_name: "Solar Panel Production"
    """


@pytest.fixture
def mock_env_vars():
    return {"BEARER_TOKEN": "test_token", "API_HOST": "test.host.com"}


class TestSettings:
    def test_load_config_with_valid_yaml(self, sample_yaml_config, mock_env_vars):
        with patch.dict("os.environ", mock_env_vars), patch(
            "builtins.open", mock_open(read_data=sample_yaml_config)
        ), patch("pathlib.Path.exists", return_value=True):

            settings = Settings.load_config()

            # Test basic settings
            assert settings.api_host == "test.api.com"
            assert settings.timeout == 60
            assert settings.retry_attempts == 5
            assert settings.log_level == "DEBUG"

            # Test env variables
            assert settings.BEARER_TOKEN == "test_token"
            assert settings.API_HOST == "test.host.com"

            # Test entities
            assert settings.entities is not None
            assert len(settings.entities) == 2
            assert isinstance(settings.entities[0], HomeAssistantEntity)
            assert settings.entities[0].id == "sensor1"
            assert settings.entities[0].display_name == "Sensor 1"

    def test_load_config_with_entities(self, sample_yaml_with_entities, mock_env_vars):
        with patch.dict("os.environ", mock_env_vars), patch(
            "builtins.open", mock_open(read_data=sample_yaml_with_entities)
        ), patch("pathlib.Path.exists", return_value=True):

            settings = Settings.load_config()

            # Test entities are properly loaded
            assert settings.entities is not None
            assert len(settings.entities) == 2
            assert isinstance(settings.entities[0], HomeAssistantEntity)
            assert settings.entities[0].id == "sensor.electricity_meter"
            assert settings.entities[0].display_name == "Main Electricity Meter"
            assert settings.entities[1].id == "sensor.solar_production"
            assert settings.entities[1].display_name == "Solar Panel Production"

    def test_load_config_file_not_found(self):
        with patch("pathlib.Path.exists", return_value=False):
            with pytest.raises(SystemExit):
                Settings.load_config()

    def test_load_config_invalid_yaml(self, mock_env_vars):
        invalid_yaml = "invalid: yaml: content: ["

        with patch.dict("os.environ", mock_env_vars), patch(
            "builtins.open", mock_open(read_data=invalid_yaml)
        ), patch("pathlib.Path.exists", return_value=True):

            with pytest.raises(SystemExit):
                Settings.load_config()

    def test_load_config_non_dict_yaml(self, mock_env_vars):
        invalid_yaml = "- just\n- a\n- list"

        with patch.dict("os.environ", mock_env_vars), patch(
            "builtins.open", mock_open(read_data=invalid_yaml)
        ), patch("pathlib.Path.exists", return_value=True):

            with pytest.raises(SystemExit):
                Settings.load_config()
