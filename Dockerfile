# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
RUN apt-get update && apt-get install -y --no-install-recommends && apt-get clean
WORKDIR /app

RUN pip3 freeze > requirements.txt
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .


EXPOSE 8000

ENTRYPOINT [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]