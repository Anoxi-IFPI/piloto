from django.shortcuts import render, HttpResponse, redirect
from .forms import ContatoForm
from .forms import ProdutoForm



def index(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request,"sobre.html")

def contato(request):
    form = ContatoForm()
    contexto = {
        'form': form,
        }
    return render(request, "contato.html", contexto)

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

#produtos
def produtos(request):
    contexto = {
        'lista': [
            {'id': 1, 'nome': 'Notebook', 'preco': '2.500,00'},
            {'id': 2, 'nome': 'Monitor', 'preco': '500,00'},
            {'id': 3, 'nome': 'Teclado', 'preco': '80,00'},
            {'id': 4, 'nome': 'Mouse', 'preco': '40,00'},
            {'id': 5, 'nome': 'Impressora', 'preco': '600,00'},
            {'id': 6, 'nome': 'Scanner', 'preco': '700,00'},
            {'id': 7, 'nome': 'Câmera Web', 'preco': '150,00'},
            {'id': 8, 'nome': 'Headset', 'preco': '120,00'},
            {'id': 9, 'nome': 'Pendrive 32GB', 'preco': '30,00'},
            {'id': 10, 'nome': 'HD Externo 1TB', 'preco': '350,00'},
            {'id': 11, 'nome': 'Estabilizador', 'preco': '200,00'},
            {'id': 12, 'nome': 'Switch 8 portas', 'preco': '180,00'},
            {'id': 13, 'nome': 'Roteador Wi-Fi', 'preco': '220,00'},
        ],
    }
    return render(request, 'produto/lista.html',contexto)

#Formulario de produtos
def form_produto(request):
    form = ProdutoForm()
    contexto = {
        'form': form,
        }
    return render(request, "produto/formulario.html", contexto)


def detalhes_produto(request, id):
    return render(request, "Botoes/detalhes.html", {'id':id})

def editar_produto(request, id):
    return render(request, "Botoes/editar_produto.html", {'id':id})

def excluir_produto(request, id):
    # Se o usuário clicou no botão "Sim, excluir" do formulário
    if request.method == "POST":
        # AQUI entraria o código para apagar do banco de dados.
        # Exemplo real seria: Produto.objects.get(id=id).delete()
        
        print(f"Produto {id} excluído com sucesso!") # Apenas para testar no terminal
        
        # Após excluir, redireciona de volta para a lista de produtos
        return redirect('produto')

    # Se for apenas o acesso à pagina (GET), mostra a pergunta
    return render(request, "Botoes/excluir_produto.html", {'id': id})