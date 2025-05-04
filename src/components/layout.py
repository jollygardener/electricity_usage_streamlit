from streamlit import sidebar, title, header, subheader


def create_layout():
    title("Electricity Usage Streamlit App")
    header("Welcome to the Electricity Usage Monitor")

    sidebar.subheader("Settings")
    sidebar.selectbox("Select a view:", ["Overview", "Usage Statistics", "Settings"])

    subheader("Current Electricity Usage")
    # Placeholder for displaying electricity usage data
    # This will be populated with actual data later
    sidebar.text("Electricity usage data will be displayed here.")
