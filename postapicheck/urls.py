from django.urls import path
from . import views
urlpatterns = [
    path('', views.CheckPost.as_view(), name="checkvalid")
]