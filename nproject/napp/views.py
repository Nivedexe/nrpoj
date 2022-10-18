from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Profile
# Create your views here.


def demo(request):
    n=Place.objects.all()
    p=Profile.objects.all()
    return  render(request,'index.html',{'result':n,'new':p})

# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     s=x-y
#     d=x/y
#     m=x*y
#     return render(request,'result.html',{'addition':res,'subtraction':s,'division':d,'multiplication':m})
#
# def about(request):
#     return  render(request,'result.html')
