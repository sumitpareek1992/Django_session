from django import forms
from main.models import Department, Students


class DepatmentForm(forms.ModelForm):
    class Meta():
        model = Department
        fields = "__all__"

class StudentForm(forms.ModelForm):
    class Meta():
        model = Students
        fields = ['s_id', 'name', 'email', 'd_name', 'age', 'image']

