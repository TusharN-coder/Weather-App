import requests
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("WHATHER_API_KEY")

# to five the page title:
st.set_page_config(
    page_title="Weather App",
    page_icon="⛅"                             
)

st.title(""🌧️🌧️ Weather App 🌧️🌧️"")
st.write("Enter the city name and click the button to fetch the weather data")

city = st.text_input("Enter the city Name")

API_URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

if st.button("Fetch Weather Data"):                          # this return boolean value
    response = requests.get(API_URL)  
    if response.status_code == 200:                          # checking status code of the API data if 200 its work successfully if 404 then its unsuccessful.
        st.success("Weather data Featched successfully!")
        data = response.json()                        # fetcing the data into the varibale

        name = data["name"]
        country = data["sys"]["country"]

        temperature = data["main"]["temp"]  
        speed = data["wind"]["speed"]
        weather = data["weather"][0]["main"]
        humidity = data["main"]["humidity"]

        # Displaying City and Country name
        st.subheader(f"{name}, {country}")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Temperature", f"🌡️{temperature}°C")
        col2.metric("Wind_Speed", f"💨{speed} m/s")
        col3.metric("Weather", f"⛅{weather}")
        col4.metric("Humidity", f"💧{humidity}%")
    else: 
        st.error("Please enter a valid city Name")
