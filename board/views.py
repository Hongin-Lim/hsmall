from django.shortcuts import render

# Create your views here.

def base (request):
    return render(request, 'layout/base.html')

def hsmall (request):
    return render(request, 'board/hsmall.html')

