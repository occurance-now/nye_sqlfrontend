"""djangoMSSQL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from usersapp import views as user_views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^',include('mssqlFrontEnd.urls')),
    path('', auth_views.LoginView.as_view(template_name='authenticate/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='authenticate/logout.html'), name='logout'),
    path('', include('usersapp.urls')),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
