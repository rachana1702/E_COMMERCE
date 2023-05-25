from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'index.html')

def home1(request):
    return render(request,'home1.html')
    
def contact(request):
    return render(request,'contact.html')
 
 
def product(request):
    return render(request,'product.html')

def about(request):
    return render(request,'about.html')
    
def choco(request):
    return render(request,'chocolate.html')

    
def gdgts(request):
    return render(request,'gadgets.html')

    
def bgs(request):
    return render(request,'bags.html')
    
def register(request):
    if request.method == 'POST':
        if User.objects.filter(username=request.POST['uname']).exists():
            print('Username already taken')
            return(request,"register.html")
        else:
            u=User.objects.create_user(username=request.POST['uname'],first_name=request.POST['fname'],last_name=request.POST['lname'],password=request.POST['pass1'])
            u.save()
            
            return redirect('/')
    else:
        return render(request,'register.html')
 

 
def logout(request):
    auth.logout(request)
    return redirect('/')
 

 
def login(request):
    if request.method == 'POST':
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            print('Invalid username and password')
            return redirect('/login')
            
    else:
        return render(request,'login.html')
        
