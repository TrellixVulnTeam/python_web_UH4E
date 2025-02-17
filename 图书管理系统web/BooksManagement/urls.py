"""BooksManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
# from django.views.generic import TemplateView

import xadmin

from .settings import MEDIA_ROOT
import apps.user.urls
import apps.operation.urls
from django.shortcuts import redirect


def index(request):
    return redirect("/operation/index")


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),  # 指定上传媒体位置
    path('operation/', include((apps.operation.urls, 'operation'), namespace='operation')),
    path('user/', include((apps.user.urls, 'user'), namespace='user')),
    path('', index)
]
