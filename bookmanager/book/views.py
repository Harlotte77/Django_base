import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from rest_framework.views import APIView

from .models import BookInfo, PeopleInfo


def index(request, phone_num):
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


@csrf_exempt
def register(request):
    data = request.POST
    print(data)
    return HttpResponse("ok")


def httpheaders(request):
    print(request.META['SERVER_PORT'])
    return HttpResponse("ok")


def validphone(request, phone_num):
    print(phone_num)
    print(type(phone_num))
    return HttpResponse("ok")


"""
第一次请求的时候，我们手动添加查询字符串: ?username=zhangsan&password=123456
http://127.0.0.1:8000/book/set_cookie/?username=zhangsan&password=123456
服务器接收到请求之后，获取username和password。服务器设置cookie信息，cookie信息中包含username和password
浏览器接收到服务器的响应之后，应该把cookie保存起来

第二次及其之后的请求，访问http://127.0.0.1:8000/时，都会携带cookie信息。服务器就可以读取到cookie信息
判断用户是否合法以及是否需要重新登录
"""


# 设置cookie
def set_cookie(request):
    # 1. 获取查询字符串的信息
    username = request.GET.get("username")
    password = request.GET.get("password")
    # 2. 服务器设置cookie信息
    # 通过响应对象.set_cookie信息进行设置
    response = HttpResponse("set_cookie")
    response.set_cookie("name", username)
    response.set_cookie("pwd", password)
    return response


def get_cookie(request):
    # 获取cookie
    # 方式1：
    print("META:", request.META.get('HTTP_COOKIE', ''))
    # 方式2：
    print(request.COOKIES.get("name"))
    print(request.COOKIES.get("pwd"))

    return HttpResponse("get_cookie")


"""
第一次请求http://127.0.0.1:8000/book/set_session/?username=zhangsan的时候，我们在服务器端设置session信息
服务器同时会生成一个sessionid的cookie信息
浏览器接收到这个信息之后，会把cookie数据保存起来

第二次及其之后的请求，都会携带这个sessionid，服务器会验证sessionid
验证没问题会读取相关数据，实现业务逻辑
"""


def set_session(request):
    """
    模拟
    """
    # 1. 获取用户信息
    username = request.GET.get("username")
    # 2. 设置session信息
    # 假设通过数据库模型查询到了用户信息
    user_id = 1
    request.session['user_id'] = user_id
    request.session['username'] = username
    return HttpResponse("set_session")


def get_session(request):
    # 方式1
    # user_id = request.session['user_id']
    # username = request.session['username']
    # print("方式1：",user_id, username)

    # 方式2
    user_id = request.session.get('user_id')
    username = request.session.get('username')
    print("方式2：",user_id, username)
    """
    方式2的健壮性比方式1要好
    当找不到user_id或者username时，方式1会报错，
    而方式2会返回None
    """
    return HttpResponse("get_session")


class RegisterView(LoginRequiredMixin, View):
    def get(self, request):
        print(request.GET.get("username"))
        return HttpResponse("get_view")
    def post(self, request):
        return HttpResponse("post_view")


