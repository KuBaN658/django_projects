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


def number_day(request, day):
    return render(request, 'week_days/greeting.html')


def list_todo(request, day):
    return render(request, 'week_days/greeting.html')
