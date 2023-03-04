import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", r"D:\ds Internship 2023\webapp\images\diamondfactoring.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data","D:\ds Internship 2023\webapp\diamonds.csv")

st.title("Dashboard - Diamonds Data")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

species = st.selectbox("Select the Diamond_quality:", df['cut'].unique())

col1 = st.columns(1)

pie_chart=px.pie(df['cut'],title='Diamond cut', names='cut')

st.plotly_chart(pie_chart)




