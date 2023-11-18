FROM python:3.11-alpine
WORKDIR /aircraft-takeoff-time-logger
COPY . /aircraft-takeoff-time-logger
RUN pip install -r requirements.txt
CMD [ "python", "run.py" ]