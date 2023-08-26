from data_manager import DataManager  # Import the DataManager class
from pprint import pprint

# Create a DataManager instance
data = DataManager()

# Call the get_price_for_each method to fetch flight prices and send alerts
data.get_price_for_each()
