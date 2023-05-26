from django.shortcuts import render
from datetime import date, timedelta

def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['hello', 'bye', 'lol', 'kek'],
        'obj': {
            'age': '18',
            'name': 'Vova',
            'pet': 'dog'
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')

