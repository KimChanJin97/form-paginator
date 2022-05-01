from django.contrib import admin
from .models import Blog, Comment #comment 추가
#같은 폴더 내에 있는 model 안에서 blog라는 객체를 가져와라
# Register your models here.
admin.site.register(Blog)
#admin site에 등록해라
admin.site.register(Comment)
# Register your models here.
