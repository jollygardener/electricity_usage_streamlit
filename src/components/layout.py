import streamlit as st
from src.api.home_assistant_client import APIClient


def get_entity_options():
    """Entities are configured in the settings.yaml file and loaded into settings."""
    from src.config.settings import settings

    entity_options = {entity.display_name: entity.id for entity in settings.entities}
    return entity_options


def create_layout(api_client: APIClient):

    st.title("Electricity Generation Streamlit App")
    st.header("Welcome to the Solar Generation Monitor")

    st.sidebar.subheader("Settings")
    entity_options = get_entity_options()
    display_name = st.sidebar.selectbox("Entity:", entity_options.keys())
    entity_id = entity_options[display_name]
    view_selected = st.sidebar.selectbox(
        "Select a view:", ["Overview", "Graph", "Raw Data"]
    )

    st.subheader("24hr Electricity Generation")
    # Placeholder for displaying electricity usage data
    dt = st.date_input(
        "Select generation date:", value=None, min_value=None, max_value=None
    )
    data = api_client.get_history_data(
        dt.isoformat() if dt else None, entity_id=entity_id
    )
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
