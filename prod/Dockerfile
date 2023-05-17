FROM jupyter/datascience-notebook:python-3.9.2

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "app.py" , "--server.port=8501", "--server.address=0.0.0.0"]