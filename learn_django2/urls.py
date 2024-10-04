"""
URL configuration for learn_django2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve

from app1 import views
from app1.views import depart, user, number, admin, account, order, chart, upload

urlpatterns = [
    # path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

    # 部门管理
    path('depart/list', depart.depart_list),
    path('depart/add', depart.depart_add),
    path('depart/del', depart.depart_del),
    path('depart/<int:nid>/edit', depart.depart_edit),
    path('depart/multi', depart.depart_multi),

    # 用户管理
    path('user/list', user.user_list),
    path('user/add', user.user_add),
    path('user/<int:nid>/edit', user.user_edit),
    path('user/<int:nid>/del', user.user_del),

    # 靓号管理
    path('number/list', number.number_list),
    path('number/add', number.number_add),
    path('number/<int:nid>/edit', number.number_edit),
    path('number/<int:nid>/del', number.number_del),

    # 管理员管理
    path('admin/list', admin.admin_list),
    path('admin/add', admin.admin_add),
    path('admin/<int:nid>/edit', admin.admin_edit),
    path('admin/<int:nid>/del', admin.admin_del),
    path('admin/<int:nid>/reset', admin.admin_reset),

    path('login', account.login),
    path('logout', account.logout),

    path('order/list', order.order_list),
    path('order/add', order.order_add),
    path('order/delete', order.order_del),
    path('order/detail', order.order_detail),
    path('order/edit', order.order_edit),

    path('chart/list', chart.chart_list),
    path('chart/line', chart.chart_line),
    path('chart/bar', chart.chart_bar),
    path('chart/pie', chart.chart_pie),

    path('upload/list', upload.upload_list),
    path('upload/form', upload.upload_form),
    path('upload/model/form', upload.upload_model_form)
]
