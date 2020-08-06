from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Post
from .forms import PostForm
from django.utils import timezone


# publish된 포스트 리스트를 가져오는 함수 
def post_list(request):
	# 이 변수는 쿼리셋을 받고 있음.
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
	# post = Post.objects.get(pk=pk)
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			# commit=False는 작성자 정보 추가 후 모델에 저장하기 위해서임
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form':form})

def post_edit(request, pk):
	# 수정하고자 하는 글을 pk로 찾아 인스턴스로 가져옴.
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form':form})