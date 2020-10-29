from django.shortcuts import render, redirect
from account.forms import RegisterForm
from django.contrib.auth import logout


# Create your views here.
def home_view(request):
    return render(request, 'home.html')


def register_view(request):
    msg = ""
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return redirect('s_view')
        else:
            msg = "Login Failed"
    form = RegisterForm()
    return render(request, 'register.html', {'form': form, 'msg': msg})


def logout_view(request):
    logout(request)
    return redirect('home')

