import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.header("Data analysis of the Corona virus")
st.write("")

st.sidebar.header('Coronavirus disease (COVID-19)')
st.write("")
st.sidebar.image('/content/download.jpg')
st.write("")
st.write('')
st.write('')

st.sidebar.write("Coronavirus disease (COVID-19) is an infectious disease caused by the SARS-CoV-2 virus.Most people infected with the virus will experience mild to moderate respiratory illness and recover without requiring special treatment. However, some will become seriously ill and require medical attention. Older people and those with underlying medical conditions like cardiovascular disease, diabetes, chronic respiratory disease, or cancer are more likely to develop serious illness. Anyone can get sick with COVID-19 and become seriously ill or die at any age. The best way to prevent and slow down transmission is to be well informed about the disease and how the virus spreads. Protect yourself and others from infection by staying at least 1 metre apart from others, wearing a properly fitted mask, and washing your hands or using an alcohol-based rub frequently. Get vaccinated when it’s your turn and follow local guidance.The virus can spread from an infected person’s mouth or nose in small liquid particles when they cough, sneeze, speak, sing or breathe. These particles range from larger respiratory droplets to smaller aerosols.")

df = pd.read_csv("newdf.csv")

df.drop("Province/State", axis=1,inplace=True)
df.drop("country+province", axis=1,inplace=True)

df["min"].fillna(df["min"].median(),inplace=True)

# %% [code]
Q1=df['min'].quantile (0.25)
Q3=df['min'].quantile (0.75)
QIR=Q3-Q1
df=df[~((df["min"]<(Q1-1.5*QIR))| (df["min"]>(Q3+1.5*QIR)))]  

df["max"].fillna(df["max"].median(),inplace=True)

Q1=df['max'].quantile (0.25)
Q3=df['max'].quantile (0.75)
QIR=Q3-Q1
df=df[~((df["max"]<(Q1-1.5*QIR))| (df["max"]>(Q3+1.5*QIR)))]  



df.drop(columns="ah", axis=1,inplace=True )


df["rh"].fillna(df["rh"].median(),inplace=True)


Q1=df['rh'].quantile (0.25)
Q3=df['rh'].quantile (0.75)
QIR=Q3-Q1
df=df[~((df["rh"]<(Q1-1.5*QIR))| (df["rh"]>(Q3+1.5*QIR)))]  


df["slp"].fillna(df["slp"].mean(),inplace=True)


c1,c2=st.columns(2)
c1.metric("number of Fatalities:",df['Fatalities'].sum())
c2.metric("number of ConfirmedCases:",df['ConfirmedCases'].sum())

from datetime import datetime 
df["Date"]= pd.to_datetime(df["Date"])
df['Month']=df["Date"].dt.month
df["Day"]=df["Date"].dt.day

fig = px.scatter_geo(df, locations="Country/Region", locationmode='country names', color="Fatalities",
                     hover_name="Country/Region", size="ConfirmedCases",
                    projection="natural earth", title='COVID-19 Fatalities and Confirmed Cases by Country')
st.plotly_chart(fig)

st.write('')
st.write('')

scatter=px.scatter(df, x="ConfirmedCases", y = "Fatalities" ,color='Country/Region', template = 'plotly_dark',width = 1000, height = 900 , size='Day')
st.plotly_chart(scatter)












