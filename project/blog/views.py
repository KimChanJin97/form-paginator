from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import CommentForm, BlogForm
from django.core.paginator import Paginator

# Create your views here.
def home(request): # 페이지 & 쿼리셋 가져오기 함수
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 5) # blogs 데이터베이스를 8개로 페이지 구분
    pagnum = request.GET.get('page') # 페이지별로 구분하고 그 변수page를 가져와서 pagnum변수에 저장
    blogs = paginator.get_page(pagnum) # pagnum변수를 가져와서 blogs에 저장
    return render(request, 'home.html', {'blogs':blogs})

def detail(request,id): # 페이지 & 쿼리셋 가져오기 함수
    blog = get_object_or_404(Blog, pk = id)
    form=CommentForm()
    return render(request, 'detail.html', {'blog':blog, 'form':form})

def new(request): # 페이지 가져오기 함수
    if request.method == 'POST': # 데이터가 입력된 후 제출 버튼을 누르고 데이터 저장 = POST
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else: # 정보가 입력되지 않은 빈칸으로 되어있는 페이지 보여귀 = GET
        form = BlogForm()
        return render(request, 'new.html', {'form':form})

def create(request): # DB 가져오는 함수
    new_blog = Blog()
    new_blog.title = request.POST['title'] # POST 형식으로 데이터 받을 땐 redirect 해야 함
    new_blog.sub_title = request.POST['sub_title'] # POST 형식으로 데이터 받을 땐 redirect 해야 함
    new_blog.contents = request.POST['contents']  # POST 형식으로 데이터 받을 땐 redirect 해야 함
    new_blog.image = request.FILES['image'] ## 글 삭제시 기존 사진 삭제하는 기능 구현했음
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
    if request.FILES:
        update_blog.image = request.FILES['image'] ## 사진 수정시 기존 사진 삭제하는 기능 구현해야 함
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