from django.shortcuts import render, redirect
from .forms import SignUpForm, ProfileUpdateForm, AboutUpadateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .models import Post, Blogger
from django.contrib.auth.models import User
from django.core.paginator import Paginator


# Create your views here.
@login_required
def home(request):
    all_post = Post.objects.filter().order_by('-posted_on')

    pagination = Paginator(all_post, 10)
    page_no = request.GET.get('page')
    page_obj = pagination.get_page(page_no)
    context = {'posts': page_obj}
    return render(request, 'blog/home.html', context)


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'Account created for {username}! Login to continue')
            new_user = User.objects.filter(username=username).first()
            new_blogger = Blogger(user=new_user)
            new_blogger.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form': form})


class AddPost(CreateView):
    model = Post
    template_name = 'blog/add_post.html'
    fields = ['title', 'post']

@login_required
def full_post(request, pk):
    if request.method == "POST":
        blogger = Blogger.objects.filter(user=request.user).first()
        title = request.POST['title']
        post = request.POST['post']
        new_post = Post(blogger=blogger, title=title, post=post)
        new_post.save()
        return render(request, 'blog/full_post.html', {'post': new_post})
    else:
        post = Post.objects.filter(pk=pk).first()
        context = {'post': post}
        return render(request, 'blog/full_post.html', context)

@login_required
def profile(request):
    blogger = Blogger.objects.filter(user=request.user).first()
    if request.POST:
        print(request.POST)
        name = request.POST['updateprofile']
        print(name)
        if name == "1":
            p_form = ProfileUpdateForm(request.POST, request.FILES, instance=blogger)    
            if p_form.is_valid():
                p_form.save()
                messages.success(request, 'Profile Pic Updated')
        elif name == "2":
            u_form = AboutUpadateForm(request.POST, instance=blogger)
            if u_form.is_valid():
                u_form.save()
                messages.success(request, 'About Updated')
    
    u_form = AboutUpadateForm()
    p_form = ProfileUpdateForm()
    posts = Post.objects.filter(blogger=blogger)
    count_post = len(posts)
    context = {'posts': posts, 'blogger': blogger, 'p_form': p_form, 'u_form': u_form, 'count_post': count_post}
    return render(request, 'blog/profile.html', context)


def search(request):
    if request.method=='GET':
        query=request.GET['query']
        user1=User.objects.filter(username=query).first()
        blogger=Blogger.objects.filter(user=user1).first()
        posts = Post.objects.filter(blogger=blogger)
        count_post = len(posts)
        context = {'posts': posts, 'blogger': blogger,'count_post': count_post}
        return render(request, 'blog/search.html', context)
