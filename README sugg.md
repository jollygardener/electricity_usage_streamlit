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
3. Create a virtual environment
4. Activate the virtual environment
5. Install the required dependencies

    ```bash
    git clone https://github.com/your-repo/electricity_usage_streamlit.git
    cd electricity_usage_streamlit
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

## Configuration
To configure the app to connect to Home Assistant, you need to set up the following in the `config.yaml` file:
- API keys
- API endpoints
- Other necessary configuration parameters

## Development
For developers looking to contribute, please follow these steps:
- Set up a virtual environment as described in the installation section.
- Run tests to ensure everything is functioning correctly.

## Troubleshooting
If you encounter common issues, refer to the troubleshooting section for solutions.

## License
This project is licensed under the MIT License.

## Acknowledgments
Special thanks to the contributors and libraries that made this project possible.