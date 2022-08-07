

from django.urls import path
from apps.home import views
urlpatterns = [
    # The home pages
    path('', views.index, name='home'), 
]
