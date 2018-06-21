#Questão 4
def troca(s,v,n):
    r=''
    for i in s:
        if i is v:
            r+=n
        else:
            r+=i
    return r

print(40*'=')
s=str(input('Digite uma frase: '))
v=str(input('Digite uma letra para ser trocada: '))
n=str(input('Digite a nova letra: '))
print(40*'=')
print('Frase: {}'.format(s))
print('Trocar: {} por {}'.format(v,n))
print('Resultado: {}'.format(troca(s,v,n)))
print(40*'=')
print()
