"""blogs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from blog.views import index2
from blog.views import IndexView, ArichiveView, TagView, TagDetailView, BlogDetailView
from blog.views import AddCommentView, CategoryDetaiView, MySearchView
from blog.feeds import BlogRssFeed
# from blogs.settings import STATIC_ROOT
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('blog/', index),
    path('blog2/', index2),
    path('blog/', IndexView.as_view(), name='index'),
    path('', IndexView.as_view(), name='index'),
    path('archive/', ArichiveView.as_view(), name='archive'),
    path('tags/', TagView.as_view(), name='tags'),
    path('tags/(?P<tag_name>\w+)', TagDetailView.as_view(), name='tag_name'),
    path('blog/(?P<blog_id>\d+)', BlogDetailView.as_view(), name='blog_id'),
    path('add_comment/', AddCommentView.as_view(), name='add_comment'),
    path('rss/', BlogRssFeed(), name='rss'),
    path('category/(?P<category_name>\w+)/', CategoryDetaiView.as_view(), name='category_name'),
    path('search/', MySearchView(),  name='haystack_search'),
    # 添加静态文件的访问处理函数
    # path('static/(?P<path>.*)/', serve, {'document_root': STATIC_ROOT}),
]
