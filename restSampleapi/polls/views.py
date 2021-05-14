from django.http import HttpResponse
"test rest deployment"

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")