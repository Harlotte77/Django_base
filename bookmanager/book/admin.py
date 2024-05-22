from django.contrib import admin
from .models import PeopleInfo, BookInfo

# 注册模型类
admin.site.register(BookInfo)
admin.site.register(PeopleInfo)