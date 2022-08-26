from django.urls import path
from profiles import views

# The code taken from the Code Institute drf-api project
urlpatterns = [
    path('profiles/', views.ProfileList.as_view()),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view()),
]