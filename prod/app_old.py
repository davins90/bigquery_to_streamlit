import streamlit as st
from google.cloud import bigquery
import pandas_gbq

# Google Cloud Project ID
project_id = "bigquery-to-streamlit"

# Dataset ID and Table ID
dataset_id = "yt_db"
table_id = "df"

# Start a BigQuery client
# client = bigquery.Client(project=project_id)

# SQL query to select data from the table
sql = """
SELECT * 
FROM `{}.{}`
""".format(dataset_id, table_id)

# Load data into a DataFrame
df = pandas_gbq.read_gbq(sql, project_id=project_id)

# Display DataFrame in Streamlit
st.write(df)
