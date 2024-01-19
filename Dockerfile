#Base Image
FROM python:3.9.18-slim-bullseye

# Set the working directory in the container
WORKDIR /app

#COPY THE SOURCE CODE
COPY app.py app.py

#COPY REQUIREMENTS FILE
COPY  requirements.txt requirements.txt

# INSTALL
RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "app.py" ]
