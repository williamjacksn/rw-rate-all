FROM python:3.8.3-alpine3.12

COPY rw_rate_all.py /rw_rate_all.py

ENTRYPOINT ["/usr/local/bin/python", "/rw_rate_all.py"]

ENV APP_VERSION="2020.2" \
    PYTHONUNBUFFERED="1"
