from django.shortcuts import render
from .forms import StudentForm
from .models import Student
# Create your views here.
def home(request):
    form=StudentForm()
    msg="registration"
    if request.method=="POST":
        form=StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            msg="successful" 
        else:
            msg="fill again"
    return render(request,'home.html',{'form':form,'msg':msg})


def show(request):
    data1=Student.objects.all()
    data=data1.values()
    return render(request,'show.html',{'data':data}) 