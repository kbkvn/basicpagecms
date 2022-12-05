# syntax=docker/dockerfile:1
FROM python:3.8.3-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /BasicCMSLanding

RUN apk update \
    && apk add gcc python3-dev musl-dev jpeg-dev zlib-dev libjpeg

COPY ./requirements.txt /BasicCMSLanding
RUN pip3 install -r requirements.txt
COPY . /BasicCMSLanding

EXPOSE 8000

# Do not use this command in production
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
