import streamlit as st
import pandas as pd

from google.cloud import bigquery
import pandas_gbq
import numyp as np

###
# Functions section


###


st.markdown("# Decision Automation from BigQuery")

st.markdown("## 1) Original Table in BigQuery")

# df = pd.read_csv("data_lake/input/youtube_tutorial_report_table_sample.csv")

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

st.dataframe(df.head(10))

st.markdown("## 2) Filtering Table")

# Filter for considering only not analyzed video
df_filtered = df[df['isTutorial'].isnull()]

country = st.selectbox("Filter Table for the country desidered.",("DE","IT","GB"),index=2)

df_filtered = df_filtered[df_filtered['regionCode']==country]

st.write("This is the number of unique videos for the selected country: ",df_filtered['videoId'].nunique())

st.markdown("## 3) Edit Table")

df_filtered['isTutorial'] = df_filtered['isTutorial'].astype("category")
df_filtered['isTutorial'] = df_filtered['isTutorial'].cat.add_categories(("Y", "N","NA"))

df_edited = st.experimental_data_editor(df_filtered)

# Replace edited rows on original dataframe
df_copy = df.copy()
df_copy.update(df_edited)

st.markdown("## 4) Check Edited Table")
st.dataframe(df_copy.head(10))

st.markdown("## 5) Save back to BigQuery or Download locally")

# st.write(df_copy['isTutorial'].value_counts(dropna=False))

# for column in df_copy.columns:
#     types = df_copy[column].apply(type).unique()
#     st.write(f"Column: {column}")
#     st.write("Unique types:")
#     st.write(list(types))

# Define mapping for pandas datatypes to appropriate NaN/None representations
nan_values = {
    np.dtype('O'): None,
    np.dtype('int64'): np.iinfo(np.int64).min,
    np.dtype('<M8[ns]'): pd.NaT,
}

# Convert None values to appropriate NaN representation based on column type
for column in df_copy.columns:
    correct_nan_value = nan_values.get(df_copy[column].dtype, None)
    if correct_nan_value is not None:
        df_copy[column] = df_copy[column].apply(lambda x: correct_nan_value if x is None else x)


# Create a button for saving changes to BigQuery
if st.button('Save to BigQuery'):
    df_copy.to_gbq('{}.{}'.format(dataset_id, table_id), project_id, if_exists='replace')
    st.success("Data saved to BigQuery successfully!")

st.download_button("Download as .csv", df_copy.to_csv(index=False), "output.csv", use_container_width=True)