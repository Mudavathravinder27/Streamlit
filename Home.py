import streamlit as st
import pandas as pd
import numpy as np


st.title('welcome to Home')

df1 = pd.read_csv(r'C:\Users\M RAVI\OneDrive\Desktop\streamlit\project\data\pub.csv')

basic = st.selectbox('Basic information',('shape_of_data','head','tail','info','check_null_values','check_duplicate'))

if basic=='sape_of_data':
    st.text('Number of rows: {}'.format(df1.shape[0]))
    st.text('Number of columns: {}'.format(df1.shape[1]))
elif basic =="head":
    st.dataframe(df1.head())
elif basic =='tail':
    st.dataframe(df1.tail())
elif basic =='info':
    st.text(df1.info())
elif basic =='check_null_values':
    st.text(df1.isnull().sum())
stats= st.radio('statistics',('describe'))

if stats=='describe':
  
    st.markdown('**We can see that there are no null values in our dataset**')
    st.text(df1.isnull().sum())

    st.text('')
st.text('')

st.subheader('Find the Statistics information of the pub dataset')

stat = st.button('Describe')

if stat==True:
    st.dataframe(df1.describe())
else:
    st.text('')