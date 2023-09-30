from django.http import HttpResponse
from .models import Students, Teacher
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import StudentForm, SubjectForm


class HomeTemplate(TemplateView):
    template_name = 'home.html'


class AboutUs(TemplateView):
    template_name = 'first_app/about_us.html'


def detail_view(request):
    print(request.method)

    if request.method.lower() == "get":
        form = SubjectForm()
        context = dict()
        context["students_data"] = Students.objects.all()
        context["form"] = form
        return render(request, 'first_app/about_us.html', context)

    if request.method.lower() == "post":
        print("post method got")
        form = SubjectForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # name = form.cleaned_data
            form.save()
            return HttpResponse("Thanks form is saved")
        else:
            return HttpResponse("Thanks form is not valid")
