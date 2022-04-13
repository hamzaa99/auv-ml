FROM python:3.8-slim

# We copy just the requirements.txt first to leverage Docker cache
COPY requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip3 install virtualenv && python -m virtualenv -p python3 venv
RUN pip3 install -r requirements.txt

COPY . /app

ENV FLASK_APP=app:app
CMD ["flask", "run", "--host", "0.0.0.0"]