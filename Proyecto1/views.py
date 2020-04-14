from django.http import HttpResponse

def saludo(request): #primera vista
    return HttpResponse("p2r")


def chau(request): #primera vista
    return HttpResponse("prueba2")