from django.shortcuts import render,redirect
from .forms import RegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from blog.models import Post



# Create your views here.
def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f"acccount is created of {username}")
            return redirect('login')
    
    else:
        form=RegisterForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    if request.method=='POST':
        
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f"profile is updated ")
            return redirect('profile')

    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    user=request.user
    posts=Post.objects.filter(author=user)
    context={'u_form':u_form,'p_form':p_form,'posts':posts}

    
    return render(request,'users/profile.html',context)

