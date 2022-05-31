from django.shortcuts import render


def index(request):
    title = 'главная страница'

    context = {
        'title': title,
    }

    return render(request, 'index.html', context)
    # return render(request=request, template_name='index.html', context=context)


def about(request):
    return render(request, 'about.html')


def contacts(request):
    return render(request, 'contact.html')
