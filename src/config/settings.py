from pydantic_settings import BaseSettings
from typing import Optional
from pathlib import Path
import sys
import yaml


class Settings(BaseSettings):
    # Secrets from .env
    BEARER_TOKEN: str

    # Config values from yaml
    api_endpoint: Optional[str] = None
    timeout: int = 30
    retry_attempts: int = 3
    log_level: str = "INFO"

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

            # Update with YAML values
            for key, value in yaml_config.items():
                if hasattr(settings, key):
                    setattr(settings, key, value)

            return settings

        except (yaml.YAMLError, FileNotFoundError, ValueError) as e:
            print(f"Configuration error: {e}", file=sys.stderr)
            sys.exit(1)

    class Config:
        env_file = ".env"
        case_sensitive = True


# Initialize settings
settings = Settings.load_config()
