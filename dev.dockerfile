FROM python:3.8.7-buster

EXPOSE 8000

RUN pip install -r ./requirements.txt
COPY . /django
WORKDIR /django
ENTRYPOINT ["python", "manage.py", "runserver", "0:8000"]