FROM python:3.11.4-slim-bullseye
WORKDIR /app

RUN apt-get update

COPY ./requirements.txt /app/

RUN pip install -r requirements.txt


COPY . /app

RUN python manage.py cllectstatic -y

ENTRYPOINT [ "gunicorn", "Nnaezitech.wsgi" ]