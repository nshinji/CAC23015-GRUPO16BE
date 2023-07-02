from django.http import HttpResponse
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