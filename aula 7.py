'''def mensagemDeErro():
    """Não retorna nada,mas mostra na tela uma mensagem clássica"""
    print("Infelizmente você terá que começar tudo de novamente")
    print("Nada do que você está certo!")

mensagemDeErro()


def soma(x,y):
    return x+y 

primeiroParametro = int (input("Digite o primeiro numero:"))
segundoParametro  = int (input("Digite o segundo numero:"))

y = soma(primeiroParametro,segundoParametro)
print(y)


def arbitrary(x,y, *more):
    """ Função com dois  ou mais parametros"""
    print("x = ", x, "y = ", y)
    print("Parametros arbitrários:", more)

arbitrary(2,3)
arbitrary(2,3, "oi", "xau")


def nomesPaises(Paises = "Noruega"):
    print("Eu vim da:", Paises)
nomesPaises("Venezuela")
nomesPaises()


def listaDeComidas(comidas):
    """ Programa para imprimir a lista de comidas passadas"""
    for comida in comidas:
        print(comida)

listaDeComidas(["Banana", "Maça", "Pera", "Abacaxi"])


def recursao(k):
    if(k > 0):
        resultado = k + recursao (k-1)
        print(resultado)

    else:
        resultado = 0
    return resultado

recursao(6)
'''
