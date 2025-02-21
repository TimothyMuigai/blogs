from django.contrib import admin
from .models import Author, Blog, Subscriber

# Register your models here.
admin.site.register(Author)
admin.site.register(Blog)
admin.site.register(Subscriber)