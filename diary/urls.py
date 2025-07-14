from django.urls import path
from diary import views as mytodo

urlpatterns = [
    path("", mytodo.index,name="index"),
]