from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Post
from .forms import PostForm

# Create your views here.

def index(req):
    if not req.user.is_authenticated:
        return render(req, 'index.html', {'page_title': 'Music Ratings'})
    else:
        return redirect('app_:posts')

@login_required
def posts(req):
    tmp = Post.objects.all()
    return render(req, 'posts.html', {'posts': tmp})


@login_required
def post(req, id):
    tmp = get_object_or_404(Post, id=id)
    return render(req, 'post.html', {'post': tmp, 'page_title': tmp.title})


@permission_required('app_.change_post')
def edit(req, id):
    if req.method == 'POST':
        form = PostForm(req.POST)

        if form.is_valid():
            a = Post.objects.get(id=id)
            a.title = form.cleaned_data['title']
            a.content = form.cleaned_data['content']
            a.save()
            return redirect('app_:posts')
        else:
            return render(req, 'edit.html', {'form': form, 'id': id})
    else:
        a = Post.objects.get(id=id)
        form = PostForm(instance=a)
        return render(req, 'edit.html', {'form': form, 'id': id})


@permission_required('app_.add_post')
def new(req):
    if req.method == 'POST':
        form = PostForm(req.POST)

        if form.is_valid():
            a = Post(title=form.cleaned_data['title'], content=form.cleaned_data['content'], owner=req.user)
            a.save()
            return redirect('app_:posts')
        else:
            return render(req, 'new.html', {'form': form})
    else:
        form = PostForm()
        return render(req, 'new.html', {'form': form})

@permission_required('app_.delete_post')
def delete(req, id):
        a = Post.objects.get(id=id)
        a.delete()
        tmp = Post.objects.all()
        return render(req, 'posts.html', {'posts': tmp})
