#!/usr/bin/env python
# coding: utf-8

# 
import streamlit as st
import pandas as pd
fn = r"C:/Users/peh/OneDrive/1 Finance/2022 Finanz Analyse/Python/Data/Reference/entries.xlsx"
Entries = pd.read_excel(fn)
st.write('Hello world!')
st.write(Entries)

import streamlit as st

st.header('Ciao Bello')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')
# In[ ]:




