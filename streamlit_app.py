import streamlit
import pandas

fruit_list_df = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")


streamlit.title("Snowflake project")
streamlit.header("Breakfast")
streamlit.text("🥣 Oatmeal")
streamlit.text("🥗 Smoothie")
streamlit.text("🐔 Egg")
streamlit.text("🥑🍞 Avocado toast")

streamlit.header("Special Menu")
streamlit.multiselect("Pick some fruits:", list(fruid_list_df.index))
streamlit.dataframe(fruit_list_df)
