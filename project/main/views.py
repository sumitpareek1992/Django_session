from django.shortcuts import render
from main.forms import DepatmentForm, StudentForm
from main.models import Students


# Create your views here.


def index(request):
    info = Students.objects.all()
    print(info)
    return render(request,"index.html", {"info":info})

def department_view(request):
    msg = ""
    if request.method == "POST":
        form = DepatmentForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "department saved successfully"
        else:
            msg = form._errors
    form = DepatmentForm()
    return render(request, "department.html",
                  {"form": form, "msg": msg})
def student_view(request):
    msg = ""
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "student saved successfully"
        else:
            msg = form._errors
    form = StudentForm()
    return render(request, "student.html",
                  {"form": form, "msg": msg})
