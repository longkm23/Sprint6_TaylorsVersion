import streamlit as st
import pandas as pd


data = pd.read_csv('taylor_swift_songs.csv')

st.write(data.head())