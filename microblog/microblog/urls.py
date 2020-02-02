"""microblog URL Configuration

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
from django.contrib import admin
from django.urls import path

from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView

# リクエスト-> urls.py -> views -> テンプレート -> レスポンス -> ユーザー

urlpatterns = [
    # path('<url>', views(関数), ニックネーム)
    # http://localhost:8000/
    # int 整数 pk=int
    path('create', BlogCreateView.as_view(), name="create"),
    path('<int:pk>/update', BlogUpdateView.as_view(), name="update"),
    path('detail/<int:pk>', BlogDetailView.as_view(), name="detail"),
    path('', BlogListView.as_view(), name='index'),
    path('admin/', admin.site.urls),
]
