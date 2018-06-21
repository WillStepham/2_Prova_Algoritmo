#Questão 1
def troque(l):
    y=len(l)//2
    z=len(l)
    for x in range(0,y):
        aux=l[x]
        l[x]=l[z-1]
        l[z-1]=aux
        z-=1
    return l

l=[1,4,7,2,5,8,3,6,9,0,12,45,78,23,56,89,13,46,79,14]
print("Lista inicial: {}".format(l))
print("Lista modificada: {}".format(troque(l)))
