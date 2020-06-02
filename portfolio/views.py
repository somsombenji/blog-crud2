from django.shortcuts import render,redirect, get_object_or_404
from .models import Portfolio


def portfolio(request):
    portfolios = Portfolio.objects
    return render(request, 'portfolio.html', {'portfolios':portfolios})

def create2(request):
    
    if request.method == 'POST': #POST로 요청이 들어오면
        portfolios = Portfolio()
        portfolios.photo = request.FILES['photo']
        portfolios.title = request.POST['title']
        portfolios.body = request.POST['body']
        portfolios.save()
        return redirect('/portfolio/')
    else:
        return render(request, 'create.html')


def detail2(request, blog_id):
    media_detail = get_object_or_404(Portfolio, pk=blog_id)
    return render(request, 'detail2.html', {'detail':media_detail})

def update2(request, blog_id):
    update2 = get_object_or_404(Portfolio, pk=blog_id)
    
    if request.method == 'POST':
        update2.title = request.POST['title'] #name=title인 애한테 담긴 내용 저장
        update2.body = request.POST['body'] #name=body인 애한테 담긴내용 저장
        update2.photo = request.FILES['photo']
        update2.save()
        return redirect('/portfolio/detail2/'+str(blog_id))

    else: #수정사항을 입력하려고 페이지에 접속하면
        return render(request, 'update2.html', {'update2':update2})

def delete2(request,blog_id):
    delete2=get_object_or_404(Portfolio, pk=blog_id)
    delete2.delete()
    return redirect('portfolio')



