import streamlit as st
import pandas as pd
st.title("anything store")
st.subheader("we literally have anything!")
df = pd.read_excel('source.xlsx')

with st.container(border=True):
    selected_category = st.selectbox("Choose what category you're looking for",options=df['category'].unique())
    selected_name = st.selectbox("Choose what item you're looking for",options=df['name'].unique())
    selected_store = st.selectbox("Choose what store you're looking for",options=df['store'].unique())
#    selected_price = st.slider("pick a price range", min_value=0, max_value=368000000000,value=0) 

#df = df[df['category'] == selected_category]
#df = df[df['price'] == selected_price]
#df = df[df['name'] == selected_name]
#df = df[df['store'] == selected_store]

st.dataframe(df)

