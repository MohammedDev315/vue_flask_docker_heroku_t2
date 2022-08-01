FROM python:3.8.3-slim

RUN python -m pip install --upgrade pip

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

WORKDIR /app1

COPY . .

RUN pip install -r requirements.txt

# for heroku deployment :
CMD ["gunicorn"  , "app:app"]
# for Docker container :
# CMD [ "python3", "app.py"]
