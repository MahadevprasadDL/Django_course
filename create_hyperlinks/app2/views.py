from django.http import HttpResponse


def next_page(request):
    return HttpResponse ('<a href="/app1/index"> App1 </a>')