import streamlit as st
import pandas as pd

st.title("test ciao")

df = pd.read_csv("data_lake/input/youtube_tutorial_report_table_sample.csv")
edited_df = st.experimental_data_editor(df)
st.dataframe(edited_df)