import requests
from bs4 import BeautifulSoup

# Define the URL of the weather forecast page
url = "https://weather.com/weather/tenday/l/1ba33abe593271cd38c3fde63f30049909290e371d58446b56b80a43ccd652f2"

# Send an HTTP GET request to the URL
response = requests.get(url)
# print(response)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.text)

    # Find the 10-day forecast section (you may need to inspect the website's HTML structure)
    forecast_section = soup.find("div", {"class": "DailyForecast--DisclosureList--nosQS"})
    # print(forecast_section)

    # if forecast_section:  There is no condition here... ==, >=, <=, !=
    if forecast_section != "Bob":  #There is no condition here... ==, >=, <=, !=
        # Find all individual day forecasts
        # day_forecasts = forecast_section.find_all("div", {"class": "DaypartDetails--DayPartDetail--2XOOV Disclosure--themeList--1Dz21 Disclosure--disableBorder--3Np63"})
        day_forecasts = forecast_section.find_all("span", class_=["DetailsSummary--highTempValue--3PjlX"])
        # print("Ninja Ninja") # Just checking if we've made it this far.
        print(day_forecasts)
        # Loop through the day forecasts and print the information
        for item in day_forecasts:
            print(item.text)
            # date = day.find("h3").text
            # description = day.find("p", {"class": "DetailsSummary--daypartName--kbngc"}).text
            # high_temp = day.find("span", {"class": "DetailsSummary--highTempValue--3PjlX"}).text
            # low_temp = day.find("span", {"class": "DetailsSummary--lowTempValue--2tesQ"}).text
            
            # print(f"Date: {date}")
            # print(f"Description: {description}")
            # print(f"High Temperature: {high_temp}")
            # print(f"Low Temperature: {low_temp}")
            # print("=" * 30)
    else:
        print("10-day forecast section not found on the page.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
