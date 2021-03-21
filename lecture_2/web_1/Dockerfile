FROM ubuntu:18.04
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && apt-get install -y --reinstall systemd \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

RUN apt-get update && apt-get install -y vim supervisor nginx net-tools curl cron
RUN pip install gunicorn django requests
RUN apt-get install nginx

# Default nginx setting 을 지워주어야 한다.
RUN rm -f /etc/nginx/sites-available/default
RUN rm -f /etc/nginx/sites-enabled/default

# Nginx service setting file
COPY nginx.conf /etc/nginx/nginx.conf
COPY test_project /etc/nginx/sites-enabled/

# Entrypoint
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
