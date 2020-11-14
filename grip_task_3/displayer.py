import streamlit as st
import altair as alt
import plotly.graph_objects as go
import numpy as np
import plotly.express as px

def show_quantities(state,city_name,region,category,subcategory,data):
    #metric_selector=st.sidebar.multiselect("Metrics",("Plot Bars","line charts","scatter plots"))
    subset_city=data[data['City']==city_name]
    subset_city_state=subset_city[subset_city['State']==state]
    subset_city_state_region=subset_city_state[subset_city_state['Region']==region]

    data1=subset_city_state_region
    sales_pref_category=data1[data1['Category']==category]['Sales']
    pref_subcategory=data1[data1['Category']==category]['Sub-Category'].unique()


    # the total number of sales of subcategory in preferred category
    



    #sales per sub-category of the category 
    st.subheader("Sales money Earned ")
    subset=data1[data1['Category']==category]   
    sub_array=[]
    for i in subset['Sub-Category'].unique():
        sub_array.append(subset[subset['Sub-Category']==i]['Sales'].sum())
    fig2=px.bar(
        subset,
        x=subset['Sub-Category'].unique(),
        y=sub_array,
         labels={
        "x": "Sub Categories",
        "y": "Sales"
    }
    )
   
    st.plotly_chart(fig2)

    #sales per sub-category of the category chosen 
    st.subheader("Percentage of Sub Category Sales")
    fig3=px.pie(subset,
     names=subset['Sub-Category'].unique(),
        values=sub_array
    )
    st.plotly_chart(fig3)


     # the total number of quantities of subcategory in preferred category
    st.subheader("Quanitity of sales")
    sub_array1=[]
    for i in subset['Sub-Category'].unique():
        sub_array1.append(subset[subset['Sub-Category']==i]['Quantity'].sum())
    fig4=px.bar(
        subset,
        x=subset['Sub-Category'].unique(),
        y=sub_array1,
        labels={
                     "x": "Sub Category",
                     "y": "Quantity Sold",
                 },
    
        
    )
    st.plotly_chart(fig4)

     # the total number of quantities of subcategory in preferred category with sales
    sub_array2=[]
    for i in subset['Sub-Category'].unique():
        sub_array2.append(subset[subset['Sub-Category']==i]['Sales'].sum())
    fig5=px.scatter(
        subset,
        x=subset['Sub-Category'].unique(),
        y=sub_array1,
        size=sub_array2,
         labels={
        "x": "Sub Categories",
        "y": "Quantity",
        "size": "Sales"
    }
    )
    st.plotly_chart(fig5)

    st.subheader("Profits Earned")
    sub_array3=[]
    for i in subset['Sub-Category'].unique():
        sub_array3.append(subset[subset['Sub-Category']==i]['Profit'].sum())
    fig6=px.bar(
        subset,
        x=subset['Sub-Category'].unique(),
        y=sub_array3,
        barmode='group',
         labels={
        "x": "Sub Categories",
        "y": "Profits"
    }
    )
    st.plotly_chart(fig6)

    st.subheader("Percentage Profits Earned")
    sub_array3=[]
    for i in subset['Sub-Category'].unique():
        sub_array3.append(subset[subset['Sub-Category']==i]['Profit'].sum())
    fig7=px.pie(
        subset,
        names=subset['Sub-Category'].unique(),
        values=sub_array3
    )
    st.plotly_chart(fig7)

    
    

#st.plotly_chart(plot)


