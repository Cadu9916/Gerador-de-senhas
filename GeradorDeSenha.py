import random


carac = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%()&1234567890'


def pegaQtdTam():
    qtd = int(input("Quantas senhas você quer que sejam geradas?"))
    tam = int(input("Qual o tamanho das senhas você quer que sejam geradas?"))
    return [qtd,tam]
    


def geradorDeSenha(dados):

    listaSenhas = []

    for l in range(dados[0]):
        senha = ''
        for s in range(dados[1]):
            senha = random.choice(carac)
            listaSenhas.append(senha)
            print("senha")
    
    return listaSenhas



print("Bem vindo ao gerador de senhas!!")
dados = pegaQtdTam()
print("Suas senhas estão sendo geradas!")
listaDeSenhas = geradorDeSenha(dados)



