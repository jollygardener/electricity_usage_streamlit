import streamlit as st
from src.components.layout import create_layout


def test_create_layout():
    layout = create_layout()
    assert layout is not None
    assert isinstance(
        layout, dict
    )  # Assuming layout returns a dictionary of components


def test_sidebar_elements():
    st.sidebar.selectbox("Select an option", ["Option 1", "Option 2"])
    selected_option = st.sidebar.session_state.get("selectbox")
    assert selected_option in ["Option 1", "Option 2"]
