from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


zodiac_dict = {
    'aries': ['Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
              'Огонь', (3, 21), (4, 20)],
    'taurus': ['Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
               'Земля', (4, 21), (5, 21)],
    'gemini': ['Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
               'Воздух', (5, 22), (6, 21)],
    'cancer': ['Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
               'Вода', (6, 22), (7, 22)],
    'leo': ['Лев - <i>пятый знак зодиака</i>, солнце (с 23 июля по 21 августа).',
            'Огонь', (7, 23), (8, 21)],
    'virgo': ['Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
              'Земля', (8, 22), (9, 23)],
    'libra': ['Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
              'Воздух', (9, 24), (10, 23)],
    'scorpio': ['Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
                'Вода', (10, 24), (11, 22)],
    'sagittarius': ['Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
                    'Огонь', (11, 23), (12, 22)],
    'capricorn': ['Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
                  'Земля', (23, 12), (1, 20)],
    'aquarius': ['Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
                 'Воздух', (1, 21), (2, 19)],
    'pisces': ['Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
               'Вода', (2, 20), (3, 20)],
}

types = {
    'Fire': ['aries', 'leo', 'sagittarius'],
    'Earth': ['taurus', 'virgo', 'capricorn'],
    'Air': ['gemini', 'libra', 'aquarius'],
    'Water': ['cancer', 'scorpio', 'pisces'],
}


class Zodiac:
    def __init__(self, name: str, text: str, group: str):
        self.name = name
        self.text = text
        self.group = group

zodiacs = (Zodiac(zodiac[0], zodiac[1][0], zodiac[1][1]) for zodiac in zodiac_dict.items())


def index(request):
    res = ''
    for key in zodiac_dict.keys():
        url = reverse("horoscope-name", args=[key])
        res += f'<li><h2><a href={url}>{key}</a></h2></li>'
    return HttpResponse(f"<ol> {res} </ol>")


def answer_for_sign(request, sign_zodiac: str):
    response = render_to_string('horoscope/info_zodiac.html')
    return HttpResponse(response)


def answer_for_int(request, sign_zodiac: int):
    if 0 < sign_zodiac < 13:
        sign = list(zodiac_dict)[sign_zodiac - 1]
        redirect_url = reverse("horoscope-name", args=[sign])
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound(f"<h1>{sign_zodiac} - Несуществующий знак зодиака</h1>")


def choose_type(request):
    response = ''
    for key in list(types):
        url = reverse("type-name", args=[key])
        response += f'<li><a href={url}>{key}</a></li>'
    return HttpResponse(f'<ul>{response}</ul>')


def get_type(request, type):
    response = ''
    for zodiac in types[type]:
        url = reverse("horoscope-name", args=[zodiac])
        response += f'<li><a href={url}>{zodiac}</a></li>'
    return HttpResponse(f'<ul>{response}</ul>')


def get_sign(request, month, day):
    if 0 >= month or month > 12 or day <= 0 or day > 31:
        return HttpResponseNotFound(f"<h1>Некорректные данные</h1>")
    for sign in zodiac_dict.items():
        if month == sign[1][2][0] and day >= sign[1][2][1]:
            redirect_url = reverse("horoscope-name", args=[sign[0]])
            return HttpResponseRedirect(redirect_url)
        elif month == sign[1][3][0] and day <= sign[1][3][1]:
            redirect_url = reverse("horoscope-name", args=[sign[0]])
            return HttpResponseRedirect(redirect_url)


def get_year(request, sign_zodiac: int) -> HttpResponse:
    return HttpResponse(f"{sign_zodiac} - валидный год")


def get_lst(request, lst: list):
    return HttpResponse(f'{lst} - список слов')
