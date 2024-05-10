lista_n =  ["alice", "bob", "carol", "david", "emma", "frank", "grace", "henry", "ivy", "jack"]

def pesquisa_binaria(lista_n, valor):
    
    baixo = 0
    alto = len(lista_n) - 1
    
    count = 0
    
    while baixo <= alto:
        
        count += 1

        meio = (baixo + alto) // 2
        chute = lista_n[meio]
       
        if chute == valor:
           return f'indice = {meio} valor = {lista_n[meio]}, etapas = {count}' 
           
           
        if chute > valor:
            alto = meio - 1
            
        else:
            baixo = meio + 1
    
    return 'valor não encontrado'
       
       
print(pesquisa_binaria(lista_n, 'jack'))