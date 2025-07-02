from django.urls import path
from . import views

urlpatterns = [
    path('', views.memo_list, name='memo_list'),
    path('<int:id>/', views.memo_detail, name='memo_detail'),
    path('create/', views.memo_create, name='memo_create'),
    path('<int:id>/edit/', views.memo_edit, name='memo_edit'),
    path('<int:id>/delete/', views.memo_delete, name='memo_delete'),
]
