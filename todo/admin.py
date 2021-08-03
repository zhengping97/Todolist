from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin): #To see the created info appear on the admin web which can be read only
    readonly_fields = ('created',)

# Register your models here.
admin.site.register(Todo, TodoAdmin)
