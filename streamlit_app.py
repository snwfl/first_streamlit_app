import streamlit
import requests
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
my_fuit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fuit_list = my_fuit_list.set_index('Fruit')

# lets'put a pick list here so they can pick the fuit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fuit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fuit_list.loc[fruits_selected]

# display the table on the page
streamlit.dataframe(fruits_to_show)


# New section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
streamlit.write('The user entered', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# take the json version of the response and normalize it
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())

# output it the screen as a table
streamlit.dataframe(fruityvice_normalized)


