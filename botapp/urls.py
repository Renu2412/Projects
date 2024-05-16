from django.urls import path

from botapp.views import Home

urlpatterns = [path('',Home.as_view(),name = 'home'),
               ]
