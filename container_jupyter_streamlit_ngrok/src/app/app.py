import streamlit as st
import pandas as pd

###
# Functions section


###


st.markdown("# Decision Automation from BigQuery")

st.markdown("## 1) Original Table in BigQuery")

df = pd.read_csv("data_lake/input/youtube_tutorial_report_table_sample.csv")

st.dataframe(df.head(10))

st.markdown("## 2) Filtering Table")

# Filter for considering only not analyzed video
df_filtered = df[(df['isTutorial']!="Y") & (df['isTutorial']!="N")]

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
st.download_button("Download as .csv", df_copy.to_csv(index=False), "output.csv", use_container_width=True)