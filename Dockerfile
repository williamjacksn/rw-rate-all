FROM python:3.9.5-alpine3.13

COPY rw_rate_all.py /rw_rate_all.py

ENTRYPOINT ["/usr/local/bin/python", "/rw_rate_all.py"]

ENV APP_VERSION="2020.2" \
    PYTHONUNBUFFERED="1"
