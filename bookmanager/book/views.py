import json

from django.shortcuts import render
from django.http import HttpResponse

from .models import BookInfo, PeopleInfo


def index(request):
    # book = BookInfo.objects.get(id = 1)
    # book = book.peopleinfo_set.all()
    # print("get:", book)
    # # book = BookInfo.objects.filter(name__icontains='湖')
    # book = BookInfo.objects.exclude(id__in=[1, 2, 3])
    # print("exclude:", book)
    return HttpResponse("ok")


def create_book(request):
    book = BookInfo.objects.create(name='百年孤独', pub_time='1981-03-12', readcount=10)
    book.save()
    return HttpResponse('create')
