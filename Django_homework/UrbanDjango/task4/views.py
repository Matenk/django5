from lib2to3.fixes.fix_input import context
from django.shortcuts import render
from django.template.defaultfilters import title

def main(request):
    title = 'Главная страница'
    text = 'Главная страница магазина'

    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'fourth_task/main.html', context)

def games(request):

    context = {
        'games': ['Spider-man', 'GTA 3', 'Dota 2']

    }
    return render(request, 'fourth_task/games.html', context)

def basket(request):
    title = 'Корзина'
    text = 'Игры в корзине'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'fourth_task/basket.html', context)



