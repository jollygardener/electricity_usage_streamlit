import streamlit as st
from src.api.home_assistant_client import APIClient
from src.components.layout import create_layout
from src.config.settings import settings


def main():
    st.title("Electricity Usage Streamlit App")

    # Initialize API client
    api_client = APIClient(bearer_token=settings.BEARER_TOKEN)

    # Create layout
    create_layout(api_client)


if __name__ == "__main__":
    main()
