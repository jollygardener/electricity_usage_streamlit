# Electricity Usage Streamlit App

## Project Overview
The Electricity Usage Streamlit App is designed to visualize and analyze electricity usage data by connecting to an external API. This application integrates seamlessly with Home Assistant, allowing users to monitor their energy consumption in real-time.

## Features
- Connects to Home Assistant API using a bearer token for secure access.
- Displays real-time electricity usage data in an interactive format.
- User-friendly interface built with Streamlit for easy navigation and data visualization.

## Prerequisites
- Python 3.13: installation for macOS [here](https://www.python.org/downloads/macos/)
- Streamlit: installation instructions [here](https://docs.streamlit.io/get-started/installation/command-line)
- Home Assistant API access, using bearer token: docs [here](https://developers.home-assistant.io/docs/api/rest)
- Other dependencies (list them here)

## Installation
1. Clone the repository
2. Navigate to the project directory
3. Add venv .venv directory
4. Activate python venv
5. Install the required dependencies

    ```bash
    git clone https://github.com/your-repo/electricity_usage_streamlit.git
    cd electricity_usage_streamlit
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

## Configuration
* Using Pydantic, environment variables keep your secrets out of the code base- you need to add  your own values in .env file
* Other configs are stored in config.yaml
    ```text
    /electricity_usage_streamlit
    ├── .env
    ├── config.yaml
    ├── requirements.txt
    ├── [readme.md](http://_vscodecontentref_/0)
    └── ...


## Development setup
Black is used as a pre-commit hook to keep the code tidy.  Here are steps for first time setup:
    ```bash
    # Install pre-commit
    pip install -r requirements-dev.txt

    # Install the git hook scripts
    pre-commit install

    # Optional: run against all files
    pre-commit run --all-files

### VSCode extensions used
* [Rest client](https://marketplace.visualstudio.com/items/?itemName=humao.rest-client)
  * Using (environment variables)[https://marketplace.visualstudio.com/items/?itemName=humao.rest-client#environment-variables]


## Data source
Home Assistant history REST API has a restriction of 10 days of data:
https://community.home-assistant.io/t/can-i-get-long-term-statistics-from-the-rest-api/761444/2


## Troubleshooting
Common issues and their solutions.

## License
This project is licensed under the MIT License.

## Acknowledgments
Special thanks to the contributors and libraries that made this project possible.