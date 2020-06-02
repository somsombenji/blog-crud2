"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import blogapp.views
import portfolio.views
#미디어 만들때 꼭 임포트할 것. 외우기
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', blogapp.views.home, name="home"),
    path('blog/<int:blog_id>', blogapp.views.detail, name="detail"),
    path('blog/create/', blogapp.views.create, name="create"),
    path('update/<int:blog_id>',blogapp.views.update, name="update"),
    path('delete/<int:blog_id>', blogapp.views.delete, name="delete"),
    path('portfolio/', portfolio.views.portfolio, name="portfolio"),
    path('portfolio/new/', portfolio.views.create2, name="create2"),
    path('portfolio/detail2/<int:blog_id>', portfolio.views.detail2, name="detail2"),
    path('portfolio/update2/<int:blog_id>', portfolio.views.update2, name="update2"),
    path('portfolio/delete2/<int:blog_id>', portfolio.views.delete2, name="delete2"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #미디어 url설계 (외우자)
