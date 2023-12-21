from django.shortcuts import render

def index(request):
    """ Pagina Principal do AppAprendiado"""

    return render(request, 'AppAprendizado/index.html')
