import streamlit as st
from google.cloud import bigquery
import pandas_gbq

# Google Cloud Project ID and dataset ID
project_id = "bigquery-to-streamlit"
dataset_id = "bigquery-to-streamlit.yt_db"

# Start a BigQuery client
client = bigquery.Client(project=project_id)

# SQL query to select data from the table
sql = """
SELECT * 
FROM `{}.{}`
""".format(dataset_id, "bigquery-to-streamlit.yt_db.df")

# Load data into a DataFrame
df = pandas_gbq.read_gbq(sql, project_id=project_id)

# Display DataFrame in Streamlit
st.write(df)
