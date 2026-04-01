lista = []

while True:
    pergunta = input('O que deseja fazer em sua lista? ').lower()

    if pergunta == 'inserir' or pergunta == 'i':
        inserir = input('Qual item deseja inserir? ').lower()
        lista.append(inserir)
        
    elif pergunta ==  'listar' or pergunta == 'l':
        for indice, item in enumerate(lista):
            print(indice, item)
    
    elif pergunta == 'deletar' or pergunta == 'del':
        for indice, item in enumerate(lista):
            print(indice, item)
        try:    
            deletar = int(input('Qual indice deseja deletar? '))
            lista.pop(deletar)
        except:
            print('Indice inválido')
        
         
        
        
  

        


    

    
