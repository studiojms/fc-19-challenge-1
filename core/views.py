from django.shortcuts import render

from core.models import Post


# Create your views here.
def blog_index(request):
    posts = Post.objects.all().order_by("-created_at")
    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context)
