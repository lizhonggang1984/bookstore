from django.conf.urls import url
from booktest import views
from django.urls import include,path,re_path

urlpatterns = [
    path('',views.login_ajax),
    path('index',views.index),
    path('index2',views.index2),
    path('index3',views.index3),
    path('child',views.child),

    path('books',views.books),
    path('create',views.create),
    re_path(r'^delete(\d+)$',views.delete),
    path('areas', views.areas), # 自关联案例
    re_path(r'^showArg(\w+)$',views.showArg),
    re_path(r'^login$',views.login),
    re_path(r'^login_check$',views.login_check),
    re_path(r'^login_ajax$',views.login_ajax),
    re_path(r'^login_ajax_check$',views.login_ajax_check),

    # path('set_cookie', views.set_cookie),
    # path('get_cookie', views.get_cookie),

    # path('set_session', views.set_session),
    # path('get_session', views.get_session),

    path('ajax_test',views.ajax_test),
    path('ajax_handle',views.ajax_handle),
]

