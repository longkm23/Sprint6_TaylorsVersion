import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import plotly.figure_factory as ff

st.write("Hello from Streamlit")

df = pd.read_csv(r'C:\Users\kirst\OneDrive\Desktop\S6P_TV\taylor_swift_songs.csv')
df = df.drop(df.columns[7], axis=1)

st.header('Exploring Different Elements and Facts About Taylor Swift Songs and Albums', divider='blue')
st.text('Calling all TripleTen Taylor Swift fans: Use the different features of this application to learn more about your favorite Taylor Swift album')


album_choice = df['album_name'].unique()
select_album = st.selectbox('Select Album:', album_choice)

df_filtered = df[df['album_name'] == select_album]

# Convert date strings to years
df_filtered['album_release'] = pd.to_datetime(df_filtered['album_release']).dt.year

# Get the min and max release years
min_date, max_date = df_filtered['album_release'].min(), df_filtered['album_release'].max()

# Fixing error message that min and max were the same
if min_date == max_date:
    min_date -= 1
    max_date += 1

# Create a slider to choose the release year
selected_year = st.slider(
    "Choose Release Year",
    min_value=min_date,
    max_value=max_date,
    value=(min_date, max_date)
)

# Display scatterplot based on the checkbox state
check = st.checkbox("Show Scatterplot")
if check:
    # Assuming 'scatterplot' is a Plotly Express scatterplot
    scatterplot = px.scatter(df_filtered, x='album_release', y='album_name', title='Scatterplot')

    # Display the scatterplot
    st.plotly_chart(scatterplot)

# Display the filtered DataFrame in a table
st.title("Explore by Album")
st.table(df_filtered)
