FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app


# Grant executable permissions to django.sh
RUN  python3 manage.py makemigrations
# RUN python3 manage.py migrate