from django.shortcuts import render,redirect
from django.contrib.auth import logout,authenticate, login,update_session_auth_hash
from Product.models import Product,Images,Category,Comment
from EcomApp.models import Setting,ContactMessage,ContactForm
from django.contrib import messages
from UserApp.forms import SignUpForm,UserUpdateForm,ProfileUpdateForm
from UserApp.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.

def user_login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Your UserName or Password is invalid !!')
    category=Category.objects.all()
    setting=Setting.objects.get(id=1)
    context={
        'category':category,
        'setting': setting,
    }
    return render(request,'user_login.html',context)

def user_logout(request):
    logout(request)
    return redirect('home')

def user_register(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password1=form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password1)
            login(request,user)
            current_user=request.user
            data=UserProfile()
            data.user_id=current_user.id
            data.image='user_image/avatar.png'
            data.save()
            return redirect('home')
        else:
            messages.warning(request, 'Your Password is not match !!')
    else:
        form=SignUpForm()
    category=Category.objects.all()
    setting=Setting.objects.get(id=1)
    context={
        'category':category,
        'setting': setting,
        'form':form,
    }
    return render(request,'user_register.html',context)


def userprofile(request):
    category=Category.objects.all()
    setting=Setting.objects.get(id=1)
    current_user=request.user
    profile=UserProfile.objects.get(user_id=current_user.id)
    context={
        'category':category,
        'setting': setting,
        'profile':profile,
    }
    return render(request,'user_profile.html',context)

@login_required(login_url='/user/login')
def user_update(request):
    if request.method=='POST':
        user_form=UserUpdateForm(request.POST,instance=request.user)
        profile_form=ProfileUpdateForm(request.POST,request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your Account has been Update !!')
            return redirect('userprofile')
    else:
        user_form=UserUpdateForm(instance=request.user)
        profile_form=ProfileUpdateForm(instance=request.user)
        category=Category.objects.all()
        setting=Setting.objects.get(id=1)
        context={
        'user_form':user_form,
        'profile_form': profile_form,
        'category':category,
        'setting': setting,
    }
    return render(request,'user_update.html',context)

@login_required(login_url='/user/login')
def user_password(request):
    if request.method=="POST":
        form=PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            messages.success(request, 'Your password Successfully Updated !!')
            return redirect('userprofile')
        else:
            messages.error(request, 'Please Correct the error.<br>' + str(form.errors))
            return redirect('user_password')

    else:
        form=PasswordChangeForm(request.user)
        category=Category.objects.all()
        setting=Setting.objects.get(id=1)
        context={
        'form':form,
        'category':category,
        'setting': setting,
    }
    return render(request,'user_password_update.html',context)



def usercomment(request):
    category=Category.objects.all()
    setting=Setting.objects.get(id=1)
    current_user=request.user
    comment=Comment.objects.filter(user_id=current_user.id)
    context={
        'setting':setting,
        'category':category,
        'comment': comment,
    }
    return render(request,'user_comment.html',context)


def comment_delete(request,id):
    current_user=request.user
    comment=Comment.objects.filter(user_id=current_user.id, id=id)
    comment.delete()
    messages.success(request,'You Comment is successfully Deleted??')
    return redirect('usercomment')
