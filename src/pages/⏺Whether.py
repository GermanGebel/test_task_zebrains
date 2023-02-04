import streamlit as st
import requests
import matplotlib.pyplot as plt
import requests
import json
import pandas as pd

st.set_page_config(page_title='Whether', page_icon=None, layout='wide')

# to do cache
res = requests.get("https://api.open-meteo.com/v1/forecast?latitude=40.71&longitude=-74.01&hourly=temperature_2m")
res = json.loads(res.text)

# to do нарисовать правильно график
df = pd.DataFrame.from_dict(res['hourly'])
st.line_chart(df, x='time', y='temperature_2m')