from django.urls import path
from RepoA.add_users.views import AddUserView, sample_view

urlpatterns = [
    path('add-user/', AddUserView.as_view(), name='add-user'),
    path('sample-A/', sample_view, name='sample-view'),

]
