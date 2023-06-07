import streamlit
import pandas

fruit_list_df = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruit_list_df = fruit_list_df.set_index('Fruit')


streamlit.title("Snowflake project")
streamlit.header("Breakfast")
streamlit.text("🥣 Oatmeal")
streamlit.text("🥗 Smoothie")
streamlit.text("🐔 Egg")
streamlit.text("🥑🍞 Avocado toast")

streamlit.header("Special Menu")
fruit_selected = streamlit.multiselect("Pick some fruits:", list(fruit_list_df.index),['Avocado','Strawberries'])
streamlit.dataframe(fruit_list_df.loc[fruit_selected])
