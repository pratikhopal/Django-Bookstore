from os import read
from django.shortcuts import get_object_or_404, render
from books.models import Review, book
from django.http import Http404
from django.shortcuts import redirect




def index(request):
    dbData=book.objects.all()
    context={'books':dbData}
    return render(request, 'books/index.html',context)


def show(request,id):
    singlebook=get_object_or_404(book,pk=id)  
    reviews=Review.objects.filter()
    context={'book':singlebook,'reviews':reviews}
    return render(request, 'books/show.html',context)


def review(request):
    body=request.POST['review']
    newreview=Review(body=body)
    newreview.save()
    return redirect('/books')