FROM python:3.7

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/
RUN pip install -r requirements.txt

CMD ./manage.py wait_for_db && ./manage.py migrate && ./manage.py createcachetable && ./manage.py runserver 0.0.0.0:3001
