from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Record

admin.site.register(Record)