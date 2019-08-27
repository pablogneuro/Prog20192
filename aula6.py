'''for i in range(10):
    print(i)

for i in range(9,-2,-3):
    print(i)


for char in ("trabalho na quinta"):
    print(char)

for i in range(9, -1,-1):
    print(i)


listaDeNomes = ['Pedro','João', 'Leticia']

for nome in listaDeNomes:
    print (nome)


linguagens = ['Python','PHP', 'C#','PowerBuilde','Cobol']
tamanho    = len(linguagens)
indices     = range(5)
for i in indices: 
    print(linguagens[i])


for key, value in enumerate(["P", "Y", "T", "H", "O", "N." ]):
    print (key,value)


linguagens = ['Python','PHP', 'C#','PowerBuilde','Cobol']
for key, value in enumerate(linguagens):
    print ("A linguagem e:", value)
    print ("O rank da linguagem e:", key)


from numpy import random

listaValores = random. rand(20)
for value in listaValores:
    print(value)


lista1 = ["q","w","e","r"]
lista2 = ["i", "u","y","t"]
for v1,v2 in zip(lista1,lista2):
    print(v1,v2)

listaDeNomes = ["A", "B", "C"]
for nome in listaDeNomes:
    print(nome)
else:
    print("Todos os nomes foram listados!")


contador = 0
while contador <= 5:
    print(contador)
    decisão = int(input("O macaco tocou a barra:"))
    if (decisão):
        contador = contador +1
print ("Segue para proxima etapa")

decisao = True
while decisao:
    decisão = int(input("O macaco aprendeu a etaapa 1:"))
    print(decisao)
else:
    print("Não aprendeu")

count = 0
while count <=5:
    print(count)
    count +=1
    if count >3: break

'''
count = -1
while count < 5:
    count +=1
    if count ==3: continue
    print(count)
print("FIM de programa")