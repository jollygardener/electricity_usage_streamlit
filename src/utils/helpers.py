def format_data(data):
    # Function to format data for display
    formatted_data = {}
    for key, value in data.items():
        formatted_data[key] = f"{value:.2f}"  # Format numbers to two decimal places
    return formatted_data


def calculate_usage(previous_reading, current_reading):
    # Function to calculate electricity usage
    return current_reading - previous_reading


def validate_api_response(response):
    # Function to validate API response
    if response.status_code != 200:
        raise ValueError(f"API request failed with status code: {response.status_code}")
    return response.json()
