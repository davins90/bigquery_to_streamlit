# 1. Introduction
## 1.1 Purpose
This document describes the functionality provided by a Streamlit web application that connects to Google BigQuery to read a table, allows users to edit the table in the application, and saves the updated table back to BigQuery.

## 1.2 Scope
The software system is a Streamlit web application designed for handling data stored in Google BigQuery. The app reads a BigQuery table into a pandas dataframe, enables user to filter and edit data, and pushes the changes back to BigQuery.

# 2. Overall Description
## 2.1 Product Perspective
This software is standalone and doesn't rely on any existing software or systems. It is designed to improve the data editing process by providing a user-friendly interface that allows for easier management of data stored in Google BigQuery.

## 2.2 Product Functions
The main functions of this software are as follows:

Connect to Google BigQuery and read a specified table into a pandas dataframe.
Display the data in Streamlit, with options to filter based on 'isTutorial' and 'regionCode' columns.
Provide an editing interface for the users to make changes to the dataframe.
After changes are made, the modified dataframe can either be saved back to BigQuery or downloaded locally as a CSV file.
# 3. Specific Requirements
## 3.1 External Interface Requirements
The application requires a working internet connection to connect to Google BigQuery.

## 3.2 Software Requirements
The following Python packages are required:

- Streamlit 1.22.0: For creating the web application interface.
- Openpyxl 3.0.9: Required for handling Excel files.
- Et-xmlfile 1.1.0: Dependency for openpyxl.
- Plotly 5.7.0: Required for generating interactive plots.
- Pandas_gbq 0.19.2: Required for interacting with Google BigQuery.

## 3.3 Installation Requirements
The software is Dockerized and the DockerFile is provided for deployment. Docker needs to be installed to build and run the Docker image. After Docker is installed, the software can be run using the command docker build -t app . && docker run -p 8501:8501 app.

# 4. System Features
## 4.1 BigQuery Connection and Data Retrieval
The system connects to a specified Google BigQuery instance, retrieves a dataset and displays the data in the Streamlit interface.

## 4.2 Data Filtering
The application provides options to filter data based on 'isTutorial' and 'regionCode' columns.

## 4.3 Data Editing
The application provides an interface for users to edit the dataframe directly.

## 4.4 Saving Changes
After editing, users can choose to save the changes back to the original BigQuery table or download the edited data as a CSV file.

# 5. Deployment
The deployment of the web application involves the following steps:
- The codebase is added to a GitHub repository.
- A service on Google Cloud Run is created and linked to the GitHub repository where the Dockerfile is located. Each time an update is pushed to the repository, the service automatically triggers a build of the Docker image and deploys the updated application.
- Set autoscale == 0 for saving purpose
# 6. Future Enhancements
As the usage of the application grows, there may be a need for additional features such as advanced filtering options, support for multiple BigQuery tables, and role-based access control for editing data. These can be considered in future versions of the application.