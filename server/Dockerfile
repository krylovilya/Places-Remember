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

ARG YANDEX_API_KEY
ENV YANDEX_API_KEY=$YANDEX_API_KEY

ARG SOCIAL_AUTH_VK_OAUTH2_KEY
ENV SOCIAL_AUTH_VK_OAUTH2_KEY=$SOCIAL_AUTH_VK_OAUTH2_KEY

ARG SOCIAL_AUTH_VK_OAUTH2_SECRET
ENV SOCIAL_AUTH_VK_OAUTH2_SECRET=$SOCIAL_AUTH_VK_OAUTH2_SECRET

ARG SOCIAL_AUTH_FACEBOOK_KEY
ENV SOCIAL_AUTH_FACEBOOK_KEY=$SOCIAL_AUTH_FACEBOOK_KEY

ARG SOCIAL_AUTH_FACEBOOK_SECRET
ENV SOCIAL_AUTH_FACEBOOK_SECRET=$SOCIAL_AUTH_FACEBOOK_SECRET

RUN python ./manage.py collectstatic --noinput
COPY /server/staticfiles ./server/staticfiles
