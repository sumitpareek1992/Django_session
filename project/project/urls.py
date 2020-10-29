"""project URL Configuration

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
from django.urls import path, re_path
from main.views import index, department_view, student_view, home_view,department_list
from django.views.generic import UpdateView, DeleteView, ListView
from main.models import Students, Department

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('department/', department_view, name='department'),
    path('student/', student_view, name='student'),
    re_path('s_update/(?P<pk>[0-9]+)', UpdateView.as_view(
        model= Students,
        fields="__all__",
        success_url= "/",
        template_name="students_update_form.html"
    )),
    re_path("s_delete/(?P<pk>[0-9]+)",DeleteView.as_view(
        model=Students,
        success_url="/",
        template_name="student_confirm_delete.html"
    )),
    path('d_list/', department_list, name='d_list'),
    re_path('d_update/(?P<pk>[0-9]+)', UpdateView.as_view(
        model=Department,
        fields="__all__",
        success_url="/d_list",
        template_name="department_update_form.html"
    )),
    re_path("d_delete/(?P<pk>[0-9]+)", DeleteView.as_view(
        model=Department,
        success_url="/d_list",
        template_name="department_confirm_delete.html"
    )),
]
