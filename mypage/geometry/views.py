import math

from django.shortcuts import render
from django.http import HttpResponse


def get_rectangle_area(request, width, height):
    # return HttpResponse(f"Площадь прямоугольника {width}х{height} равна {width * height}")
    return render(request, 'geometry/rectangle.html')


def get_square_area(request, width):
    # return HttpResponse(f"Площадь квадрата размером {width}x{width} равна {width ** 2}")
    return render(request, 'geometry/square.html')


def get_circle_area(request, radius):
    # return HttpResponse(f"Площадь круга радиуса {radius} {math.pi * radius ** 2:.2f}")
    return render(request, 'geometry/circle.html')
