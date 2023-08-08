FROM python:3.8-slim-buster

WORKDIR /rssbuddy

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

RUN pip3 install psycopg2-binary

COPY . .

CMD [ "python3", "run.py"]

# docker build -t rssbuddy .
# docker run -d --name rssbuddy -p 8000:8000 -e POSTGRES_USER=dsds -e POSTGRES_PW=sdsd -e POSTGRES_URL=0.0.0.0:5432 -e POSTGRES_DB=rssbuddy rssbuddy