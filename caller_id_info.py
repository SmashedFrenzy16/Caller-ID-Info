from requests import *
from bs4 import BeautifulSoup

api_key = "ENTER IN YOUR API KEY HERE"

phone_number = input("Enter in a phone number: ")

country_c = input("Enter in the country code for the number: ")

raw_data = get(f"http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}&country_code={country_c}&format=1")

print(BeautifulSoup(raw_data, "html.parser"))