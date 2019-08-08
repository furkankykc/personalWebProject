from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.utils import timezone

from blog.models import Post


def getBlog(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    print("posts",posts)
    return render(request, 'blog/index.html', locals())


def getPost(request,id):
    post = get_object_or_404(Post, pk=id)
    print(post)
    return render(request,'blog/post_detail.html',locals())