from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': ' Лев - <i>пятый знак зодиака</i>, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}


def index(request):
    res = ''
    for key in zodiac_dict.keys():
        url = reverse("horoscope-name", args=[key])
        res += f'<li><h2><a href={url}>{key}</a></h2></li>'
    return HttpResponse(f"<ol> {res} </ol>")

def answer_for_sign(request, sign_zodiac: str):
    answer = zodiac_dict.get(sign_zodiac)
    if answer:
        return HttpResponse(f"<h1>{answer}</h1>")
    else:
        return HttpResponseNotFound(f"<h1>{sign_zodiac} - Несуществующий знак зодиака</h1>")


def answer_for_int(request, sign_zodiac: int):
    if 0 < sign_zodiac < 13:
        sign = list(zodiac_dict)[sign_zodiac - 1]
        redirect_url = reverse("horoscope-name", args=[sign])
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound(f"<h1>{sign_zodiac} - Несуществующий знак зодиака</h1>")
