# Tutorial
> 해당 tutorial 에서는 기본적인 python web library 을 파악한다. <br>
> server, client로 나뉘어져 있으며 대표적으로 `urllib`, `http` 가 존재한다. 

http 는 client, server 관련 저수준 library 들이 정의되어 있다.
urllib 는 client side 에서 필요한 고수준 library 들이 정의 되어 있다. 


# 1. urllib
## 1.1 url 을 제어하는 방법 
url 은 application 이 받아야 할 정보를 제공 합니다.   
서버 측에서 어떤 page 을 보여 주어야 할지 또는 어떤 행동을 해야 할지 정보를 제공하는 역활을 합니다.

url 에서 제공되는 인자는 여러가지가 있습니다. 
url 은 아래와 같은 방법으로 생성됩니다.

```shell script
scheme://주소/path;params?query#fragment

https://www.google.co.kr/?search?q=paui
``` 



url 을 parsing 하는 method 을 urllib 에서 제공 합니다. 

1. urlparse()
 1.1 scheme
 1.2 주소
 1.3 path
 1.4 params
 1.5 query
 1.6 fragment
 
2. urlsplit()
3. urljoin()
4. parse_qs()
5. quote()
6. encode() 


### 1.2 urllib.requests 
> url 을 통해 서버로 신호를 송신 및 수신 하는 모듈 

서버에 신호를 보내는건 기본적으로 2가지가 있습니다. 
`GET`, `POST`

`GET` 은 간단하게 url 을 통해서 정보를 전달하는 방법라고 생각하면 됩니다. 

아래 url 도 get 방식으로 신호를 전달하는 주요 예시라고 볼수 있습니다. 
pai 라는 검색어로 검색 하라는 검색기능을 제공 하는것으로 볼수 있습니다. 
```https://www.google.co.kr/?search?q=pai```
 
`POST` 은 보내야 할 정보들이 크거나 할때 주로 사용합니다. 


1.2.1 urllib.requests.urlopen

GET 방식으로 신호를 보내는 방법
```shell script
url = 'http://google.co.kr/?search?q=pai'
urlopen(url)
```

POST 방식으로 신호를 보내는 방법
```shell script
url = 'http://google.co.kr'
data = 
urlopen(url)
```

1.2.2    




