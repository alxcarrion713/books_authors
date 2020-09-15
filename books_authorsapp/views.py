from django.shortcuts import render, HttpResponse, redirect
from . models import Book, Author

# Create your views here.
def index(request):
    return HttpResponse("Its lit")

def index(request):
    context = {
        'allbooks': Book.objects.all()
    }
    return render(request, "index.html", context)

def createbook(request):
    print(request.POST)
    Book.objects.create(title = request.POST['bookName'], description = request.POST['desc'])
    return redirect("/")

def showbook(request, bookid):
    context = {
        'booktoshow': Book.objects.get(id=bookid),
        'allauthors': Author.objects.all()
    }
    
    return render(request,"bookid.html", context)

def addauthor(request, bookid):
    print(request.POST)
    booktojoin = Book.objects.get(id = bookid)
    authorThatjoins= Author.objects.get(id=request.POST['author'])
    authorThatjoins.books.add(booktojoin)
    return redirect(f"/book/{bookid}")