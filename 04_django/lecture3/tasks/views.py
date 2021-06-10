#from django.http.response import HttpResponse
from django import forms
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


class NewTaskForm(forms.Form):
    task = forms.CharField(label="Description")
    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

# Create your views here.


def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })
    # return HttpResponse("No")


def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            # priority = form.cleaned_data["priority"]
            if request.session["tasks"].count(task) == 0:
                request.session["tasks"] += [task]

            return HttpResponseRedirect(reverse("tasks:index"))

        else:
            return render(request, "tasks/add.html", {
                "form": form
            })

    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })
