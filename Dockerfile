FROM python:3.9.7-alpine3.14

COPY rw_rate_all.py /rw_rate_all.py

ENTRYPOINT ["/usr/local/bin/python", "/rw_rate_all.py"]

ENV APP_VERSION="2021.1" \
    PYTHONUNBUFFERED="1"
