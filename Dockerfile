FROM python:3.7
ENV PYTHONUNBUFFERED 1
# Gettext
# RUN apt-get update && apt-get install -y gettext libgettextpo-dev \
# locales \
# locales-all \
# python3.7-dev
ENV DEBUG False
COPY requirements.txt /code/requirements.txt
WORKDIR /code
RUN pip install -r requirements.txt
ADD . .
# RUN python manage.py collectstatic --noinput
CMD [ "gunicorn", "--bind", "0.0.0.0", "-p", "8000",  "khanbuta_store.wsgi" ]