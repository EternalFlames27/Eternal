import pandas as pd
import streamlit as st
data = pd.read_excel('./pages/source.xlsx')
unique_category = data['category'].unique()
unique_storename = data['store'].unique()

selected_category = st.multiselect("select category",options=unique_category)
selected_store = st.multiselect("select store",options=unique_store)

criteria1 = data['category'].isin(selected_category) 
criteria2 = data['store'].isin(selected_store)
join_criteria = (criteria1) & (criteria2)
criteria3 = data['price'] >= 12000
criteria4 = (data['price'] >= 12000) & (data['price'] <= 20000)
criteria5 = (criteria4) & (criteria2)


data[criteria5]

data = data[join_criteria]

print(data[criteria5].sort_values('price',ascending=True))
st.dataframe(data)
