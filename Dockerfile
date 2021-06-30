FROM python:3.9.6-alpine3.14

COPY rw_rate_all.py /rw_rate_all.py

ENTRYPOINT ["/usr/local/bin/python", "/rw_rate_all.py"]

ENV APP_VERSION="2020.2" \
    PYTHONUNBUFFERED="1"
