from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    if request.method == 'POST':
        un=request.POST['username']
        pas=request.POST['password']
        user=auth.authenticate(username=un,password=pas)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method== 'POST':
        un=request.POST['username']
        fn = request.POST['first_name']
        ln = request.POST['last_name']
        em = request.POST['email']
        pas = request.POST['password']
        cpas = request.POST['password1']
        if pas==cpas:
            if User.objects.filter(username=un).exists():
                messages.info(request,"Username taken")
                return redirect('register')
            elif User.objects.filter(email=em).exists():
                messages.info(request,"Username taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=un, password=pas, first_name=fn, last_name=ln, email=em)
                user.save();
                return redirect('login')

        else:
            messages.info(request,"password not matched")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')