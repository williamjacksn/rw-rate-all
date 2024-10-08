FROM python:3.13-slim

COPY rw_rate_all.py /rw_rate_all.py

ENTRYPOINT ["/usr/local/bin/python", "/rw_rate_all.py"]

ENV APP_VERSION="2024.1" \
    PYTHONUNBUFFERED="1"
