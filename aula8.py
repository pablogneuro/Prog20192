'''
arquivo = open ("pablo.txt", "w") 
arquivo.write ("Eu sou Pabl")
arquivo.write ("Eu sou PabloG")
arquivo.write ("Eu sou PabloQ")



arquivo.close()
arquivo = open ("pablo.txt", "r")
print(arquivo.read())



arquivo = open ("pablo.txt", "w")
linhasDoTexto = ["acertos Tempo Barra", "10 20 esq"
                    "10 20m esq"]
arquivo.writelines(linhasDoTexto)
arquivo.close ()
arquivo = open ("pablo.txt", "r")
for linha in arquivo:
    print(linha)
arquivo.close()
'''


import csv

with open("pablo.csv", "w", newline= '') as arquivoCSV:
    spamWriter = csv.writer(arquivoCSV, delimiter = '',
    quotechar=  '', quoting = csv.QUATE_MINIMAL)

    spamWriter.writerow(["Ola"]*5 + ["mundo"])