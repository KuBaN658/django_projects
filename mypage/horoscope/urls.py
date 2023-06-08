from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('<int:sign_zodiac>', views.answer_for_int),
    path('<str:sign_zodiac>', views.answer_for_sign, name="horoscope-name"),
]