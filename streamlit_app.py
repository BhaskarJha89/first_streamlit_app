import streamlit as st
import pandas as pd
st.title('Ankita Sajal Cutie hai')
st.title('Ankita Sajal New Healthy Breakfast')
st.header('Breakfast Favorites')
st.text('🥣 Omega 3 and Blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avocado Toast')
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
st.dataframe(fruits_to_show)
st.header("Fruityvice Fruit Advice!")
fruit_choice = st.text_input('What fruit would you like information about?')
st.write('The user entered ', fruit_choice)
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi" )
#st.text(fruityvice_response.json())
# Take the Json version of response and normalize it
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# Output it the screen as a Table
st.dataframe(fruityvice_normalized)
#import snowflake.connector
#my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_data_row = my_cur.fetchone()
#st.text("Hello from Snowflake:")
#st.text(my_data_row)

