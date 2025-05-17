from pydantic_settings import BaseSettings
from typing import Optional
from pathlib import Path
import sys
import yaml


class HomeAssistantEntity(BaseSettings):
    """Nested setting"""

    id: str
    display_name: str


class Settings(BaseSettings, extra="allow"):
    # Secrets from .env
    BEARER_TOKEN: str
    API_HOST: str

    # Config values from yaml
    api_host: Optional[str] = None
    api_endpoint_history: Optional[str] = None
    timeout: int = 30
    retry_attempts: int = 3
    log_level: str = "INFO"
    entities: list[HomeAssistantEntity] = []

    @classmethod
    def _update_nested_settings(cls, settings_obj, config_dict):
        """Update settings with values from config dictionary."""
        for key, value in config_dict.items():
            if hasattr(settings_obj, key):
                if key == "entities" and isinstance(value, list):
                    # Handle list of entities
                    entities = []
                    for entity_dict in value:
                        entity = HomeAssistantEntity(**entity_dict)
                        entities.append(entity)
                    setattr(settings_obj, key, entities)
                else:
                    setattr(settings_obj, key, value)

    @classmethod
    def load_config(cls):
        try:
            config_path = Path("config.yaml")
            if not config_path.exists():
                raise FileNotFoundError("config.yaml not found")

            with open(config_path, "r") as file:
                yaml_config = yaml.safe_load(file)

            if not isinstance(yaml_config, dict):
                raise ValueError("Invalid YAML configuration format")

            # Create settings instance (this will automatically load from .env)
            settings = cls()

            # Update with YAML values recursively
            cls._update_nested_settings(settings, yaml_config)

            return settings

        except (yaml.YAMLError, FileNotFoundError, ValueError) as e:
            print(f"Configuration error: {e}", file=sys.stderr)
            sys.exit(1)

    class Config:
        env_file = ".env"
        case_sensitive = True


# Initialize settings
settings = Settings.load_config()
