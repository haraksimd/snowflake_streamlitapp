import streamlit
import pandas
import requests
import snowflake.connector

fruit_list_df = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruit_list_df = fruit_list_df.set_index('Fruit')

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")



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
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#streamlit.dataframe(fruityvice_normalized)
streamlit.text(fruityvice_normalized)

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
