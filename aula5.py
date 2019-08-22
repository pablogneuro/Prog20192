''''
lista = []
print (lista)


lista = ["carro", "peixe", 111, 2333]
print (lista)
novaLista = ["pedra", lista]
print (novaLista)
print(lista[2])
print(lista[-2])
print(len(lista))
print(len(novaLista))
print(lista+novaLista)
print(lista*3)
print("peixe"in lista)
if(not("carro"in lista)):
    print("sou ric:")
else:
    print("sou pobre: ~")

vetorDeNumeros = [14.55,67,89,10,21.5]
print(min(vetorDeNumeros))
print(max(vetorDeNumeros))
print(sum(vetorDeNumeros))

livros = ["Java", "SqlServer", "Delphi", "Python"]
livros.append ("Android")
print(livros)
livros.insert(0, "Oracle")
print(livros)
livros.pop(1)
print(livros)
livros.remove("Delphi")
print(livros)
listaDeNumeros= [66.25, 333,-1, 3333,1,]
print(listaDeNumeros.index(333))

livros = ["Java", "SqlServer", "Delphi", "Python", "Java"]
livros.sort()
print(livros)
livros.reverse()
print(livros)
print(livros.count("Java"))
'''

'''a = [33,33,33]
b = [33,33,33]
print(a == b)
print(a is b)
b[0]= 3
print (a)
b = a
b[0] = 3
print(a)

a = [33,33,33]
b = a [:]
b[0]
print(a)

tupla = (1,2,3,4);print (tupla)
tupla = (1,);print (tupla)
tupla = ();print(tupla)

tupla = ("Maria", "João", "Carlos")
print(tupla[0])
print(tupla [0:2])

p = "python"
print (p[0:0])
print (p[0:1])
print (p[1:2])
print (p[0:3])
print (p[0:4])

'''

agenda = {}
print (agenda)
agenda = {"Maria":[863636333, 35353637,]}
print(agenda)
print (agenda ["Maria"])
agenda = {"Maria":[863636333, 35353637,], "Pedro": [3476564446565]}
print(agenda["Pedro"])