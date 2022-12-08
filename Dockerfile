FROM python:3.11.1-alpine3.16

COPY rw_rate_all.py /rw_rate_all.py

ENTRYPOINT ["/usr/local/bin/python", "/rw_rate_all.py"]

ENV APP_VERSION="2021.1" \
    PYTHONUNBUFFERED="1"
