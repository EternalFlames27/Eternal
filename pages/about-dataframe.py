import pandas as pd
import streamlit as st
data = pd.read_excel('./pages/source.xlsx')

criteria1 = data['category'] == 'food'
criteria2 = data['store'] == 5
criteria3 = data['price'] >= 12000
criteria4 = (data['price'] >= 12000) & (data['price'] <= 20000)
criteria5 = (criteria4) & (criteria2)

data[criteria5]


print(data[criteria5].sort_values('price',ascending=True))
st.dataframe(data)
