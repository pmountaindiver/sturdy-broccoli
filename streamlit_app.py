#!/usr/bin/env python
# coding: utf-8

# 
import streamlit as st
import pandas as pd
import base64
def create_onedrive_directdownload (onedrive_link):
    data_bytes64 = base64.b64encode(bytes(onedrive_link, 'utf-8'))
    data_bytes64_String = data_bytes64.decode('utf-8').replace('/','_').replace('+','-').rstrip("=")
    resultUrl = f"https://api.onedrive.com/v1.0/shares/u!{data_bytes64_String}/root/content"
    return resultUrl
#fn = r"C:/Users/peh/OneDrive/1 Finance/2022 Finanz Analyse/Python/Data/Reference/entries.xlsx"
onedrive_link=https://1drv.ms/x/s!AoEzYwQs3f9mkIQBeQNATkGFw3xcgw?e=7rbGfn
     
#x = pd.read_excel(create_onedrive_directdownload (onedrive_link))
st.write('Hello world!')
st.write(create_onedrive_directdownload (onedrive_link))

import streamlit as st

st.header('Ciao Bello')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')
# In[ ]:




