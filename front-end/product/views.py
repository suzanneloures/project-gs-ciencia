from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader



def index(request):
    data_from_api = {
        "name": "Cama",
        "description": "Cama de Madeira com 4 pes",
        "value": "5400.00",
    }
    context = {
        'data': data_from_api,
    }
    return render(request, 'index.html',data_from_api)