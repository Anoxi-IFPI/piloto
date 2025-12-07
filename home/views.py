from django.shortcuts import render, HttpResponse 


def index(request):
    return render(request, 'base.html')

def sobre(request):
    return render(request,"sobre.html")

def contato(request):
    return render(render, "contato.html")

def ajuda(request):
    return render(request, "ajuda.html")

def exibir_item(request, id):
    return render(request, "exibir_item.html", {"id":id})

def perfil(request, usuario):
    return render(request, 'perfil.html', {'usuario':usuario})

def diasemana(request, numero):
    
    dias_map = {
        1: 'Domingo',
        2: 'Segunda-feira',
        3: 'Terça-feira',
        4: 'Quarta-feira',
        5: 'Quinta-feira',
        6: 'Sexta-feira',
        7: 'Sábado'
    }

    resultado = dias_map.get(numero, 'Dia inválido')

    return render(request, 'diasemana.html', {'dia': resultado})