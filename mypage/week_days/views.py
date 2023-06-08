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
    if 0 < day < 8:
        day = list(answers)[day - 1]
        redirect_url = reverse("day_of_week", args=[day])
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound(f"{day} - нет такого дня")


def list_todo(request, day):
    answer = answers.get(day)
    if answer:
        return HttpResponse(answer)
    return HttpResponseNotFound(f"{day} - нет такого дня")
