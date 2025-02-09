import random


carac = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%()&1234567890'
senhasSalvas = []

'''
def pegaQtdTam():
    
    qtd = int(input("Quantas senhas você quer que sejam geradas?"))
    tam = int(input("Qual o tamanho das senhas você quer que sejam geradas?"))
    
    return [qtd,tam]
'''

def geradorDeSenha(dados):

    listaSenhas = []

    for l in range(dados[0]):
        senha = ''
        for s in range(dados[1]):
            senha += random.choice(carac)
        listaSenhas.append(senha)

    return listaSenhas


def mostraLista(listaSenhas):
    for L in range(len(listaSenhas)):
        print(f"{L+1} - {listaSenhas[L]}")
    slc = int(input("Qual das senhas você quer salvar?"))
    try:
        senhasSalvas.append(listaSenhas[slc-1])
        print(f"Parabéns!!! Você salvou a senha {slc}")
        print(senhasSalvas)
    except Exception as e:
        print("Senha fora da lista!")
        mostraLista(listaSenhas)
'''
print("Bem vindo ao gerador de senhas!!")
dados = pegaQtdTam()
print("Suas senhas estão sendo geradas!")
listaDeSenhas = geradorDeSenha(dados)
'''




