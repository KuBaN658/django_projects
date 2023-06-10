from django.urls import path
from . import views

urlpatterns = [
    path('people_details', views.get_people_details),
    path('people', views.get_people),
    path('<int:day>', views.number_day),
    path('<str:day>', views.list_todo, name="day_of_week"),
]
