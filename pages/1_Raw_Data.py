import streamlit as st
import pandas as pd

st.write("# Best Bakery Demo :cupcake:")
st.write("### Raw Data")
df = pd.read_csv("./data/demo_data.csv")
st.write(df)