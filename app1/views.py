# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from app1.models import Emp
from app1.form import ef
# Create your views here.

def em(r):
    data=Emp.objects.all()
    return render(r,"home.html",{'data':data})


def emp_f(r):
    form=ef()
    if r.method=="POST":
        form=ef(r.POST)
        if form.is_valid():
            form.save()
            return redirect("rec")

    return render(r,"new.html",{'form':form})