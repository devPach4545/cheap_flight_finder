import requests
from flight_search import FlightSearch
import os

sheety_endpoint = os.environ.get("SHEETY_ENDPOINT")

flight_search = FlightSearch()

class DataManager:
    def __init__(self):
        self.api_url = sheety_endpoint

    def get_flight_deals(self):
        # Function to fetch flight deals from Sheety API
        response = requests.get(self.api_url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch data. Status code: {response.status_code}")

    def put_iatacodes_in_sheet(self):
        # Function to update IATA codes in the sheet
        flight_deals = self.get_flight_deals()
        sheet_data = flight_deals['prices']
        
        for each_iatacode in sheet_data:
            if each_iatacode['iataCode'] == '':
                each_iatacode['iataCode'] = flight_search.get_code(city_name=each_iatacode['city'])
        
        for each_city in sheet_data:
            json_data = {
                "price": {
                    "iataCode": each_city["iataCode"],
                }
            }
            response = requests.put(url=f"{sheety_endpoint}/{each_city['id']}", json=json_data)  
        
    def get_price_for_each(self):
        # Function to get flight prices and send email alerts if prices are lower
        flight_deals = self.get_flight_deals()
        sheet_data = flight_deals['prices']
        from_code_input = input("Enter the departure airport code (e.g., ONT): ")

        for each_city in sheet_data:
            all_price = flight_search.get_price(from_code=from_code_input,  to_code=each_city['iataCode'], from_date="09/24/2023", to_date="04/24/2024")
            
            if all_price == "no flight":
                print("No flights available.")
            else:
                # Compare the prices
                if int(all_price) < int(each_city['lowestPrice']):
                    subject = "Flight Price Alert"
                    body = f"Price Alert: Flight from {from_code_input} to {each_city['iataCode']} is now available at a lower price than {each_city['lowestPrice']} USD at {all_price} USD"
                    print(subject, body)
                    # Send email alert
                    FlightSearch.send_email(subject, body)

