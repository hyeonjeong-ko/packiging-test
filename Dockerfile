FROM python:3.7

COPY entrypoint.sh /entrypoint.sh

# Grant execute permission to all files in the directory (optional)
RUN chmod +x *

ENTRYPOINT ["/entrypoint.sh"]

WORKDIR /app
COPY test.py .
