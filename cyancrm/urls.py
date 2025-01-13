from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include

from core.views import index
from userprofile.views import signup

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/leads/', include('lead.urls')),
    path('dashboard/clients/', include('client.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('sign-up/', signup, name='signup'),
    path('login-in/', views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('log-out/', views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]
