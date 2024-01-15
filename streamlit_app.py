# streamlit_app.py

import streamlit as st

import numpy as np

import plotly.express as px

# Initialize connection.
conn = st.connection("snowflake")

# Perform query.
#df = conn.query("select * from WATCHTOWER_STATIONS_TBL;", ttl=600)

df = conn.query("select * from MERAKI_CLIENTS_TBL;", ttl=600)

# Print results.
#for row in df.itertuples():
  # st.write(f"{row.ID} has a :{row.ORGANIZATIONUNITID}:")

st.subheader("MERAKI CLIENTS VIZ")

fig = px.scatter(
    df,
    x="CONNECTEDBY",
    y="LASTSEEN",
    color="STATUS",
    color_continuous_scale="reds",
)

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    st.plotly_chart(fig, theme=None, use_container_width=True)
