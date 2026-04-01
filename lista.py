lista = []

while True:
    print('\ninserir, listar, deletar, sair\n')
    
    pergunta = input('O que deseja fazer em sua lista? ').lower()

    if pergunta == 'inserir':
        inserir = input('Qual item deseja inserir? ').lower()
        lista.append(inserir)
        
    elif pergunta ==  'listar':
        if not lista:
            print('Lista vazia')
        else:
            for indice, item in enumerate(lista):
                print(indice, item)
    
    elif pergunta == 'deletar':
        if not lista:
            print('Lista vazia')
        else:
            for indice, item in enumerate(lista):
                print(indice, item)
            try:
                deletar = int(input('Qual indice deseja deletar? '))
                lista.pop(deletar)
            except:
                print('Indice inválido')
    elif pergunta == 'sair':
        print('Encerrando programa...')
        break
        
         
        
        
  

        


    

    
