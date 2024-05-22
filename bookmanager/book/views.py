from django.shortcuts import render
from django.http import HttpResponse

from .models import BookInfo, PeopleInfo


def index(request):

    return HttpResponse("OK")

