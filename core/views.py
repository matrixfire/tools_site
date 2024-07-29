from django.shortcuts import render
from .models import BlogPost
from django.http import Http404, HttpResponse
import time

from django.http import JsonResponse


# Create your views here.
def index1(request):
    post = BlogPost.objects.first()
    return render(request, 'core/index1.html', {"post": post})



# Create your views here.
def index2(request):
    return render(request, "core/index2.html")

# The texts are much longer in reality, but have
# been shortened here to save space
texts = ["Text 1", "Text 2", "Text 3"]

def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num - 1])
    else:
        raise Http404("No such section")
    



# Create your views here.
def index3(request):
    return render(request, "core/index3.html")

def posts(request):

    # Get start and end points
    start = int(request.GET.get("start") or 0)
    end = int(request.GET.get("end") or (start + 9))

    # Generate list of posts
    data = []
    for i in range(start, end + 1):
        data.append(f"Post #{i}")

    # Artificially delay speed of response
    time.sleep(1)

    # Return list of posts
    return JsonResponse({
        "posts": data
    })