from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
          readonly_fields = ('created',)

# Register your models here.
admin.site.register(Todo, TodoAdmin)