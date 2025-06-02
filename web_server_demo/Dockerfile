FROM python:3.12-slim AS DemoProd 
RUN apt update && apt install -y \
    build-essential \
    libffi-dev \
    && apt clean
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /demo-server
ARG  DEMO_SRC_DIR=./
ARG  DEMO_RUN_DIR=./
VOLUME  /demo-server/
VOLUME  /demo-server/logs 
EXPOSE 7010
CMD  ["python", "/demo-server/run.py"]