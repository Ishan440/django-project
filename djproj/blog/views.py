from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    """
    :param request: this page was requested
    :return: http response upon taking the requested route i.e. the view of the page
    """
    # return HttpResponse('<h1> Blog Home </h1>'). We'll return a template instead using render:
    return render(request, 'blog/home.html')
    # django looks into the templates folder by default.


def about(request):
    """
    :param request: this page was requested
    :return: http response upon taking the requested route i.e. the view of the page
    """
    # return HttpResponse('<h1> Blog about </h1>')
    return render(request, 'blog/about.html')