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

def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()
  
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute(f"insert into fruit_load_list values ('{new_fruit}')")
    return "Thanks for adding "+ new_fruit

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


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("The fruid load list contains")
if streamlit.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  my_cnx.close()
  streamlit.dataframe(my_data_row)

#streamlit.stop()
add_my_fruit = streamlit.text_input('What fruit would you like to add?','Jackfruit')
if streamlit.button('Add a fruit to the List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  insert_row = insert_row_snowflake(add_my_fruit)
  my_cnx.close()
  streamlit.text(insert_row)

#my_cur.execute("insert into fruit_load_list values ('from streamlit')")
