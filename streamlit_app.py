import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import requests
import json

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

# num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
# num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

# indices = np.linspace(0, 1, num_points)
# theta = 2 * np.pi * num_turns * indices
# radius = indices

# x = radius * np.cos(theta)
# y = radius * np.sin(theta)

# df = pd.DataFrame({
#     "x": x,
#     "y": y,
#     "idx": indices,
#     "rand": np.random.randn(num_points),
# })

# st.altair_chart(alt.Chart(df, height=700, width=700)
#     .mark_point(filled=True)
#     .encode(
#         x=alt.X("x", axis=None),
#         y=alt.Y("y", axis=None),
#         color=alt.Color("idx", legend=None, scale=alt.Scale()),
#         size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
#     ))

apiKey = '49151930da411856c561cc751ee2945a6a5f249a'

country = 'IN'
st.write(f'{country}')

years = st.text_input('Years limit', '2100')
st.write(f'Projections from 2023 to {years}')

# perform check box selection for males, females, or both
# 0 - total, 1 - male, 2 - female

age =  st.text_input('Age Limit', '100')
st.write(f'Age window from 0 to {age}')

if st.button('Get Population Projections'):
    response = requests.get(f'https://api.census.gov/data/timeseries/idb/1year?get=NAME,GENC,POP&YR=2023:{years}&AGE=0:{age}&SEX=0&for=genc+standard+countries+and+areas:{country}&key={apiKey}')
    # response.raise_for_status()
    jsonData = json.loads(response.text)
    df = pd.DataFrame(jsonData)
    st.dataframe(df)

    line = alt.Chart(df).mark_line(color="#333").encode(
    alt.X("YR:T").axis(format="%Y").title("Year"),
    alt.Y("POP:Q").title("Population"),)

    st.altair_chart((line).properties(
    title= f"Population of {country} from 2003 to {years} in total",
    width=500,
    height=300))

    

else: 
    st.write(f'Things to check out: Population Projections for {country}')




