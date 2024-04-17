import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import json
from data_processing import df_for_sale, df_sold

# Set Wide Mode
st.set_page_config(layout="wide")

st.write("# Real Estate Comp :house:")
st.write("**Note: Analysis is done by Le Business Boutique. The data for this comp was collected using the Zillow API in April 2024.")
st.write("")

## - [ ] Header with main listing stats

with open("./data/client_prop_demo_data.json") as f:
    client_prop = json.load(f)

st.markdown("<h4 style='font-size:16; color:#414572'>Client Property Details</h4>",
                unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

col1.markdown("<h6 style='font-size:16; color:#414572'>Address</h6>",
                unsafe_allow_html=True)
col1.markdown("<p style='font-size:16; color: #9898b4'>" + client_prop['address']['streetAddress'] + 
              ", " + client_prop['address']['city'] + 
              " " + client_prop['address']['state'] + 
              "</p>",
                unsafe_allow_html=True)

col2.markdown("<h6 style='font-size:16; color:#414572'>Zip Code</h6>",
                unsafe_allow_html=True)
col2.markdown("<p style='font-size:16; color: #9898b4'>" + client_prop['address']['zipcode'] + "</p>",
                unsafe_allow_html=True)

col3.markdown("<h6 style='font-size:16; color:#414572'>Property Type</h6>",
                unsafe_allow_html=True)
col3.markdown("<p style='font-size:16; color: #9898b4'>" + client_prop['homeType'] + "</p>",
                unsafe_allow_html=True)

col4.markdown("<h6 style='font-size:16; color:#414572'>Year Built</h6>",
                unsafe_allow_html=True)
col4.markdown("<p style='font-size:16; color: #9898b4'>" + str(client_prop['yearBuilt']) + "</p>",
                unsafe_allow_html=True)

col5, col6, col7, col8 = st.columns(4)

col5.markdown("<h6 style='font-size:16; color:#414572'>Living Area SQFT</h6>",
                unsafe_allow_html=True)
col5.markdown("<p style='font-size:16; color: #9898b4'>" + str(client_prop['livingArea']) + "</p>",
                unsafe_allow_html=True)

col6.markdown("<h6 style='font-size:16; color:#414572'>Beds</h6>",
                unsafe_allow_html=True)
col6.markdown("<p style='font-size:16; color: #9898b4'>" + str(client_prop['bedrooms']) + "</p>",
                unsafe_allow_html=True)

col7.markdown("<h6 style='font-size:16; color:#414572'>Baths</h6>",
                unsafe_allow_html=True)
col7.markdown("<p style='font-size:16; color: #9898b4'>" + str(client_prop['bathrooms']) + "</p>",
                unsafe_allow_html=True)

col8.markdown("<h6 style='font-size:16; color:#414572'>Rent Zestimate</h6>",
                unsafe_allow_html=True)
col8.markdown("<p style='font-size:16; color: #9898b4'> $" + str(client_prop['rentZestimate']) + "</p>",
                unsafe_allow_html=True)
st.write("")
st.write("")
st.markdown("<h4 style='font-size:16; color:#414572'>Analytics</h4>",
                unsafe_allow_html=True)

## - [ ] Map with address points

plot1, plot2 = st.columns(2)
## - [ ] Scatter plot, for sale,  x=sq, y=price

#plot1.write("##### Similar Properties For Sale, Sqft vs Price")

fig = plt.figure()
plt.scatter(df_for_sale['livingArea'], df_for_sale['price'])
plt.title("Sqft vs Price")
plt.xlabel("Sqft")
plt.ylabel("Price")
plot1.pyplot(fig)

## - [ ] H bar chart, sold, x=Days on Zillow, y=price

plot2.write("##### Days on Zillow vs Price")

fig = px.bar(df_sold, x="property.daysOnZillow", y="property.price", orientation='h')
plot2.write(fig)

## - [ ] Table, for sale - beds/bath, sqft, zip code, price
plot3, plot4 = st.columns(2)

plot3.write("##### Similar Properites Listed For Sale")
basic_for_sale = df_for_sale[['bedrooms', 'bathrooms', 'livingArea', 'address.zipcode', 'price']]
plot3.write(basic_for_sale)

## - [ ] Table, sold - beds/bath, sqft, zip code, price, days on Zillow

plot4.write("##### Similar Properites Sold")
basic_sold = df_sold[['property.bedrooms', 'property.bathrooms', 'property.livingAreaValue', 
                      'property.address.zipcode', 'property.price', 'property.daysOnZillow']]
plot4.write(basic_sold)

## - [ ] H bar chart, for sale, x=# properties, y=price
st.write("")
st.write("##### Number of Properties Sold by Price Range")

price_range = df_for_sale.groupby(pd.cut(df_for_sale['price'], [400000, 425000, 450000, 475000, 500000]))['price'].count()
price_range = price_range.to_frame()
price_range["range"] = ["$400000-$425000", "$425001-$450000", "$450001-$475000", "$475001-$500000"]

fig = px.bar(price_range, x="range", y="price", orientation='h')
st.write(fig)