import sys

def menu2():
    tab = []
    linhas = int(input("Digite o número de linhas\r\n:"))
    colunas = int(input("Digite o número de colunas\r\n:"))
    tab = geraMatriz(tab, linhas,colunas)
    imprimiMatriz(tab)
def geraMatriz(a = [], linhas = int, colunas = int):
    n = 0
    p = 0
    k = 1
    while(p < linhas):
        a.append([])
        while(n < colunas):
            k += 1
            a[p].append(str(k-1))
            n = n+1
        p = p +1
        n = 0

    return a
def imprimiMatriz(a=[]):
    b = 0
    while (b < len(a)):
        print(a[b])
        b += 1
def menu():
    sair = input("Deseja gerar?\r\nR:")
    if(sair == 's'  ):
        menu2()
    else:
        sys.exit()
menu()
