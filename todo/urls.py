from django.contrib import admin
from django.urls import path
from todo import views 
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.home, name = 'home'),
    path('admin/', admin.site.urls),
    #path('signup/', views.signupuser, name = 'signupuser'),
    path('current/', views.currenttodos, name = 'currenttodos'),
    path('completed/', views.completedtodos, name = 'completedtodos'),
    #path('logout/', views.logoutuser, name = 'logoutuser'),
   # path('login/',auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
    #path('login/', views.loginuser, name = 'loginuser'),
    path('create/', views.createtodo, name = 'createtodo'),
    path('todo/<int:todo_pk>', views.viewtodo, name = 'viewtodo'),
    path('todo/<int:todo_pk>/complete', views.completetodo, name = 'completetodo'),
    path('todo/<int:todo_pk>/delete', views.deletetodo, name = 'deletetodo'),
]
