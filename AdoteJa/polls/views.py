from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')

def pag2(request):
    return render(request, 'pages/pag2.html')