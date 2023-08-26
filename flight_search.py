import requests
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# Access the environment variables
kiwi_endpoint_location = os.environ.get("KIWI_ENDPOINT_LOCATION")
kiwi_endpoint_search = os.environ.get("KIWI_ENDPOINT_SEARCH")

class FlightSearch:
    def send_email(subject, body):
        # Email configuration
        sender_email = "quantumdevwave@gmail.com"
        sender_password = os.environ.get("SENDER_PASSWORD")
        recipient_email = "dhaivatpachchigar@gmail.com"

        # Create a MIMEText object for the email content
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = subject

        # Attach the email body to the message
        message.attach(MIMEText(body, "plain"))

        # Establish a secure SMTP connection
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            text = message.as_string()
            server.sendmail(sender_email, recipient_email, text)
            server.quit()

    def get_code(self, city_name):
        # Function to get the IATA code for a city
        headers = {
            "apikey": os.environ.get("KIWI_API_KEY")
        }
        parameters = {
            "term": city_name
        }
        response = requests.get(headers=headers, url=kiwi_endpoint_location, params=parameters)
        code = response.json()
        code = code['locations'][0]['code']
        return code

    def get_price(self, from_code, to_code, from_date, to_date):
        # Function to get flight prices
        from_date = datetime.strptime(from_date, "%m/%d/%Y")
        to_date = datetime.strptime(to_date, "%m/%d/%Y")
        headers = {
            "apikey": os.environ.get("KIWI_API_KEY")
        }
        flight_data = {
            "fly_from": from_code,
            "fly_to": to_code,
            "date_from": from_date.strftime("%d/%m/%Y"),
            "date_to": to_date.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }
        response = requests.get(headers=headers, url=kiwi_endpoint_search, params=flight_data)
        
        priced = response.json()['data']
        if priced == []:
            return "no flight"
        else:
            priced = response.json()['data'][0]
            price = priced['price']
            return price
