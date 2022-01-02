# Log in 기능 구현
- 해당 페이지는 [해당 page](https://learndjango.com/tutorials/django-login-and-logout-tutorial) 을 참조해 만들어졌습니다.

## Object 

### Step 1: Setup
Start by creating a new Django project. This code can live anywhere on your computer. On a Mac, the desktop is a convenient place and that's where we'll put this code. We can do all of the normal configuration from the command line:

create a new auth directory for our code on the Desktop
install Django with Pipenv
start the virtual environment shell
create a new Django project called config
create a new Sqlite database with migrate
run the local server
Here are the commands to run:

```shell script
$ cd ~/Desktop
$ mkdir accounts && cd accounts
$ pipenv install django~=3.1.0
$ pipenv shell
(accounts) $ django-admin.py startproject config .
(accounts) $ python manage.py migrate
(accounts) $ python manage.py runserver
```

### Step 2: The Django auth app
Django automatically installs the auth app when a new project is created. Look in the config/settings.py file under INSTALLED_APPS and you can see auth is one of several built-in apps Django has installed for us.

```python
# config/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth', # Yoohoo!!!!
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
To use the auth app we need to add it to our project-level urls.py file. Make sure to add include on the second line. I've chosen to include the auth app at accounts/ but you can use any url pattern you want.
```python
# config/urls.py
from django.contrib import admin
from django.urls import path, include # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # new
]
```
The auth app we've now included provides us with several authentication views and URLs for handling login, logout, and password management.

The URLs provided by auth are:
```python
accounts/login/ [name='login']
accounts/logout/ [name='logout']
accounts/password_change/ [name='password_change']
accounts/password_change/done/ [name='password_change_done']
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete']
```
There are associated auth views for each URL pattern, too. That means we only need to create a template to use each!


### Step 3: Login Page

Let's make our login page! Django by default will look within a templates folder called registration for auth templates. The login template is called login.html.

Create a new directory called registration and the requisite login.html file within it. From the command line type Control-c to quit our local server and enter the following commands:
```shell
(accounts) $ mkdir templates
(accounts) $ mkdir templates/registration
(accounts) $ touch templates/registration/login.html
```
Note: Make sure that templates is created at the project level, not within an existing directory such as config. You can see the official source code here for further confirmation your structure is correct.

Then include this template code in our login.html file:

```html
<!-- templates/registration/login.html -->
<h2>Log In</h2>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Log In</button>
</form>
```
This is a standard Django form using POST to send data and {% csrf_token %} tags for security concerns, namely to prevent a CSRF Attack. The form's contents are outputted between paragraph tags thanks to {{ form.as_p }} and then we add a "submit" button.

Next update the settings.py file to tell Django to look for a templates folder at the project level. Update the DIRS setting within TEMPLATES as follows. This is a one-line change.

```python
# config/settings.py
TEMPLATES = [
    {
        ...
        'DIRS': [str(BASE_DIR.joinpath('templates'))],
        ...
    },
]
```
Our login functionality now works but to make it better we should specify where to redirect the user upon a successful login. In other words, once a user has logged in, where should they be sent on the site? We use the LOGIN_REDIRECT_URL setting to specify this route. At the bottom of the settings.py file add the following to redirect the user to the homepage.

```python
# config/settings.py
LOGIN_REDIRECT_URL = '/'
```
We're actually done at this point! If you now start up the Django server again with python manage.py runserver and navigate to our login page at http://127.0.0.1:8000/accounts/login/ you'll see the following.

![login](https://learndjango.com/static/images/tutorials/login_logout/login.png)


### Step 4: Create users
But there's one missing piece: we haven't created any users yet. Let's quickly do that by making a superuser account from the command line. Quit the server with Control+c and then run the command python manage.py createsuperuser. Answer the prompts and note that your password will not appear on the screen when typing for security reasons.

```shell script
(accounts) $ python manage.py createsuperuser
Username (leave blank to use 'wsv'):
Email address: will@learndjango.com
Password:
Password (again):
Superuser created successfully.
```

![login_](https://learndjango.com/static/images/tutorials/login_logout/homepage-error.png)

Now spin up the server again with python manage.py runserver and refresh the page at http://127.0.0.1:8000/accounts/login/. Enter the login info for your just-created user.
Homepage error

We know that our login worked because we were redirected to the homepage, but we haven't created it yet so we see the error Page not found. Let's fix that!

### Step 5: Create a homepage
We want a simple homepage that will display one message to logged out users and another to logged in users.

First quit the local server with Control+c and then create new base.html and home.html files. Note that these are located within the templates folder but not within templates/registration/ where Django auth looks by default for user auth templates.

```shell script

(accounts) $ touch templates/base.html
(accounts) $ touch templates/home.html
```
Add the following code to each:
```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>{% block title %}Django Auth Tutorial{% endblock %}</title>
</head>
<body>
  <main>
    {% block content %}
    {% endblock %}
  </main>
</body>
</html>
```

```html
<!-- templates/home.html -->
{% extends 'base.html' %}

{% block title %}Home{% endblock %}

{% block content %}
{% if user.is_authenticated %}
  Hi {{ user.username }}!
{% else %}
  <p>You are not logged in</p>
  <a href="{% url 'login' %}">Log In</a>
{% endif %}
{% endblock %}
```
While we're at it, we can update login.html too to extend our new base.html file:
```html
<!-- templates/registration/login.html -->
{% extends 'base.html' %}

{% block title %}Login{% endblock %}

{% block content %}
<h2>Log In</h2>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Log In</button>
</form>
{% endblock %}
```
Now update our urls.py file so we can display the homepage. Normally I would prefer to create a dedicated pages app for this purpose, but we don't have to and for simplicity, we'll just add it to our existing config/urls.py file. Make sure to import TemplateView on the third line and then add a urlpattern for it at the path ''.

```python
# config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'), # new
]
```

And we're done. If you start the Django server again with python manage.py runserver and navigate to the homepage at http://127.0.0.1:8000/ you'll see the following:

![Homepage logged in](https://learndjango.com/static/images/tutorials/login_logout/homepage-loggedin.png)

It worked! But how do we logout? The only option currently is to go into the admin panel at http://127.0.0.1:8000/admin/ and click on the "Logout" link in the upper right corner.

![Admin page logout link](https://learndjango.com/static/images/tutorials/login_logout/admin-logout.png)
This will log us out as seen by the redirect page:

![Admin page logged out](https://learndjango.com/static/images/tutorials/login_logout/admin-loggedout.png)

If you go to the homepage again at http://127.0.0.1:8000/ and refresh the page, we can see we're logged out.

![Home page logged out](https://learndjango.com/static/images/tutorials/login_logout/homepage-loggedout.png)
 
 
### Step 6: Logout link
Let's add a logout link to our page so users can easily toggle back and forth between the two states. Fortunately the Django auth app already provides us with a built-in url and view for this. And if you think about it, we don't need to display anything on logout so there's no need for a template. All really we do after a successful "logout" request is redirect to another page.

So let's first add a link to the built-in logout url in our home.html file:
```html
<!-- templates/home.html-->
{% extends 'base.html' %}

{% block title %}Home{% endblock %}

{% block content %}
{% if user.is_authenticated %}
  Hi {{ user.username }}!
  <p><a href="{% url 'logout' %}">Log Out</a></p>
{% else %}
  <p>You are not logged in</p>
  <a href="{% url 'login' %}">Log In</a>
{% endif %}
{% endblock %}
```
Then update settings.py with our redirect link which is called LOGOUT_REDIRECT_URL. Add it right next to our login redirect so the bottom of the settings.py file should look as follows:

```python
# config/settings.py
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/' # new
Actually, now that we have a homepage view we should use that instead of our current hardcoded approach. What's the url name of our homepage? It's home, which we named in our config/urls.py file:
```

```python
# config/urls.py
    ...
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    ...
```
So we can replace '/' with home at the bottom of the settings.py file:

```python
# config/settings.py
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
```

Now if you revisit the homepage and login you'll be redirected to the new homepage that has a "logout" link for logged in users.

![Homepage logout link](https://learndjango.com/static/images/tutorials/login_logout/homepage-logout-link.png)

Clicking it takes you back to the homepage with a "login" link.

![Homepage login link](https://learndjango.com/static/images/tutorials/login_logout/homepage-login-link.png)


 
 