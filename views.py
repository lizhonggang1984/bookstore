from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader, RequestContext
from booktest.models import BookInfo,HeroInfo
from datetime import date
# Create your views here.

def index(request):
    books = BookInfo.objects.all()
    return render(request,'booktest/books.html',{'books':books})

def create(request):
    book = BookInfo()
    book.btitle = 'liuxinghudiejian'
    book.bpub_date = date(1990,1,1)
    book.bcomment = 15
    book.bread = 10
    book.save()
    return HttpResponseRedirect('/index')

def delete(request,bid):
    book = BookInfo.objects.get(id=bid)
    book.delete()
    return HttpResponseRedirect('/index')