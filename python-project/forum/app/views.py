from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .forms import *

def register_view(req: HttpRequest):
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    return render(req, "register.html", context={'form': UserCreationForm()})

def login_view(req: HttpRequest):
    if req.method == 'POST':
        form = AuthenticationForm(data=req.POST)
        if form.is_valid():
            login(req, form.get_user())
            return redirect("categories")
    return render(req, "login.html", context={'form': AuthenticationForm()})

@login_required(login_url="login")
def logout_view(req):
    logout(req)
    return redirect("login")

@login_required(login_url="login")
def home_view(req):
    return render(req, "discussions.html")

@login_required(login_url="login")
def discussion_create_view(req: HttpRequest):
    if req.method == 'POST':
        form = DiscussionModelForm(req.POST)
        if form.is_valid():
            sub = form.cleaned_data['subject']
            text = form.cleaned_data['text']
            category = form.cleaned_data['category']

            disc = Discussion.objects.create(author=req.user, subject=sub, text=text, category=category)
            disc.save()
            return redirect("discussion", id = disc.id)
        else:
            return render(req, "discussion/discussion_create.html", context={"form": form})

    return render(req, "discussion/discussion_create.html", context={"form": DiscussionModelForm()})


@login_required(login_url="login")
def discussion_edit_view(req: HttpRequest, id:int):
    try:
        disc = Discussion.objects.get(id=id)
        if req.user != disc.author:
            return HttpResponseForbidden()
        
        if req.method == 'POST':
            form = DiscussionModelForm(req.POST)
            if form.is_valid():
                disc.subject = form.cleaned_data['subject']
                disc.text = form.cleaned_data['text']
                disc.category = form.cleaned_data['category']
                disc.save()
                return redirect("discussions")
        return render(req, "discussion/discussion_update.html", context={"form": DiscussionModelForm(instance=disc)})
    except Discussion.DoesNotExist:
        return HttpResponseNotFound()

@login_required(login_url="login")
def discussion_delete_view(req, id):
    try:
        d = Discussion.objects.get(id=id)
        if req.user != d.author:
            return HttpResponseForbidden()
        d.delete()
        return redirect("discussions", id=d.category.id)
    except Discussion.DoesNotExist:
        return HttpResponseNotFound()

def discussions_view(req, id):
    f = req.GET.get("filter")
    d = Discussion.objects.filter(category_id=id).annotate(
        num_likes=Count('likediscussion'),   
        num_comments=Count('comment')     
    )

    if f == "comments":
        d = d.order_by('-num_comments')
    elif f == "likes":
        d = d.order_by('-num_likes')

    return render(req, "discussion/discussions.html",context={'discussions': d})

@login_required(login_url="login")
def discussion_like(req: HttpRequest):
    id = req.GET.get("id")
    next = req.GET.get("next")
    try:
        disc = LikeDiscussion.objects.get(discussion_id=id, user=req.user)
        disc.delete()
    except LikeDiscussion.DoesNotExist:
        LikeDiscussion.objects.create(user=req.user, discussion_id=id).save()
    
    return redirect("discussions" if not next else next, id=id if not next else next)
    
def discussion_view(req, id):
    try:
        d = Discussion.objects.get(id=id)
        c = Comment.objects.filter(discussion_id=id).annotate(
            num_likes=Count('likecomment'),   
        )
        liked = LikeDiscussion.objects.filter(user_id=req.user.id, discussion_id=id).exists()
        c = c.order_by("-num_likes")
        return render(req, "discussion/discussion.html", context={'discussion': d, "comments": c, "comment_form": CommentModelForm(), "has_like": liked})
    except Discussion.DoesNotExist:
        return HttpResponseNotFound()

@login_required(login_url="login")
def comment_create(req: HttpRequest, id):
    if req.method == 'POST':
        Comment.objects.create(author=req.user, text=req.POST.get("text"), discussion_id=id).save()
    return redirect(f"discussion", id=id)

@login_required(login_url="login")
def comment_delete(req: HttpRequest, id):
    discussion_id = None
    try:
        c = Comment.objects.get(id=id)
        if c.author != req.user:
            return HttpResponseForbidden()
        discussion_id = c.discussion.id
        c.delete()
        return redirect(f"discussion", id=discussion_id)
    except Comment.DoesNotExist:
        return HttpResponseNotFound()

@login_required(login_url="login")
def comment_like(req):
    id = req.GET.get("id")
    if not id:
        return HttpResponseBadRequest()
    d_id = None
    try:
        c = LikeComment.objects.get(comment_id=id, user=req.user)
        d_id = c.comment.discussion.id
        c.delete()
    except LikeComment.DoesNotExist:
        c = LikeComment.objects.create(user=req.user, comment_id=id)
        c.save()
        d_id = c.comment.discussion.id

    return redirect(f"discussion", id=d_id)

@login_required(login_url="login")
def favorites_view(req):
    f = LikeDiscussion.objects.filter(user=req.user)
    for i in f:
        print(i.discussion)
    return render(req, "discussion/favorites.html", context={"discussions": f})


def categories_view(req:HttpRequest):
    c = Category.objects.all()
    return render(req, "category/categories.html", context={"categories": c})


def author_view(req, author_id):

    a = User.objects.get(id=author_id)
    d = Discussion.objects.filter(author_id=author_id)
    return render(req, "author/author.html", context={"discussions": d, "author": a})