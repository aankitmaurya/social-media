from django import forms
from .models import Subject


class StudentForm(forms.Form):
    first_name = forms.CharField(label="First name", max_length=100)
    qualification = forms.CharField(label="qualification", max_length=100)


class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = ["name"]
