#!/usr/bin/env python
# coding: utf-8

# 
import streamlit as st
import pandas as pd
df= pd.read_excel(r'C:\Users\peh\OneDrive\1 Finance\2023 Finanz Analyse\Python\Data\Reference\entries.xlsx')
st.write('Hello world!')
st.write(df)

import streamlit as st

st.header('Ciao Bello')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')
# In[ ]:




