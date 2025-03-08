import pandas as pd
import streamlit as st
data = pd.read_excel('./pages/source.xlsx')
unique_category = data['category'].unique()
unique_storename = data['store'].unique()
minimum_price = data['price'].min()
maximum_price = data['price'].max()

selected_category = st.multiselect("select category",options=unique_category)
selected_store = st.multiselect("select store",options=unique_storename)
price_point = st.slider("Price",min_value=minimum_price,max_value=maximum_price,value=maximum_price)

criteria1 = data['category'].isin(selected_category) 
criteria2 = data['store'].isin(selected_store)
criteria3 = data['price'] <= price_point

join_criteria =  (criteria1) & (criteria2) & (criteria3)



with st.container(border=True):
  data = data[join_criteria]
  data_count = len(data)
  
  for i in range(data_count):
    product_picture = data.iloc[i]['picture']
    st.image(product_picture,width = 240)
    if st.button("buy now!",key=str(i)):
      st.write("Thank you for buying our product! It will arrive shortly.")

  
  st.dataframe(data,use_container_width=True)
