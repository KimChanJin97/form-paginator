from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
##
from .forms import CommentForm
##

# Create your views here.
def home(request): # 페이지 & 쿼리셋 가져오기 함수
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs':blogs})

def detail(request,id): # 페이지 & 쿼리셋 가져오기 함수
    blog = get_object_or_404(Blog, pk = id)
    form=CommentForm()
    return render(request, 'detail.html', {'blog':blog, 'form':form})

def new(request): # 페이지 가져오기 함수
    return render(request, 'new.html')

def create(request): # DB 가져오는 함수
    new_blog = Blog()
    new_blog.title = request.POST['title'] # POST 형식으로 데이터 받을 땐 redirect 해야 함
    new_blog.sub_title = request.POST['sub_title'] # POST 형식으로 데이터 받을 땐 redirect 해야 함
    new_blog.contents = request.POST['contents']  # POST 형식으로 데이터 받을 땐 redirect 해야 함
    new_blog.save()
    return redirect('detail', new_blog.id)

def edit(request, id):
    edit_blog = get_object_or_404(Blog, pk = id) # 페이지 & 쿼리셋 가져오기 함수
    return render(request, 'edit.html', {'blog':edit_blog})

def update(request, id):
    update_blog = get_object_or_404(Blog, pk=id)
    update_blog.title = request.POST['title'] # POST 형식으로 데이터 받을 땐 redirect 해야 함
    update_blog.sub_title = request.POST['sub_title'] # POST 형식으로 데이터 받을 땐 redirect 해야 함
    update_blog.contents = request.POST['contents'] # POST 형식으로 데이터 받을 땐 redirect 해야 함
    update_blog.save()
    return redirect('detail', update_blog.id)

def delete(request, id):
    delete_blog = get_object_or_404(Blog, pk=id)
    delete_blog.delete()
    return redirect('home') # 삭제하면 돌아갈 곳이 없으므로 redirect 해야 함

def add_comment_to_post(request, blog_id):
    blog=get_object_or_404(Blog, pk=blog_id)
    if request.method == "POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=blog
            comment.save()
            return redirect('detail', blog_id)


