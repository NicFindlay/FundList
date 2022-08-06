# Pull base image

FROM --platform=linux/amd64 python:3.10.4-slim-bullseye

# set environmental variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#Set work directory

WORKDIR /FUNDLIST-MASTER

# Install dependencies

COPY ./requirements.txt .
RUN pip install -r requirements.txt 

# Copy project 

COPY . .
