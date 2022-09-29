# oskarcode.com
Project background: 
I have created my blog(oskarcode.com) and made it live with the tutorial here as part of my learnings, https://www.youtube.com/watch?v=Sa_kQheCnds&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=13
I have changed some parts and deployed it with different way.  You can see the codes here, 

Blog function: 
User can view the posts, to post a content, use can create an account and post, delete, update the posts they created
User can create/update their profile 
Admin can set and change the permission


Platforms I used:
Python, Django for the development 
AWS ubuntu EC2 for hosting, Nginx for web server 
Cloudflare domain, DNS, SSL, and CDN

Project directory
settings.py
- update installed application, every time when we created new apps, need to add the class name from apps.py
urls.py
- define the path, function, and name


App directory
urls.py
- redirect from project urls.py
views.py
-main function/logic for the apps
templates/app name 
-template for the views, e.g., base.html
- can reused for other templates, can be defined with:  {% block content %}{% endblock%}, the block area can be overwritten, other area kept same with sub template ,to extend the base.html, put {% extends 'base.html %}
static/app name
-need to create this folder for static files such as main.css. To include main.css file put {% load static %} on the top of the files, in href='{% static 'static/main.css %}', what this does here is generate a path to access


Some of Syntax 
-django-admin: to get all Django commands
- {{}} : access variable, a bit like dictionary, e.g., {{post.title}}, this will get title of the post 
- {% %} : put function in it, e.g., {% for i in n% }{% endfor }, this will run for loop
- { % static 'path' %}: access the static path, e.g., href = '{ % static 'path' %}'
- {% url 'path '%} : access the url path, e.g, href = '{ % url 'path' %}', instead of hardcoding url path, we used url function and name of the path to get the url
- makemigrations/migrate anytime update DB, needs to run this to update, when migrated, it creates a DB table backend for us
-python manage.py shell: we can play with models or db with SQL language


Security best practices:
- use variables for sensitive info such as secret keys, email credential
![image](https://user-images.githubusercontent.com/63486484/193052402-1e80e0d4-9f88-4e1f-8368-879877de2964.png)
