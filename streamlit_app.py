# streamlit_app.py

import streamlit as st

import numpy as np

import plotly.figure_factory as ff

# Initialize connection.
conn = st.connection("snowflake")

# Perform query.
df = conn.query("select * from WATCHTOWER_STATIONS_TBL;", ttl=600)

print(df)

