from django.shortcuts import render, redirect
from .models import Book
# Create your views here.
def index(request):
    b = request.user.book_set.all()
    context = {
        "bset" : b
    }
    return render(request, "book/index.html", context)

def create(request):
    if request.method == "POST":
        bn = request.POST.get("bname")
        bu = request.POST.get("burl")
        bc = request.POST.get("bcon")
        im = bool(request.POST.get("impo"))
        Book(site_name=bn, site_url=bu, site_con=bc, impo=im, user=request.user).save()
        return redirect("book:index")
    return render(request, "book/create.html")