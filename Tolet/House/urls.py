

from django.urls import path
from .import views
from .views import Postcreateview

urlpatterns = [
    path('home/', views.homepage),
    path('home/new', views.Postcreateview.as_view()),
]
