from django.shortcuts import render

from mainapp.models import Product

links_menu = [
    {'href': 'index', 'name': 'Домой', 'route': ''},
    {'href': 'products:index', 'name': 'Продукты', 'route': 'products/'},
    {'href': 'about', 'name': 'О&nbsp;нас', 'route': 'about/'},
    {'href': 'contacts', 'name': 'Контакты', 'route': 'contacts/'},
]


def index(request):
    title = 'главная страница'

    products_ = Product.objects.all()

    context = {
        'title': title,
        'links_menu': links_menu,
        'products': products_,
    }

    return render(request, 'index.html', context)
    # return render(request=request, template_name='index.html', context=context)


def about(request):
    title = 'о нас'

    context = {
        'title': title,
        'links_menu': links_menu,
    }

    return render(request, 'about.html', context)


def contacts(request):
    title = 'контакты'

    context = {
        'title': title,
        'links_menu': links_menu,
    }

    return render(request, 'contact.html', context)
