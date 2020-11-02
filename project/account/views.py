from django.shortcuts import render, redirect, HttpResponse
from account.forms import RegisterForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required


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
            return redirect('home')
        else:
            msg = form._errors
    form = RegisterForm()
    return render(request, 'register.html', {'form': form, 'msg': msg})
@login_required
def logout_view(request):
    logout(request)
    return redirect('home')






def login_view(request):
    msg = ""
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return redirect('s_view')

        else:
            msg = "Login Failed"
    return render(request, 'login.html', {'msg':msg})