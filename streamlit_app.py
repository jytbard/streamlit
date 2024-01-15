# streamlit_app.py

import streamlit as st

# Initialize connection.
conn = st.connection("snowflake")

# Perform query.
df = conn.query("select * from WATCHTOWER_STATIONS_TBL;", ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.ID} has a :{row.ORGANIZATIONUNITID}:")


#pja45566.east-us-2.azure
