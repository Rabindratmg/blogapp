from django.http import HttpResponse
from django.shortcuts import redirect, render
from accounts.forms import LoginForm, ProfileForms
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from accounts.models import Profile


from posts.models import Post

from django.views.generic import ListView

from .forms import SignUpForm

USER = get_user_model()

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password = form.cleaned_data['password'])
        if user:
            login(request,user)
            return redirect('blogs')
        else:
            return HttpResponse("Your credentials donot match")
    elif request.method=='GET':
        if request.user.is_authenticated:
            return redirect('dashboard')
        form = LoginForm()
    return render(request,'accounts/login.html',{'form':form})
    



def logout_view(request):
    logout(request)
    return redirect('login')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.validate_email()
            form.validate_password()
            user = USER(
            first_name = form.cleaned_data['first_name'],
            last_name = form.cleaned_data['last_name'],
            email = form.cleaned_data['email'],
            username = form.cleaned_data['username'],
            password=form.cleaned_data['password'],
            )
            user.save()
            user.set_password(form.cleaned_data['password']) #use to save hash of password
            user.save()
            return redirect('login')

    elif request.method == 'GET':
        form = SignUpForm()
    
    return render(request,'accounts/signup.html',{'form':form})

@login_required
def dashboard(request):
    userid = request.user
    posts = Post.objects.all().filter(user=userid)
    data = {'posts': posts }
    return render(request,'accounts/dashboard.html',data)

@login_required
def profile(request):
            profileforms = ProfileForms()
            userid= request.user.id
            profile = Profile.objects.get(pk=userid)
            data = {'profile':profile, "profileforms": profileforms }
            return render(request,'accounts/profile.html',data)
   

def editprofile(request,id):
    if request.method == 'POST':
        editforms = ProfileForms(request.POST)
        contact = editforms.GET['contact']
        address = editforms.GET['address']
        bio = editforms.post.GET['bio']
        userprofile = Profile.objects.get(pk=id)
        userprofile.contact = contact
        userprofile.bio = bio
        userprofile.address = address
        return render('profile')
    else:
        return render(request,'accounts/profile.html')