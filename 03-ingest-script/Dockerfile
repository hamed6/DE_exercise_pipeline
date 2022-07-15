FROM python:3.9

# RUN apt-get intall wget

RUN pip install pandas sqlalchemy psycopg2

WORKDIR /app

COPY check_logfile.py taxi_data_light.csv ./

ENTRYPOINT ["python", "check_logfile.py"]
