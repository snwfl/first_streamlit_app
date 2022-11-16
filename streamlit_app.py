import streamlit
import pandas as pd

# streamlit demo
streamlit.title('My Parents New Healty Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smootie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# pandas demo
df = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
df = df.set_index('Fruit')

# lets'put a pick list here so they can pick the fuit they want to include
streamlit.multiselect("Pick some fruits:", list(df.index), ['Avocado', 'Strawberries'])

# display the table on the page
streamlit.dataframe(df)
