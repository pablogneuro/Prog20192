'''
print ('Hello World')
nome = input ('Qual seu nome?')
print ('Prazer te conhecer,',nome)
n1= int(input ('Digite uma nota:'))
n2= int(input ('Digite uma nota:'))
m= (n1+n2)/2
print('A média é igual a', m)
varString= " JP"
print (varString)
print (type(varString))
varInt = 1
print (varInt)

varFoat = 1.1
print (varFoat)

varBool = True #False
print(varBool)
'''

#import math
'''
from math import sqrt
print(sqrt(100))
'''
#print (2**2)
'''
var1= 2
var1 += 56
print (var1)

a,b,c =  2,4,8
a,b,c = a*2, a+b+c, a*b*c
print(a,b,c)
'''
'''
peso = float(input('Digite seu peso em (kg):'))
altura = float(input('Digite sua altura em (cm):'))
imc = (peso/altura*altura)
print = (imc)
'''

'''
alturaFloat= 1.74
pesoFloat= 64.0

imc = pesoFloat/(alturaFloat**2)

print(imc)

print ('Muito abaixo do peso?', imc < 17.0)
print ('Abaixo do peso normal?', imc >= 17.0 and imc <= 18.5)
print ('Peso dentro do normal?', imc > 18.5 and imc <= 25.5)
print ('Acima do normal?', imc >= 25.0 and imc <=30.0)
print ('Muito acima do normal?', imc > 30.0 )
'''

print ('Programa para calcular IMC')

altura = input ('Digite sua altura (em m):')
peso = input ('Digite seu peso (em kg):')

imc = float(peso)/(float(altura)**2)
print (imc)


if imc < 17.0: 
    print('Muito abixo do peso!')
elif imc >= 17.0 and imc <= 18.5:
    print('Abaixo do peso normal!')
elif imc > 18.5 and imc <= 25.5:
    print ('Peso dentro do normal!')
elif imc >= 25.0 and imc <=30.0:
    print ('Acima do normal!')
else: 
    print ('Muito acima do normal!')
