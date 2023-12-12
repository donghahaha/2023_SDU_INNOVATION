from accounts.serializers import User
from django.contrib import admin
from .models import Community, Comment
# Register your models here.
admin.site.register(Community)
admin.site.register(Comment)