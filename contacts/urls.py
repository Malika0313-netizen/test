from contacts.views import TaskList, TaskDetail
from django.urls import path
from django.contrib import admin
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', TaskList.as_view()),
    path('contacts/list/', ListAPIView.as_view()),
    path('contacts/create/', CreateAPIView.as_view()),
    path('contacts/update/', UpdateAPIView.as_view()),
    path('contacts/delete/', DestroyAPIView.as_view()),
    path('contacts/delete/<int:pk>', DestroyAPIView.as_view()),
    path('contacts/detail/<int:pk>', TaskDetail.as_view()),

]



