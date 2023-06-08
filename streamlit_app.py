import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

fruit_list_df = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruit_list_df = fruit_list_df.set_index('Fruit')

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

def get_fruityvice_data():
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

streamlit.title("Snowflake project")
streamlit.header("Breakfast")
streamlit.text("🥣 Oatmeal")
streamlit.text("🥗 Smoothie")
streamlit.text("🐔 Egg")
streamlit.text("🥑🍞 Avocado toast")

streamlit.header("Special Menu")
fruit_selected = streamlit.multiselect("Pick some fruits:", list(fruit_list_df.index),['Avocado','Strawberries'])
streamlit.dataframe(fruit_list_df.loc[fruit_selected])

streamlit.header("Fruityvice advice")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
  else:
    fruityvice_data = get_fruityvice_data()
    streamlit.dataframe(fruityvice_data)
except URLError as e:
  streamlit.error()
  
streamlit.write('The user entered ', fruit_choice)

streamlit.stop()
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("The fruid load list contains")
streamlit.dataframe(my_data_row)

add_my_fruit = streamlit.text_input('What fruit would you like to add?','Jackfruit')
streamlit.write('Thanks for adding ', add_my_fruit)

#my_cur.execute("insert into fruit_load_list values ('from streamlit')")
