

# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import BOOKLET
from django.contrib.auth.decorators import login_required
from .forms import BookletForm

# Create your views here.
def home(request):
   
    return render(request,"BOOKLET/index.html")

def signin(request):
    if request.method=="POST": 
        username=request.POST.get("username")
        pass1=request.POST.get("pass1")
        user = authenticate( request,username=username,password=pass1)
        print(username)
        print(pass1)
        if user is not None:
            login(request,user)
            
            
            # //messages.success(request,"logged in successfully")
            return redirect('page2')
            
        else:
            messages.error(request,"bad credentials") 
            return redirect('home')   


    return render(request,"BOOKLET/signin.html")  

def signup(request):

    if request.method=="POST":
        username=request.POST.get('username')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        email=request.POST.get('email')
       
        
        if User.objects.filter(username=username):
            messages.error(request,"username already exist!! try other")
            return redirect('home')
        if pass1!=pass2:
            messages.error(request,"confirm password again!")
            return redirect('home')
        if len(username)>10:
            messages.error(request,"username must be less than 10 characters!")
            return redirect('home')   
        if not username.isalnum:
            messages.error("username must be alpha-numeric!")
            return redirect('home')

        myuser=User.objects.create_user(username=username,email=email,password=pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()

        # messages.success(request,"your account has been successfully created")

        return redirect('signin')

    return render(request,"BOOKLET/signup.html")



def signout(request):
    logout(request) 
    messages.success(request,"logged out successfully!")  
    return redirect('home')
  


@login_required
def page2(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            if 'delete' in request.POST:
                booklet_id= request.POST.get('booklet.id')
                
                
                booklet = BOOKLET.objects.get(id=booklet_id)
                booklet.delete()
                return redirect('page2')
        booklets = BOOKLET.objects.all()
   
        return render(request, 'BOOKLET/admin.html', {'booklets': booklets})
    else:
        admin_user = User.objects.get(is_superuser=True)
        # admin_user = request.user  # Adjust this as per your requirement
        booklets = BOOKLET.objects.all()
        
        return render(request, 'BOOKLET/normal.html', {'booklets': booklets})

@login_required
def add_booklet_view(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = BookletForm(request.POST, request.FILES)
            if form.is_valid():
                BOOKLET = form.save(commit=False)
                BOOKLET.uploaded_by = request.user
                BOOKLET.save()
                return redirect('page2')
        else:
            form = BookletForm()
        return render(request, 'BOOKLET/add.html', {'form': form})
    else:
        return redirect('page2')        

def delete(request,id):
    dele=BOOKLET.objects.get(id=id)
    dele.delete()
    return redirect('page2')