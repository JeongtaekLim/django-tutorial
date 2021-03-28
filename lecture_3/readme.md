# 목적 
`192.168.0.16:80/helloworld` 로 `get` 방식으로 `reqeust` 을 전송했을 때 `backend` 집합으로 `was1`, `was2` 서버에게 round robin 으로 전송함.  
`192.168.0.16:80/helloworld` 로 `get` 방식으로 `reqeust` 을 전송했을 때 `backend` 집합으로 `was3`, `was4` 서버에게 round robin 으로 전송함.  
`was1` 으로 `192.168.0.16:80/helloworld` 으로 request 가 날라올 시 `helloworld1` 을 반환  
`was2` 으로 `192.168.0.16:80/helloworld` 으로 request 가 날라올 시 `helloworld2` 을 반환  
`was3` 으로 `192.168.0.16:80/helloworld` 으로 request 가 날라올 시 `helloworld3` 을 반환  
`was4` 으로 `192.168.0.16:80/helloworld` 으로 request 가 날라올 시 `helloworld4` 을 반환          
     
아래와 같은 구조로 서버를 설계함.


![Imgur](https://i.imgur.com/LSc28K0.png)

1. Nginx 서버 셋팅은 default config 파일 http context(directive)에 아래 코드를 추가한다.<br>
 
```shell script
upstream backend{
    server 192.168.0.16:8000 weight=1;
    server 192.168.0.16:8001 weight=1;
    }

    upstream backend1{
    server 192.168.0.16:8002 weight=1;
    server 192.168.0.16:8003 weight=1;
    }

   server {
      listen 80;
      location / {
          proxy_pass http://backend;
      }
   }

   server {
      listen 81;
      location / {
          proxy_pass http://backend1;
      }
   }  
```

위 코드를 통해 192.168.0.16:80 으로 접속한 유저는 192.168.0.16:8000 또는 192.168.0.16:8001 로 
포트포워딩 된다.     
192.168.0.16:81 으로 접속한 유저는 192.168.0.16:8002 또는 192.168.0.16:8003 로 
포트포워딩 된다.     

2. web 서버 `dockerfile`에 아래 코드를 추가한다.   

```dockerfile
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 81
EXPOSE 80
```

3. docker 을 빌드하고 docker 을 실행한다.

```shell script
# docker build
docker build -t nginx_lec3 .

# docker run with deamon
docker run -d --rm -p 80:80 -p 81:81 nginx_lec3

# docker run with bash
docker run -it --rm -p 80:80 -p 81:81 nginx /bin/bash
```