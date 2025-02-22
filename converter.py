import streamlit as st

conversion_factors = {
  'distance':{'mm':1,
              'cm':0.1,
              'm':0.01},
  'weight':None,
  'time':None,
}

  category = st.radio("select category",options=conversion_factor.keys())
