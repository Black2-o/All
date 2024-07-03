from django.shortcuts import render
from .models import *
import requests
from django.db.models import Q

def homePage(request):
    return render(request, 'pages/index.html')


def booksPage(request, pk):
    re_id= pk
    className= Classes.objects.get(pk= pk)
    books= className.books_set.all()
    context={
        're_id': re_id,
        'books': books,
    }
    return render(request, 'pages/books.html', context)




def classPage(request):
    classList = Classes.objects.all()

    context={
        'list': classList,
    }
    print(classList[0])
    return render(request, 'pages/class.html', context )


def chapterPage(request, pk, bpk):
    re1_id= pk
    re2_id= bpk
    className= Classes.objects.get(pk= pk)
    books= className.books_set.get(pk=bpk)
    chapters= books.chapter_set.all()
    context={
        're1_id': re1_id,
        're2_id': re2_id,
        'chapters': chapters,
    }
    return render(request, 'pages/chapter.html', context)

# def singleClassPage(request, cpk, bpk, chpk):
def singleClassPage(request, url):
    # className= Classes.objects.get(pk=cpk)
    # books= className.books_set.get(pk=bpk)
    # chapters= books.chapter_set.get(pk=chpk)
    video= url
    print(video)
    context={
        "video": video,
    }
    return render(request, 'pages/singleclass.html', context)





def chatPage(request):
    context={}
    return render(request, 'pages/chat.html', context)

def booksPage(request):
    books = BookPdf.objects.all()
    if request.method == 'POST':
        quary= request.POST.get('search')
        books= BookPdf.objects.filter(Q(name__icontains=quary))

    context={
        'books': books,
    }
    return render(request, 'pages/readbook.html', context)

def singleBookPage(request):
    context={}
    return render(request, '', context)



def helloworld(request):
    return render(request, 'temp.html')


from django.http import JsonResponse

def reset_api(request):
    # Logic to handle the API request
    response_data = {'message': 'Hello, World!'}
    return JsonResponse(response_data)


