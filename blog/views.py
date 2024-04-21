# render function of the views looks for HTML templates in a directory named templates/ inside your app directory
# templates of different apps can have the same names so it's BP to add a subdirectory with the app's name inside the templates/ directory
from django.shortcuts import render

# custom imports to this project
from django.http import HttpResponseRedirect
from blog.models import Post, Comment
from blog.forms import CommentForm

# a Queryset is a collection of all the objects in the database that match the query

# results in a Queryset containing all the posts in the database
def homepage(request):
    # .order_by arranges the results, the minus starts the result at the largest value
    # or in this case the most recent
    posts = Post.objects.all().order_by("-created_on")

    # context defines context dictionary which populates the render function
    # this can also be sent as an object within the render()
    context = {
        "posts": posts,
    }

    # renders the home.html template with the populated context content
    return render(request, "main/home.html", context)

# results in a Queryset containing all the posts in the database, this is sending to an alt template for more control
def posts(request):
    posts = Post.objects.all().order_by("-created_on")

    context = {
        "posts": posts,
    }

    return render(request, "main/posts.html", context)

# pk = primary key which returns a single post that has the requested pk to then pull it's comments
def post(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": CommentForm(),
    }

    return render(request, "main/post.html", context)


def category(request, category):
    # .filter is Django Queryset filter to set conditions to retrieve results
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")

    # context dictionary to send into template
    context = {
      "category": category,
      "posts": posts,
    }

    # renders the category.html with the context dictionary
    return render(request, "main/category.html", context)

