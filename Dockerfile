# FROM python:3.10-slim-buster

# WORKDIR /app

# COPY . /app

# RUN pip install -r requirements.txt

# CMD ["python3", "app.py"]

FROM python:3.10-slim-buster

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip \
 && pip install -r requirements.txt

EXPOSE 8080

CMD ["python3", "app.py"]
