from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create_book, name='create'),
    path('register', views.register, name='create'),
    path('httpheaders', views.httpheaders, name='httpheaders'),

    # 自定义转换器
    # 有时候Django自带的转换器不能满足业务需求，
    # 如验证电话号码是否符合格式，此时的<int: phone>已经不能满足需求，需要自定义
    # 1. 新建converters.py文件(bookmanager/book/utils/converters.py)
    # 2. 在converters.py文件中实现验证手机号码的代码
    # 3. 在"项目名/urls.py"下对自定义的路由转换器进行注册
        # from book.utils.converters import MobileConverter
        # register_converter(MobileConverter, 'mobile')
    # 4. 使用自定义路由转换器
    path('<mobile:phone_num>', views.validphone, name="validphone"),
    path('setcookie', views.set_cookie, name="setcookie"),
    path('getcookie', views.get_cookie, name="getcookie"),
    path('setsession', views.set_session, name="setsession"),
    path('getsession', views.get_session, name="getsession"),

    #####################################################
    path('register_view', views.RegisterView.as_view(), name="register_view"),

]
