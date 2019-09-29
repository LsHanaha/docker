FROM ruby:latest

RUN apt-get update -qq && apt-get install -y apt-utils libpq-dev build-essential nodejs sqlite3
RUN gem update && gem install rails

RUN mkdir -p /opt/app


COPY Gemfile /opt/app/Gemfile
COPY Gemfile.lock /opt/app/Gemfile.lock
WORKDIR /opt/app
COPY app /opt/app



RUN bundle install
RUN rake db:migrate
RUN rake db:setup

