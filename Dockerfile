FROM python:3.7.4-alpine3.10

COPY rw_rate_all/rw_rate_all.py /rw_rate_all.py

ENTRYPOINT ["/usr/local/bin/python", "/rw_rate_all.py"]
