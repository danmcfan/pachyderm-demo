FROM python:3.11-slim-buster

WORKDIR /

COPY requirements.txt /requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY src/aggregate.py /aggregate.py
COPY src/bbox.py /bbox.py
COPY src/montage.py /montage.py
COPY src/normalize.py /normalize.py