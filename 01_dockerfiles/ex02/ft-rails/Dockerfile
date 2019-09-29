FROM ruby:latest

RUN apt-get update -qq && apt-get install -y apt-utils libpq-dev build-essential nodejs sqlite3 git
RUN gem install rails --version 4.2.4


RUN mkdir -p /opt/app

# ONBUILD COPY app /opt/app
WORKDIR /opt/app
ONBUILD ADD app /opt/app



ONBUILD EXPOSE 3000
ONBUILD RUN bundle install
ONBUILD RUN db:migrate
ONBUILD RUN db:seed

