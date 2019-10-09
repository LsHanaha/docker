FROM ruby:2.6.3

ENV PACKAGES="apt-utils libpq-dev build-essential nodejs sqlite3 yarn npm"

RUN apt-get update -qq && \
    apt-get install -y $PACKAGES

RUN mkdir -p /opt/app
WORKDIR /opt/app

COPY app/Gemfile Gemfile
COPY app/Gemfile.lock Gemfile.lock
RUN bundle install

ADD app .

RUN rails db:create && \
    rails db:migrate
