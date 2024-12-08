from django.urls import path
from .views import AddUserView, sample_view

urlpatterns = [
    path('add-user/', AddUserView.as_view(), name='add-user'),
    path('sample-A/', sample_view, name='sample-view'),

]
