FROM python:3.8.7-buster

ENV PROD True
COPY . /django
WORKDIR /django
RUN pip install -r ./requirements.txt
EXPOSE 8000
ENTRYPOINT ["python", "manage.py", "runserver", "0:8000"]