from django.shortcuts import render
from .models import Post
from django.utils import timezone

# publish된 포스트 리스트를 가져오는 함수 
def post_list(request):
	# 이 변수는 쿼리셋을 받고 있음.
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})
