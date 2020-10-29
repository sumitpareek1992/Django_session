from django.shortcuts import render, redirect
from main.forms import DepatmentForm, StudentForm
from main.models import Students, Department


# Create your views here.

def index(request):
    info = Students.objects.all()
    one = Students.objects.all().first()
    two =  Students.objects.get(s_id=2)
    three = Students.objects.filter(name="ravi")
    for i in three:
        print(i)
    print(three)
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
            return redirect('s_view')
        else:
            msg = form._errors
    form = StudentForm()
    return render(request, "student.html",
                  {"form": form, "msg": msg})
def department_list(request):
    lst = Department.objects.all()
    return render(request, 'department_list.html', {"lst":lst})
