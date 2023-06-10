from django.shortcuts import render
from django.http import (HttpResponse,
                         HttpResponseNotFound,
                         HttpResponseRedirect)
from django.urls import reverse


answers = {
    'monday': 'Сегодня понедельник',
    'tuesday': 'Сегодня вторник',
    'wednesday': 'Сегодня среда',
    'thursday': 'Сегодня четверг',
    'friday': 'Сегодня пятница',
    'saturday': 'Сегодня суббота',
    'sunday': 'Сегодня воскресенье',
}

people = [
    'Жукова Анна Константиновна',
    'Юлия Степановна Потапова',
    'Гущин Аполлинарий Тимурович',
    'Дорофей Ярославович Третьяков',
    'Селезнева Анна Тарасовна',
    'Федотов Симон Харлампьевич',
    'Красильникова Вера Борисовна',
    'Бажен Тихонович Костин',
    'Веселова Анжелика Тимофеевна',
    'Щербаков Самсон Феодосьевич'
]

def number_day(request, day):
    return render(request, 'week_days/greeting.html')


def list_todo(request, day):
    return render(request, 'week_days/greeting.html')


def get_people(request):
    context = {
        'people': people,
    }
    return render(request, 'week_days/people.html', context=context)
