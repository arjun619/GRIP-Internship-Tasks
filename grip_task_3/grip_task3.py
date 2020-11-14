import numpy as np
import pandas as pd
import streamlit as st
import plotly.offline as py
import pydeck as pdk 
import altair as alt
import displayer
import plotly.graph_objects as go

st.title("Super Store Analysis")
data=pd.read_csv("C:\\Users\\arjun\\Downloads\\SampleSuperstore.csv")
city_names=data['City']
data.drop(['Country'],axis=1,inplace=True)
states=data['State']
st.sidebar.title("Visualizer")

state=st.sidebar.selectbox('State',states.unique().tolist())
city_names=data[data['State']==state]['City'].unique()
city_name = st.sidebar.selectbox('City Name',city_names)

region=data[data['State']==state]['Region'].unique()
region=st.sidebar.selectbox('Select Region',region)

#st.sidebar.button("Add",key="mybutton")
category=st.sidebar.selectbox("Category",data['Category'].unique())
subcat=data[data["Category"]==category]['Sub-Category'].unique()
subcategory=st.sidebar.selectbox('SubCategory',subcat)
    

if st.sidebar.button("Add",key="mybutton"):
    displayer.show_quantities(state,city_name,region,category,subcategory,data)