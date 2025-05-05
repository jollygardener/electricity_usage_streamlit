import streamlit as st
from src.api.home_assistant_client import APIClient
from src.components.layout import create_layout


def main():

    # Initialize API client
    api_client = APIClient()

    # Create layout
    create_layout(api_client)


if __name__ == "__main__":
    main()
