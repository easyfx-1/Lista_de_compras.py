import subprocess
import platform

# Função para limpar a tela de forma cross-platform usando subprocess
def limpar_tela():
    if platform.system() == "Windows":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)

lista = []

while True:
    print('inserir, listar, deletar, sair')
    
    pergunta = input('O que deseja fazer em sua lista? ').lower()

    if pergunta == 'inserir':
        inserir = input('Qual item deseja inserir? ').lower()
        lista.append(inserir)
        limpar_tela()
        print(f'"{inserir}" adicionado à lista.\n')
        
    elif pergunta ==  'listar':
        limpar_tela()
        if not lista:
            print('Lista vazia')
        else:
            for indice, item in enumerate(lista):
                print(indice, item)
    
    elif pergunta == 'deletar':
        if not lista:
            print('Lista vazia')
        else:
            limpar_tela()
            for indice, item in enumerate(lista):
                print(indice, item)
            try:
                deletar = int(input('Qual indice deseja deletar? '))
                valor_removido = lista.pop(deletar)
                limpar_tela()
                print(f'"{valor_removido}" foi removido da lista.\n')
            except:
                print('Índice inválido')
                
    elif pergunta == 'sair':
        print('Encerrando programa...')
        break

    else:
        print('Opção inválida, escolha inserir, listar, deletar ou sair.\n')
