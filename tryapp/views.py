from django.shortcuts import render,redirect
from .models import newtable
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def list(request):
    values = newtable.objects.all()
    return render(request,'posts/list.html',{"value":values})

def agepage(request,val):
    post = newtable.objects.get(name = val)
    return render(request,'posts/page.html',{"value":post})

@login_required(login_url='/users/login/')
def newpost(request):
    if request.method =="POST":
        form = forms.createpost(request.POST,request.FILES)
        if form.is_valid():
            np = form.save(commit=False)
            np.author = request.user
            np.save()
            return redirect("tryapp:listurl")
    else:
        form = forms.createpost()
    return render(request,'posts/newpost.html',{'form':form})
    