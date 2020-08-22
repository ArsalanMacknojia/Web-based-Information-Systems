# --------------------------------------------BASE IMAGE-------------------------------------------- 

FROM python:3.8.1-slim-buster as builder

# set work directory
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends gcc
RUN pip install --upgrade pip

# install python dependencies
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

# --------------------------------------------MAIN IMAGE--------------------------------------------

FROM python:3.8.1-slim-buster

RUN mkdir -p /home/app

# create required directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends netcat
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*

# copy entrypoint.sh to created DB schema
COPY ./entrypoint.sh $APP_HOME

# copy project
COPY . $APP_HOME

ENTRYPOINT ["/home/app/web/entrypoint.sh"]
