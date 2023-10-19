FROM python

ENV PYTHONBUFFERED 1

WORKDIR /eventplatform

ADD . /eventplatform

COPY ./requirements.txt /eventplatform/requirements.txt

RUN pip install -r requirements.txt

COPY . /eventplatform