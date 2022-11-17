import streamlit
import requests
import pandas as pd
import snowflake.connector

from urllib.error import URLError

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
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
   else: 
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)
   #endif
except URLError as e:
  streamlit.error()

# don't run anything past here while we troubleshoot
streamlit.stop()

# snowflake area
my_cnx = snowflake.connector.connect(**streamlit.secrets['snowflake'])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()

streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

add_my_fruit = streamlit.text_input('What fruit would you like to add?', 'jackfruit')
streamlit.write('Thanks for adding ', add_my_fruit)

# this will not work correctly, but just go with it for now
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
