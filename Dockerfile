FROM python:3.7.3-alpine3.9

RUN mkdir /code
WORKDIR /code

COPY ./src/requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

COPY ./src/ /code/

CMD python server.py