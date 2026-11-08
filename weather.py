import streamlit as st
import requests

st.title("Live Weather App 🌦️")
st.write("Real Data from OpenWeather API")


API_KEY = "PASTE_YOUR_NEW_KEY_HERE"  # Replace with your OpenWeather API k

city = st.text_input("Enter City Name:", "Hyderabad")

if st.button("Get Weather"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        feels = data['main']['feels_like']
        humidity = data['main']['humidity']
        desc = data['weather'][0]['description']
        
        st.success(f"Weather in {city}")
        st.metric("Temperature", f"{temp}°C")
        st.metric("Feels Like", f"{feels}°C")
        st.write(f"**Condition:** {desc}")
        st.write(f"**Humidity:** {humidity}%")
    else:
        st.error("City not found or Key inka active kaledu. 10 mins wait chesi malli try chey!")