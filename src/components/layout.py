import streamlit as st
from src.api.home_assistant_client import APIClient


def create_layout(api_client: APIClient):

    st.title("Electricity Generation Streamlit App")
    st.header("Welcome to the Solar Generation Monitor")

    st.sidebar.subheader("Settings")
    view_selected = st.sidebar.selectbox(
        "Select a view:", ["Overview", "Graph", "Raw Data"]
    )

    st.subheader("24hr Electricity Generation")
    # Placeholder for displaying electricity usage data
    dt = st.date_input(
        "Select generation date:", value=None, min_value=None, max_value=None
    )
    data = api_client.get_history_data(dt.isoformat() if dt else None)
    if not data.empty:
        match view_selected:
            case "Overview":
                st.write("Overview of electricity generation data.")
                st.write(data.describe())
            case "Graph":
                st.line_chart(data, x="datetime", y="value", use_container_width=True)
            case "Raw Data":
                st.dataframe(data)
    else:
        st.warning("No data available for the selected date.")
