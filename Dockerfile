# sintax=docker/dockerfile:1
FROM python:3.8-slim-buster
RUN apt update
RUN apt-get install libsndfile1 -y
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python3", "app.py"]