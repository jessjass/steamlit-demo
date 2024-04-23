import streamlit as st
import pandas as pd
from data_processing import df_for_sale, df_sold

# Set Wide Mode
st.set_page_config(layout="wide")

st.write("# Real Estate Comp :house:")
st.write("**Note: Analysis is done by Le Business Boutique. The data for this comp was collected using the Zillow API in April 2024.")
st.write("")

st.write(df_for_sale)
st.write(df_sold)