FROM python:3.9

WORKDIR /service

COPY ./requirements.txt /service/requirements.txt

RUN pip install -r requirements.txt

COPY ./app /service/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]