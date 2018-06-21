#Questão 2
from math import sqrt

def maior(l):
    maior=l[0]
    for i in l:
        if i>maior:
            maior=i
    return maior

def menor(l):
    menor=l[0]
    for i in l:
        if i<menor:
            menor=i
    return menor

def media(l):
    soma=0
    for i in l:
        soma+=i
    media=soma/len(l)
    return media

def desvio(l):
    m=media(l)
    soma=0
    for i in l:
        soma+=(i-m)**2
    desvio=sqrt(soma/len(l))
    return desvio

l=[1,4,7,2,5,8,3,6,9,0,12,45,78,23,56,89,13,46,79,14,25,36,47,58,69]
print("Maior: {} => Posição: {}".format(maior(l),l.index(maior(l))))
print("Menor: {} => Posição: {}".format(menor(l),l.index(menor(l))))
print("Média: {}".format(media(l)))
print("Desvio padrão: {:.4}".format(desvio(l)))
