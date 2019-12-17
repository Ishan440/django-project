from django.shortcuts import render, redirect
from django.contrib import messages
# ^ for flash messages to show success or some kind of one time sign
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import redirect, render
# Create your views here.


def register(request):
    """
    Django’s login form is returned using the POST method, in which the browser bundles up the
    form data, encodes it for transmission, sends it to the server, and then receives back its response.
    :param request:
    :return:
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)  # if post request is received, then a form will be made with that data.
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')  # fstring is basically str.format()
            return redirect('blog-home')
    else:
        messages.error(request, "nope")
        form = UserCreationForm()  # Create an instance of the user registration form. blank form.

    return render(request, 'users/register.html', {'form': form})
