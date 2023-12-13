import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import plotly.figure_factory as ff

# Open up streamlit and call up the proper app.py
st.write("Hello from Streamlit")
#  To run streamlit local host 8502: streamlit run C:\Users\kirst\OneDrive\Desktop\S6P_TV\app.py

df = pd.read_csv(r'C:\Users\kirst\OneDrive\Desktop\S6P_TV\taylor_swift_songs.csv')
df = df.drop(df.columns[7], axis=1)

st.header('Exploring Different Elements and Facts About Taylor Swift Songs and Albums', divider='blue')
st.text('Calling all TripleTen Taylor Swift fans: Use the different features of this application to learn more about your favorite Taylor Swift album')

 # Creating a dropdown box so users can select their favorite Taylor Swift album to explore
album_choice = df['album_name'].unique()
select_album = st.selectbox('Select Album:', album_choice)

# Creating a filter for the dropdown box so users can select their favorite album
df_filtered = df[df['album_name'] == select_album]

# Display the filtered DataFrame in a table. The information in the table should be specific to the album that was selected in the dropdown box.
st.title("A Deep Dive Into Your Favorite Album")
st.table(df_filtered)


# Convert date strings to years
df['album_release'] = pd.to_datetime(df['album_release']).dt.year

# Get the min and max release years
min_date, max_date = df['album_release'].min(), df['album_release'].max()

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

# Create a histogram showing trends in the danceability of Taylor Swift's releases
histogram_all = px.histogram(df, x='danceability', title='Danceability Over Time', color_discrete_sequence=['#FF5733'] )
# Display histogram
st.plotly_chart(histogram_all)

# Display scatterplot based on the checkbox state
check = st.checkbox("Show Scatterplot")
if check:
    # Assuming 'scatterplot' is a Plotly Express scatterplot
    scatterplot = px.scatter(df, x='album_release', y='album_name', title='Scatterplot of Album Releases Over the Years', color_discrete_sequence=['#33B5FF'])

    # Display the scatterplot
    st.plotly_chart(scatterplot)

