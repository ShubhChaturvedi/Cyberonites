from django.contrib import admin
from .models import Staff , Post
# Register your models here.
admin.site.register((Staff , Post))