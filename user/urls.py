from django.urls import path
from .views import HelloWordView

urlpatterns=[
    path('hello/',HelloWordView.as_view(),name='Hello-devetechnologies')
]