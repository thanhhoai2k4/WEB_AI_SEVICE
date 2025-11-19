from django.urls import path
from . import views # Import file views.py cùng thư mục

urlpatterns = [
    path('', views.Home, name='Home_View'),
    path("yolo/", views.yolo_detect_view, name="yolo_detect"),
    path("learning_dataset/", views.Learning_Dataset, name="learning_dataset")
]