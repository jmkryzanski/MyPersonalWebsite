from django.shortcuts import redirect, render
from .models import Post, Profile
from .forms import PostForm, ProfileForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'website/home.html')

def about(request):
    return render(request, 'website/about.html')

# display the main blog page
def myblog(request):
    posts = Post.objects.all()
    form = PostForm()
    context = {
        'posts': posts,
        'form': form,
    }
    return render(request, 'website/myblog.html', context)

# display invidiual blog posts
def myblog2(request, id):
    post = Post.objects.get(id=id)
    form = PostForm()
    if id > 0:
        context = {
            'form': form,
            'post': post,
        }
    else:
        context = {
            'form': form,
            'post': post,
        }

    return render(request, 'website/myblog2.html', context)

def addPost(request):
    form = PostForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('myblog')

    context = {'form': form}
    return render(request, 'website/addPost.html', context)

def updatePost(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('myblog')
        else:
            form = PostForm(instance=post)

    context = {
        'form': form,
        'post': post,
    }

    return render(request, 'website/updatePost.html', context)

def deletePost(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('myblog')

    context = {
        'post': post,
    }
    return render(request, 'website/myblog.html', context)

def contact(request):
    return render(request, 'website/contact.html')

def viewProfile(request):
    profile = Profile.objects.all()
    form = ProfileForm()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('website/myblog.html')

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'website/viewProfile.html', context)

@login_required
def profile(request):
    return render(request, 'website/profile.html')

@login_required
def editProfile(request):
    profile = Profile.objects.all()
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        form.actual_user = request.user
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm()

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'website/editProfile.html', context)

