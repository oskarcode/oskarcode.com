from django.contrib import admin
from .models import Post # registe model so that it can show up in admin page
# Register your models here.

admin.site.register(Post) # with this, we can access post models in admin and edit there 