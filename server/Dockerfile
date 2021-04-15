FROM python:3.8-slim AS server

RUN mkdir /server
WORKDIR /server

COPY ./server/requirements.txt /server/
RUN pip install -r requirements.txt
COPY ./server /server

# for podman
#RUN adduser --disabled-password user
#RUN chown user:user -R /server/
#USER user
ARG secret_KEY
ENV secret_KEY=$secret_KEY

RUN python ./manage.py collectstatic
