from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'templates.html')
    # return HttpResponse ('<b>This is Home buddy <b/>')

def insta(request):
    # return render(request, 'templates.html')
    return HttpResponse ('<b>This is Home buddy <b/>')