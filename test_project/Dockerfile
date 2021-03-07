FROM ubuntu:18.04
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && apt-get install -y --reinstall systemd \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

RUN apt-get update && apt-get install -y vim supervisor nginx net-tools curl cron
RUN pip install gunicorn django requests

# 현재 폴더를 srv 폴더에 추가합니다.
ADD . /srv
WORKDIR /srv

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# open port
EXPOSE 8000

# run gunicorn
CMD exec gunicorn test_project.wsgi:application --bind 0.0.0.0:8000

# docker build -t gunicorn .
# docker run -d --rm -p 8000:8000 gunicorn
