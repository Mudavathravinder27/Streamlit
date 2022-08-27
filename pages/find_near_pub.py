import streamlit as st
import numpy as np
import pandas as pd
import pydeck as pdk

df1= pd.read_csv('data/pub.csv')

# Python code for the above approach
 
# Calculate the Euclidean distance
# between two points
def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** ( 1 / 2)
 
# Function to calculate K closest points
def kClosest(points, target, K):
    pts = []
    n = len(points)
    d = []
 
    for i in range(n):
        d.append({
            "first": distance(points[i][0], points[i][1], target[0], target[1]),
            "second": i
        })
    
    
     
    d = sorted(d, key=lambda l:l["first"])
    
    for i in range(K):
        pt = []
        pt.append(points[d[i]["second"]][0])
        pt.append(points[d[i]["second"]][1])
        pts.append(pt)
   
# Calling DataFrame constructor on list
    df_nearest_loc = pd.DataFrame(pts,columns=['latitude','longitude'])
    st.header('Lets have Drink:wine_glass: and enjoy the music , If you cannot be happy atleast you can be drunk :wine_glass::wine_glass::wine_glass:')

    st.markdown('**Here are Nearest five Pubs based on user enter  Latitude and longitude**')
    st.map(df_nearest_loc)
    
# Driver code
df_lat_log=df1[['latitude','longitude']]
points = df_lat_log.values.tolist()

lat = st.sidebar.number_input('Your Latitude',format="%.5f")
log = st.sidebar.number_input('Your Longitude',format="%.6f",key=int)

target = [lat,log]
K = 5

kClosest(points, target, K)