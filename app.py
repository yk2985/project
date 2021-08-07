import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
@st.cache
def load_data():
    df = pd.read_csv('data/data.csv')
    return df

df = load_data()
st.title("Evaluation of Every Mobile  strategy game on appstore")
st.write(df)
options = [
            'Introduction',
            'About',
            'View Raw Data',
            'Analysis',
            'Analysis - User Rating',
            'Analysis - Analysis Average Rating',
            'Analysis - price',
            'Analysis - In-App purchases',
            'Analysis - languages',
            'Analysis - size',
            'Analysis - genres',
            'Analysis - original release dates',
            'Analysis - current release dates',
            'Conclusion',
        ]
menu = st.sidebar.radio("Select an Option", options)

if menu == options[0]:
	st.write(0)
if menu == options[1]:
	st.write(0)
if menu == options[2]:
	st.write(0)
if menu == options[3]:
	st.write(0)
if menu == options[4]:
	st.write(0)
if menu == options[5]:
	st.write(0)
if menu == options[6]:
	st.write(0)
if menu == options[7]:
	st.write(0)
if menu == options[8]:
	st.write(0)

``