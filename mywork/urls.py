from django.contrib import admin
from django.urls import path, include
from mywork.views import *

app_name = 'mywork'

urlpatterns = [
    path('create/', ProductCreateView.as_view()),
    path('all/', ProductListView.as_view()),
    path('detail/<int:pk>/', ProductDetailView.as_view()),
]