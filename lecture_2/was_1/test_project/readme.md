# Django Tutorial with docker

1. 가상 환경 설치 

2. Django install 

3. 프로젝트 생성 하기 
   `django-admin startproject test_project`

4. 프로젝트 내 App 생성 하기 
   `python manage.py startapp helloworld_echo`

5. `test_project/test_project/Settings.py:INSTALLED_APPS`에 app 등록하기

   ```python
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       "helloworld_echo",
   ]
   ```

6. view 만들기 

   1. `test_project/helloworld_echo` 에 `urls.py` 만들기 

   2. `test_project/test_project/urls.py`에 아래와 같이 include 사용해서 코딩하기 

      ```python
      # test_project/test_project/urls.py
      from django.contrib import admin
      from django.urls import path, include
      
      urlpatterns = [
          path('admin/', admin.site.urls),
          # helloworld_echo에 있는 urls.py 주소를 include 함. 
          path('helloworld', include('helloworld_echo.urls'))
      ]
      ```

   3. `test_project/helloworld_echo/urls.py`에 아래와 같이 코딩하기

      ```python
      from django.urls import path
      from . import views
      
      urlpatterns = [
          # path 안 앞에 있는 string 은 ''이 되어야 함
          path('', views.helloworld, name='helloworld'),
      ]
      ```

   4. `/test_project/helloworld_echo/views.py`에 아래와 같이 코딩하기

      ```python
      from django.http import HttpResponse
      from django.shortcuts import render
      from requests import Response
      
      def helloworld(request):
          return HttpResponse('Helloworld')
      
      ```

7. Run server 

   `Terminal` 에서 아래 명령어 수행 (manage.py 파일이 있는 위치에서)

   ```shell
   python manage.py runserver
   ```

8. Web Browser(ex chrome)에서 아래 주소 입력 

   ```
   http://lcoalhost:8000/helloworld
   ```

9. Gunicorn Server 실행 

   ```
   gunicorn --bind 0.0.0.0:8000 --workers 9 test_project.wsgi:application
   ```

   reference from [here](http://hell0-world.com/architecture/2020/05/10/gunicorn.html)

