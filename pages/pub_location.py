import streamlit as st
import pandas as pd
import numpy as np

df1=pd.read_csv('data/pub.csv')
st.map(df1)


st.subheader('select a Local Authority')


local = df1.local_authority.unique()
option = st.selectbox('',local)


'You Selected : ' ,option

btn_clk = st.button('Find now')
if btn_clk==True:
    res = df1[df1['local_authority']==option]
    res=res[['latitude','longitude']]
    st.map(res)
    st.markdown('_Its displaying all the pubs in the area that you selected_')                                              


