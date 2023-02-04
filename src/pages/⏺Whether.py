import streamlit as st
import requests
import matplotlib.pyplot as plt
import requests
import json
import pandas as pd
import pprint

st.set_page_config(page_title='Whether', page_icon=None, layout='wide')

cities = {
    "New York": {
        "latitude": 40.71,
        "longitude": -74.01
    },
    "Berlin": {
        "latitude": 52.52,
        "longitude": 13.41
    }
}

st_city = st.selectbox(
    'City',
    ('New York', 'Berlin'))

@st.cache(ttl=30)
def get_data(city):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={cities[city]['latitude']}&longitude={cities[city]['longitude']}&hourly=temperature_2m"
    res = requests.get(url)
    res = json.loads(res.text)
    return res['hourly']

def plot(data):
    df = pd.DataFrame.from_dict(data)
    st.line_chart(df, x='time', y='temperature_2m')

if st.button('Plot'):
    city = st_city
    data = get_data(city)
    plot(data)