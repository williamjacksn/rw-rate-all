FROM python:3.8.1-alpine3.11

COPY rw_rate_all/rw_rate_all.py /rw_rate_all.py

ENTRYPOINT ["/usr/local/bin/python", "/rw_rate_all.py"]
