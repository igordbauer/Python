from django.contrib import admin
from django.urls import path
from .views import home ,save, getObject, update, delete

urlpatterns = [
    path('', home),
    path('core/save/',save, name='save'),
    path('core/getObject/<int:id>', getObject, name = 'getObject'),
    path('core/update/<int:id>', update, name = 'update'),
    path('core/delete/<int:id>', delete, name = 'delete')
]