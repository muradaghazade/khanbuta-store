FROM python:3.7

ENV PYTHONUNBUFFERED 1


COPY requirements.txt /code/requirements.txt
COPY manage.py /code/manage.py
COPY data.json /code/data.json

WORKDIR /code
RUN pip install -r requirements.txt
RUN python3 manage.py loaddata data.json
ADD . .