from django.contrib import admin
from .models import Post

# 관리자 페이지에서 추가, 수정, 삭제할 수 있게 하기 위해 모델을 등록 
admin.site.register(Post)
