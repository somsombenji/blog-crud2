from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from .forms import NewBlog #이거 두개 임포트 해주는거 잊지말자

def index(request):
    return render(request, 'index.html')

def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog':blog_detail})


def create(request):
    if request.method == 'POST':
        form_content = NewBlog(request.POST)
        if form_content.is_valid:
            post = form_content.save(commit=False) #아직은 저장x
            post.pub_date = timezone.now() #현재시간
            post.save() #이제 저장
            return redirect('home')
    else:
        forms = NewBlog()
        return render(request, 'new.html', {'forms':forms})


def delete(request, blog_id): #urls.py에 있는 int:blog_id
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    return redirect('home')


def update(request, blog_id):
    forms = get_object_or_404(Blog, pk=blog_id)
    
    if request.method == 'POST':
        forms.title = request.POST['title'] #name=title인 애한테 담긴 내용 저장
        forms.body = request.POST['body'] #name=body인 애한테 담긴내용 저장
        forms.save()
        return redirect('/blog/'+str(blog_id))

    else: #수정사항을 입력하려고 페이지에 접속하면
        return render(request, 'new.html', {'forms':forms})


