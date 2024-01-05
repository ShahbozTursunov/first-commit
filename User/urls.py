from django.urls import path
from .views import *

urlpatterns = [
    path('register/',RegView.as_view()),
    path('order/',OrderView.as_view()),
    path('update/<int:id>/',UpdateView.as_view()),
    path('order_list/<int:pk>/',OrderListView.as_view()),
    path('user_list/',UserListView.as_view()),
    path('user_delete/<int:id>/',UserDeleteView.as_view()),
    path('Login/',LogView.as_view()),
]