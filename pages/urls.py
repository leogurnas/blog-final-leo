from django.urls import path
from . import views
from .views import PageCreateView, PageUpdateView

urlpatterns = [
    path('', views.page_list, name='page_list'),
    path('<int:pk>/', views.page_detail, name='page_detail'),
    path('about/', views.about, name='about'),
]
urlpatterns += [
    path('create/', PageCreateView.as_view(), name='page_create'),
    path('edit/<int:pk>/', PageUpdateView.as_view(), name='page_edit'),
]
