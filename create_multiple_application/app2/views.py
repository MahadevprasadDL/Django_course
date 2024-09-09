from django.http import HttpResponse


def next_page(request):
    return HttpResponse (" this is second app")