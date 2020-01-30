from django.shortcuts import render
from django.http import HttpResponse
from . models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)


# Create your views here.

""" Function based views for home and about"""
def home(request):
    """
    :param request: this page was requested
    :return: http response upon taking the requested route i.e. the view of the page
    """
    context = {'posts': Post.objects.all()}
    # return HttpResponse('<h1> Blog Home </h1>'). We'll return a template instead using render:
    return render(request, 'blog/home.html', context)
    # django looks into the templates folder by default.
    # context will be passed to our template; key name post will be used to access our posts data.


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # by default, django will look in app/model_typeofview.html .
    context_object_name = 'posts'  # specify what you want to be iterated for the list based view.
    ordering = ['-date']  # order post view from latest to oldest (hence the minus) as we scroll down.


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    "Classes can't use decorators so we inherit the mixin to create post only when someone is looged in."
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):  # override the form validation
        form.instance.author = self.request.user  # create a post with author as the current logged in user.
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    "The UserPasses mixin checks if the person trying to update the post is the actual author of the post"
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):  # override the form validation
        form.instance.author = self.request.user  # update a post with author as the current logged in user.
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()  # get the post we're current;y trying to update.
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = 'blog/'  # if post is deleted successfully redirect to blog home.

    def test_func(self):
        post = self.get_object()  # get the post we're current;y trying to update.
        if self.request.user == post.author:
            return True
        return False


def about(request):
    """
    :param request: this page was requested
    :return: http response upon taking the requested route i.e. the view of the page
    """
    # return HttpResponse('<h1> Blog about </h1>')
    return render(request, 'blog/about.html', {'title': 'title for about page'})

