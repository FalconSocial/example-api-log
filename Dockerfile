FROM python:3.7.3-slim-stretch

# Install build dependencies
RUN apt-get update \
 && apt-get install --no-install-recommends --assume-yes build-essential git gcc libcurl4-openssl-dev libssl-dev \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

WORKDIR app

# Install application dependencies
COPY requirements.txt ./requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Add application code
COPY run.py run.py
COPY logging.conf logging.conf
COPY api api

EXPOSE 8080

# Add command to run.
CMD ["gunicorn", \
     "--max-requests=3000", \
     "--log-level=debug", \
     "--workers=1", \
     "--bind=0.0.0.0:8080", \
     "--log-config=logging.conf", \
     "run:app"]
