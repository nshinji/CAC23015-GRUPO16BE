from django.http import HttpResponse
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render

def saludo(request):
    documento= """<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <h1> ZARAXA</h1>
        </body>
        </html> """
    return HttpResponse(documento)

def op_site(request):
    return render(request,"index.html")

def nic_site(request):
    return render(request,"nico.html")