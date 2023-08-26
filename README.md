
# Flight Price Tracker

The Flight Price Tracker is a Python application that helps users track flight prices and receive email alerts when prices drop below a certain threshold. It utilizes two main components: the Sheety API for storing and retrieving flight deal data and the Kiwi API for fetching flight prices and IATA codes.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Components](#components)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you can use this Flight Price Tracker, you'll need the following:

1. Python 3.x installed on your system.
2. API keys for the Sheety API and Kiwi API.
3. A Gmail account to send email alerts.

## Installation

1. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/your-username/flight-price-tracker.git
   ```

2. Navigate to the project directory.

   ```bash
   cd flight-price-tracker
   ```

3. Install the required Python libraries using pip.

   ```bash
   pip install requests
   ```

## Usage

The Flight Price Tracker has three main functionalities:

1. **Updating IATA Codes in the Sheet:** To ensure accurate tracking of flight deals, you can run the `put_iatacodes_in_sheet` method in the `DataManager` class. This method retrieves flight deals from the Sheety API and updates any missing IATA codes for cities using the Kiwi API.

   ```python
   data_manager = DataManager()
   data_manager.put_iatacodes_in_sheet()
   ```

2. **Getting Flight Prices and Sending Email Alerts:** You can fetch flight prices and receive email alerts for price drops. Run the `get_price_for_each` method in the `DataManager` class and provide the departure airport code when prompted.

   ```python
   data_manager = DataManager()
   data_manager.get_price_for_each()
   ```

3. **Sending Email Alerts:** The Flight Search class includes a `send_email` method that sends email alerts. Make sure to configure your Gmail account and set the required environment variables for this to work.

## Components

### `flight_search.py`

This module contains the `FlightSearch` class responsible for fetching flight prices and IATA codes, as well as sending email alerts.

- `send_email(subject, body)`: Sends email alerts with the specified subject and body.
- `get_code(city_name)`: Retrieves the IATA code for a given city name.
- `get_price(from_code, to_code, from_date, to_date)`: Fetches flight prices for a specified route and date range.

### `data_manager.py`

The `DataManager` class in this module handles interactions with the Sheety API and coordinates the flight price tracking process.

- `get_flight_deals()`: Fetches flight deals data from the Sheety API.
- `put_iatacodes_in_sheet()`: Updates missing IATA codes in the Sheety sheet.
- `get_price_for_each()`: Gets flight prices and sends email alerts for price drops.

## Configuration

To use the Flight Price Tracker effectively, you need to configure the following:

- **API Keys:** Obtain API keys for the Sheety API and Kiwi API and set them as environment variables.

- **Email Configuration:** Set up your Gmail account to send email alerts. Ensure you set the `SENDER_PASSWORD` environment variable to your Gmail account password.

## OUTPUT


## Contributing

Contributions to the Flight Price Tracker project are welcome! If you have any improvements, bug fixes, or new features to add, please follow the standard GitHub Fork-Pull Request workflow.



---
