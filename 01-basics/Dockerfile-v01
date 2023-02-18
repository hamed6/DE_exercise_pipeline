FROM python:3.9

WORKDIR /app
COPY basic_pipeline.py basic_pipeline.py 

RUN pip install pandas

ENTRYPOINT ["python", "basic_pipeline.py"]