FROM python:3.8-slim-buster

WORKDIR /rssbuddy

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

RUN pip3 install psycopg2-binary

COPY . .

CMD [ "python3", "run.py"]

# docker build -t rssbuddy .
docker run -d --name rssbuddy_new -p 8000:8000 -e POSTGRES_USER=vignesh -e POSTGRES_PW=passs -e POSTGRES_URL=172.17.0.3:5432 -e POSTGRES_DB=rssbuddy rssbuddy_new
