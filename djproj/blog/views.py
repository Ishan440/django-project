from django.shortcuts import render
from django.http import HttpResponse


# dummy info to pass to templates so that our pages have dynamic views.
posts = [
    {'author': 'Ishan', 'content': 'First blog post', 'date': 'Dec 13'},
    {'author': 'NOT Ishan', 'content': 'First blog post', 'date': 'Dec 15'}
]

# Create your views here.

def home(request):
    """
    :param request: this page was requested
    :return: http response upon taking the requested route i.e. the view of the page
    """
    context = {'posts': posts}
    # return HttpResponse('<h1> Blog Home </h1>'). We'll return a template instead using render:
    return render(request, 'blog/home.html', context)
    # django looks into the templates folder by default.
    # context will be passed to our template; key name post will be used to access our posts data.


def about(request):
    """
    :param request: this page was requested
    :return: http response upon taking the requested route i.e. the view of the page
    """
    # return HttpResponse('<h1> Blog about </h1>')
    return render(request, 'blog/about.html', {'title': 'title for about page'})
