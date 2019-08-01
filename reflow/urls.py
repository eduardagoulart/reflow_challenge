"""reflow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import reflow.core.views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', reflow.core.views.signup, name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), {'next_page': '/'}, name='logout'),
    path('user_details/', reflow.core.views.user_details, name='user_details'),
    path('index/see_all/<str:email>/', reflow.core.views.see_everything, name='see_all'),
    path('index/see_all/<str:email>/edit/', reflow.core.views.edit, name='edit'),
    path('index/see_all/<str:email>/delete/', reflow.core.views.delete, name='delete'),
    path('success/', reflow.core.views.success, name='success'),
    path('index/', reflow.core.views.home, name='home'),
]
# user_id>/
