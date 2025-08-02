from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': "Home - Главная",
        'content': "Магазин мебели HOME"
        
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': "Home - О нас",
        'content': "О нас",
        'text_on_page': "Восхваление магазина!"
        
    }

    return render(request, 'main/about.html', context)


def contacts(request):
    context= {
        'title': "Home - Наши контакты",
        'content': "Наши контакты",
        'text_on_page': ['Телефон: 8-800-555-35-35',
                         'Telegram: @prodam_vse',
                         'Email: prodam_vse@home.com'
                        ]

    }

    return render(request, 'main/contacts.html', context)


def delivery(request):
    context= {
        'title': "Home - Доставка и оплата",
        'content': "Доставка и оплата",
        'text_on_page': "Когда доставим, тогда доставим. Вы не платите - мы не продаём"

    }

    return render(request, 'main/delivery.html', context)
