import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import requests
import json

"""
# Welcome :heart:

This is an effort to document, explore my different areas of interests. Visualize to showcase my point of view.

-- Thanks to Streamlit for building the platform. --
"""

# US census bureau API Key
apiKey = '49151930da411856c561cc751ee2945a6a5f249a'

country = 'IN'
st.write(f'{country}')

year = st.text_input('Years limit', '2100')
st.write(f'Projections for year {year}')

# perform check box selection for males, females, or both
# 0 - total, 1 - male, 2 - female

age =  st.text_input('Age Limit', '100')
st.write(f'Age window from 0 to {age}')

if st.button('Get Population Projections'):
    response = requests.get(f'https://api.census.gov/data/timeseries/idb/1year?get=NAME,GENC,POP&YR=2023:{year}&AGE=0:{age}&SEX=0&for=genc+standard+countries+and+areas:{country}&key={apiKey}')
    # response.raise_for_status()
    # ['NAME', 'GENC', 'POP', 'YR', 'AGE', 'SEX', 'genc standard countries and areas']
    jsonData = json.loads(response.text)
    df = pd.DataFrame(jsonData[1:])
    st.dataframe(df)

    st.altair_chart(alt.Chart(df).mark_bar().encode(
    x = alt.X("4:O").sort(),
    y = "2:Q",
).properties(width=1000)
)

    # st.altair_chart((line).properties(
    # title= f"Population of {country} from 2003 to {years} in total",
    # width=500,
    # height=300))


else: 
    st.write(f'Things to check out: Population Projections for {country}')




