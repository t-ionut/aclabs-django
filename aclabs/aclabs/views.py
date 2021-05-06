from django.http import HttpResponse


def hello_world(request):
    response = HttpResponse('<h1>Hello <a href="https://google.com/" target="_blank">World!</a></h1>')
    return response