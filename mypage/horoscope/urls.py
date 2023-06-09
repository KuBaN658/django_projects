from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'year')
register_converter(converters.SplitConvertor, 'wordlist')

urlpatterns = [
    path('', views.index),
    path('type', views.choose_type),
    path('<year:sign_zodiac>', views.get_year),
    path('<int:month>/<int:day>', views.get_sign),
    path('<int:sign_zodiac>', views.answer_for_int),
    path('type/<str:type>', views.get_type, name="type-name"),
    path('<str:sign_zodiac>', views.answer_for_sign, name="horoscope-name"),
    path('<wordlist:lst>', views.get_lst),
]
