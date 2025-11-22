# user/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),

    # Sử dụng Class-based view có sẵn của Django giúp tiết kiệm thời gian viết code lặp lại
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),

    # Logout trong Django 5.x yêu cầu POST request để bảo mật, nhưng ta có thể dùng view sẵn
    # Chúng ta sẽ xử lý nút bấm ở template sau.
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]