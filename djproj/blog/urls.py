"""djproj URL Configuration

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
from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-home'),
    # for class based our path must be of format: app/model_typeofview.html. But we can specify template path in
    # our view class.
    # empty path name means home page, for others, do admin/ or store/.
    # view.home mean exec home function in view file.
    # name is the name for this path. used blog-home to not confuse with other webapps' homes.
    path('about/', views.about, name='blog-about'),
    # the trailing slash at the end ensures that django redirects paths without a / also to that route.
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    # different urls for diff posts are determined by the post's primary key (pk). we spec int type.
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete')
]
