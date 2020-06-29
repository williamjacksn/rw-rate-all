FROM python:3.8.3-alpine3.11

COPY rw_rate_all.py /rw_rate_all.py

ENTRYPOINT ["/usr/local/bin/python", "/rw_rate_all.py"]

ENV APP_VERSION="2020.1" \
    PYTHONUNBUFFERED="1"
