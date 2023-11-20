import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

df = pd.read_csv('taylor_swift_songs.csv')
df = df.drop(df.columns[7], axis=1)

album_choice = df['album_name'].unique()
select_album = st.selectbox('Select Album:', album_choice)

df_filtered = df[df['album_name']== select_album]

(min_date,max_date)=int( df['album_release'].min(), df['album_release'].max())
st.slider("Choose Release Year")

st.table(df)