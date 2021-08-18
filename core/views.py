from django.shortcuts import render #, redirect -> opção de redirecionamento
from core.models import Evento
# Create your views here.

# opção de redirecionamento
#def index(request):
#    return redirect('/agenda/')

def tituloEvento(request, titulo_evento):
    return Evento.objects.get(titulo = titulo_evento)

def lista_eventos(request):
    # Para mostrar os agendamentos de acordo com a autenticação do usuario:
#    usuario = request.user
#    evento = Evento.objects.filter(usuario=usuario)

# Força o programa a exibir os agendamentos gerais mesmo sem login
    evento = Evento.objects.all()
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)