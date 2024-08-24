import os    #Biblioteca para manipular arquivo
import time  #Biblioteca para definir delay

#---------------------------------------------------------------------------------------------------------------------------------------------------------                                    

#Função para averiguar se a senha está correta
def identificaSenha(x = None):
    cpf = input ('Digite o CPF: ')          #Requer o CPF ao usuario
    if os.path.isfile(cpf+'.txt'):          #confere se existe um arquivo com cpf referente
        arquiv = open(cpf+'.txt', 'r')      #Abre tal arquivo
        senha = input('Digite uma Senha: ')   #Requer uma senha ao usuario
        leitor = arquiv.readlines()         #Variavel que lê as linhas do arquivo
        arquiv.close()                      #Fechamento do arquivo
        dados = []                          #Dados é uma lista que vai armazenaras linhas do arquivo
        for y in leitor:                    #Para cada elemento lido
            organizador = y.split()         #Organizador guarda cada elemento sem o \n
            dados.append(organizador)       #Adiciona na lista dados os elementos sem o \n
    else:
        print('\nCPF incorreto e/ou Conta inexistente!\n') #Registra que o CPF esta errado ou inexistente
        time.sleep(1)
        return menu()
    if x:                                   #Se x tiver um valor diferente de None
        return dados, senha, cpf            #Retorna os valores dados, senha e cpf
    else:
        return dados, senha                 #Retorna os valores dados, senha

#---------------------------------------------------------------------------------------------------------------------------------------------------------                                    

#Função para criar novo usuário e começar um pedido
def novoPedido():   
    precoFinal = 0
    nome = input('Digite o nome: ')                     #Requer o nome do usuario
    cpf = input('Digite o CPF: ')                       #Requer o cpf do usuario
    if(len(cpf) < 9):                                   #---------------------------------------------------------   
        print('\nCPF inválido!\n')                      # Observa se o tamanho do CPF é menor que 9 dígitos       
        time.sleep(1)                                   # Caso seja, retorna que o CPF é inválido                
        return novoPedido()                             #----------------------------------------------------------
        
    elif(len(cpf) > 13):                                #---------------------------------------------------------   
        print('\nCPF inválido!\n')                      # Observa se o tamanho do CPF é maior que 13 dígitos       
        time.sleep(1)                                   # Caso seja, retorna que o CPF é inválido 
        return novoPedido()                             #----------------------------------------------------------
    if os.path.isfile(cpf+'.txt'):                      #confere se existe um arquivo com cpf referente
        print('\nCliente ja registrado!\n')             #Diz que o cliente ja existe
        time.sleep(1)

    else:
            senha = input('Digite uma Senha: ')
            arquiv = open(cpf+'.txt', 'w')  
            arquiv.write('%s\n' % nome)         #Arquiva o nome inserido pelo usuario
            arquiv.write('%s\n' % senha)        #Arquiva a senha inserido pelo usuario
            arquiv.write('%s\n' % cpf)          #Arquiva o cpf inserido pelo usuario  
            print('\nCadastro criado com sucesso!\n') 
            
            time.sleep(2)


            show = 1

            while(show == 1):
#-----------------------------------------------------------------------------------------             
                print('''
Código        Produto          Preço
1            X-salada        R$ 10,00
2            X-burger        R$ 10,00
3         Cachorro quente    R$ 7,50            
4          Misto quente      R$ 8,00                                        
5        Salada de frutas    R$ 5,50
6          Refrigerante      R$ 4,50
7          Suco natural      R$ 6,25''')               #Apresenta o cardápio ao cliente
#-----------------------------------------------------------------------------------------              
                valor = 0  #define o valor 0 para a variável valor
#-----------------------------------------------------------------------------------------------------------------------------------------------------------                          
                pedido = int(input('Digite o código do produto que deseja pedir: '))            #Requer o código do produto a ser comprado
                qnt = int(input('Digite a quantidade: '))                                       #Requer a quantidade desse produto

                if(pedido == 1):
                    valor = 10 * qnt                                                                                                        
                    arquiv.write('%d - X-salada               - Preço unitário:    10,00    Valor: +%.2f\n' %(qnt, 10*qnt))
                    
                if(pedido == 2):
                    valor = 10 * qnt
                    arquiv.write('%.2f\n' %precoFinal)
                    arquiv.write('%d - X-burguer              - Preço unitário:    10,00    Valor: +%.2f\n' %(qnt, 10*qnt))
                    
                if(pedido == 3):
                    valor = 7.5 * qnt                                                                                                                   
                    arquiv.write('%.2f\n' %precoFinal)
                    arquiv.write('%d - Cachorro quente        - Preço unitário:    7,50     Valor: +%.2f\n' %(qnt, 7.50*qnt))             
                    
                if(pedido == 4):                                                                                                             #Retorna todas as possiblidades e valores dentro do cardápio e imprime no arquivo
                    valor = 8 * qnt
                    arquiv.write('%.2f\n' %precoFinal)                                                                                                          
                    arquiv.write('%d - Misto quente           - Preço unitário:    8,00     Valor: +%.2f\n' %(qnt, 8*qnt))        
                    
                if(pedido == 5):
                    valor = 5.5 * qnt
                    arquiv.write('%.2f\n' %precoFinal)
                    arquiv.write('%d - Salada de frutas       - Preço unitário:    5,50     Valor: +%.2f\n' %(qnt, 5.50*qnt))
                    
                if(pedido == 6):
                    valor = 4.5 * qnt
                    arquiv.write('%.2f\n' %precoFinal)
                    arquiv.write('%d - Refrigerante           - Preço unitário:    4,50     Valor: +%.2f\n' %(qnt, 4.50*qnt))
                    
                if(pedido == 7):
                    valor = 6.25 * qnt
                    arquiv.write('%.2f\n' %precoFinal)
                    arquiv.write('%d - Suco natural           - Preço unitário:    6,25     Valor: +%.2f\n' %(qnt, 6.25*qnt))     

#---------------------------------------------------------------------------------------------------------------------------------------------------------                                    

                precoFinal += valor   #Soma o valor dos itens adicionados em uma só variável para obter o valor final
                
                show = int(input('Deseja adicionar outro item? Digite 1 para SIM e 0 para NÃO: '))  #Pergunta se deseja continuar com o mesmo procedimento
                if(show == 0):
                    arquiv.write('%.2f\n' %precoFinal)
                    arquiv.close()                                   #Caso não queira prosseguir, fecha o arquivo e retorna ao menu
                    return menu()
 #---------------------------------------------------------------------------------------------------------------------------------------------------------                                                   
            
#Função para cancelar o pedido
def cancelaPedido():
    dados, senha, cpf = identificaSenha(1)  #Retorna os dados do usuario que serão manipulados
    if(dados[1][0] == senha):               #Executa o comando caso a senha esteja correta
        os.remove(cpf+'.txt')               #Deleta o arquivo com os dados do pedido
        print('\nPedido Cancelado!\n')      #Imprime aviso de sucesso na operação
        time.sleep(2)                       #delay de 2 segundos

    elif dados[1][0] != senha:              #Se a senha estiver errada ele retorna a mensagem de senha incorreta
        print('\nSenha incorreta!\n')       #Imprime aviso de senha incorreta
        time.sleep(2)                       #delay de 2 segundos

#---------------------------------------------------------------------------------------------------------------------------------------------------------                                    

#Função para inserir algum produto no pedido
def insereProduto():
     dados, senha, cpf = identificaSenha(1)     #Retorna os dados do usuario que serão manipulados
     if(dados[1][0] == senha):                  #Executa o comando caso a senha esteja correta
         show = 1                               #Define valor a variável show
         while(show == 1):                      #Executa os comandos enquanto show tiver o valor de 1
            arquiv = open(cpf+'.txt', 'a')      #abre o arquivo para dar append
            print('''
    Código        Produto          Preço
    1            X-salada        R$ 10,00
    2            X-burger        R$ 10,00
    3         Cachorro quente    R$ 7,50            
    4          Misto quente      R$ 8,00
    5        Salada de frutas    R$ 5,50
    6          Refrigerante      R$ 4,50
    7          Suco natural      R$ 6,25''')  #Apresenta o cardápio ao cliente
            insere = int(input('Insira o código do produto que deseja inserir: ')) #Requer o código do produto a ser inserido
            qnt = int(input('Digite a quantidade: '))                              #Requer a quantidade de produto a ser inserida
#---------------------------------------------------------------------------------------------------------------------------------------------------------                                                
            if(insere == 1):
                valor = 10 * qnt
                arquiv.write('%d - X-salada               - Preço unitário:    10,00    Valor: +%.2f\n' %(qnt, 10*qnt))
            if(insere == 2):
                valor = 10 * qnt
                arquiv.write('%d - X-burguer              - Preço unitário:    10,00    Valor: +%.2f\n' %(qnt, 10*qnt))
            if(insere == 3):
                valor = 7.5 * qnt
                arquiv.write('%d - Cachorro quente        - Preço unitário:    7,50     Valor: +%.2f\n' %(qnt, 7.50*qnt))      
            if(insere == 4):
                valor = 8 * qnt
                arquiv.write('%d - Misto quente           - Preço unitário:    8,00     Valor: +%.2f\n' %(qnt, 8*qnt))        #Cada uma das opções para inserir no pedido já existente
            if(insere == 5):
                valor = 5.5 * qnt
                arquiv.write('%d - Salada de frutas       - Preço unitário:    5,50     Valor: +%.2f\n' %(qnt, 5.50*qnt))
            if(insere == 6):
                valor = 4.5 * qnt
                arquiv.write('%d - Refrigerante           - Preço unitário:    4,50     Valor: +%.2f\n' %(qnt, 4.50*qnt))
            if(insere == 7):
                valor = 6.25 * qnt
                arquiv.write('%d - Suco natural           - Preço unitário:    6,25     Valor: +%.2f\n' %(qnt, 6.25*qnt))            
#---------------------------------------------------------------------------------------------------------------------------------------------------------                                    

            dados[-1][0] = float(dados[-1][0]) + valor  #Modifica o ultimo item da lista
            arquiv.write('%.2f\n' % dados[-1][0])  #escreve o novo ultimo item da lista


            show = int(input('Deseja adicionar outro item? Digite 1 para SIM e 0 para NÃO: '))   #Pergunta se deseja continuar
            if(show == 0):
                arquiv.close()                                #Caso não queira prosseguir, fecha o arquivo e retorna ao menu
                return menu()

     elif dados[1][0] != senha:               #Se a senha estiver errada ele retorna a mensagem de senha incorreta
        print('\nSenha incorreta!\n')
        time.sleep(2)              


#Função para cancelar algum produto do pedido
def cancelaProduto():
     dados, senha, cpf = identificaSenha(1)     #Retorna os dados do usuario que serão manipulados
     if(dados[1][0] == senha):

         show = 1
         while(show == 1):
            arquiv = open(cpf+'.txt', 'a')      #abre o arquivo para dar append
            for i in range(3,len(dados),2):     #Para cada item dentro do tamanho da lista, a partir do três a cada duas linhas
                print('Seus itens:')
                print(*dados[i])                #Retorna dados[i] sem a formatação de lista
            print('Código dos produtos')
            print('''
Código        Produto       
1            X-salada        
2            X-burger     
3         Cachorro quente           
4          Misto quente  
5        Salada de frutas 
6          Refrigerante  
7          Suco natural''')  #Apresenta apenas os códigos dos produtos

            remove = int(input('Insira o código do produto que deseja remover: '))     #Requer o código do produto a ser removido
            qnt = int(input('Digite a quantidade: '))                                  #Requer a quantidade a ser removida
            
            #---------------------------------------------------------------------------------------------------------------------------
            if(remove == 1):
                valor = 10 * qnt
                arquiv.write('%d - X-salada               - Preço unitário:    10,00    Valor: -%.2f   -   Removido\n' %(qnt, 10*qnt))
            if(remove == 2):
                valor = 10 * qnt
                arquiv.write('%d - X-burguer              - Preço unitário:    10,00    Valor: -%.2f   -   Removido\n' %(qnt, 10*qnt))
            if(remove == 3):
                valor = 7.5 * qnt
                arquiv.write('%d - Cachorro quente        - Preço unitário:    7,50     Valor: -%.2f   -   Removido\n' %(qnt, 7.50*qnt))      
            if(remove == 4):
                valor = 8 * qnt
                arquiv.write('%d - Misto quente           - Preço unitário:    8,00     Valor: -%.2f   -   Removido\n' %(qnt, 8*qnt))        #Cada uma das possibilidades a serem removidas
            if(remove == 5):
                valor = 5.5 * qnt
                arquiv.write('%d - Salada de frutas       - Preço unitário:    5,50     Valor: -%.2f   -   Removido\n' %(qnt, 5.50*qnt))
            if(remove == 6):
                valor = 4.5 * qnt
                arquiv.write('%d - Refrigerante           - Preço unitário:    4,50     Valor: -%.2f   -   Removido\n' %(qnt, 4.50*qnt))
            if(remove == 7):
                valor = 6.25 * qnt
                arquiv.write('%d - Suco natural           - Preço unitário:    6,25     Valor: -%.2f   -   Removido\n' %(qnt, 6.25*qnt))            
            #-------------------------------------------------------------------------------------------------------------------------------
            dados[-1][0] = float(dados[-1][0]) - valor  #Modifica o ultimo item da lista
            arquiv.write('%.2f\n' % dados[-1][0])  #escreve o novo ultimo item da lista


            show = int(input('Deseja remover outro item? Digite 1 para SIM e 0 para NÃO: '))  #Realiza novamente caso queira remover outro item
            if(show == 0):      
                arquiv.close()          #Caso não queira prosseguir, fecha o arquivo e retorna ao menu
                return menu()

     elif dados[1][0] != senha:               #Se a senha estiver errada ele retorna a mensagem de senha incorreta
        print('\nSenha incorreta!\n')   
        time.sleep(2)  


#Função para mostrar o valor do pedido
def valorPedido(): 
    dados, senha = identificaSenha()         #Retorna os dados do usuario que serão manipulados
    if dados[1][0] == senha:
        print('Valor: R$%s' %dados[-1][0])   #Retorna o valor
        voltar = int(input("Digite 0 para voltar ao menu: "))
        if(voltar == 0):
            menu()

    elif dados[1][0] != senha:               #Se a senha estiver errada ele retorna a mensagem de senha incorreta

        print('\nSenha incorreta!\n')   
        time.sleep(2)         


def extrato():
    dados, senha= identificaSenha()           #Retorna os dados do usuario que serão manipulados
    if dados[1][0] == senha:                  #Se o dado referente a senha for igual a senha inserida pelo usuario
        print()
        print('Nome: %s' % dados[0][0])       #Retorna o nome
        print('CPF: %s' % dados[2][0])        #Retorna o CPF
        print('Preço: R$%s' % dados[-1][0])   #Retona o Preço final
        print('Itens do pedido:')
        for i in range(3,len(dados),2):       #Para cada item dentro do tamanho da lista, a partir do três a cada duas linhas
            print(*dados[i])                  #Retorna dados[i] sem a formatação de lista

        print()
        voltar = int(input("Digite 0 para voltar ao menu: "))
        if(voltar == 0):
            menu()


    elif dados[1][0] != senha:                #Se o dado referente a senha for igual a senha inserida pelo usuario
        print('\nSenha incorreta!\n')
        time.sleep(2)              

#--------------------------------------------------------------------------------------------------------------------------------------------

#Criação do Menu

def menu():
    while True:
        print()
        print('''
        
_____ Menu _____
        
1 - Novo Pedido
2 - Cancela Pedido
3 - Insere produto
4 - Cancela Produto
5 - Valor do pedido
6 - Extrato do pedido


        
0 - Sair
        ''') # Imprime menu
        print()
        opcao = input('Escolha uma das opções: ') #Variavel que requer a opção escolhida pelo usuario

        print()

        if opcao == '1':
            novoPedido()                    #Realiza a função novoPedido()
        elif opcao == '2':
            cancelaPedido()                 #Realiza a função cancelaPedido()
        elif opcao == '3':
            insereProduto()                 #Realiza a função insereProduto()
        elif opcao == '4':
            cancelaProduto()                #Realiza a função cancelaProduto()
        elif opcao == '5':
            valorPedido()                   #Realiza a função valorPedido()
        elif opcao == '6':
            extrato()                       #Realiza a função extrato()
        elif opcao == '0':                      
            break
        else:
            break

menu()                                      #Realiza a função menu()