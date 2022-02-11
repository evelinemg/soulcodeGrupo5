#Novo Codigo Inserindo Whiles e Assim dando Loop nos Menus

#Variavéis: lista de produtos, serviços e preços
produtos = ('Teclado','Mouse','Memória RAM','Memória HD','Memória SSD','Placa de vídeo','Webcam')
precos_produtos = (10.0,20.0,30.0,40.0,50.0,60.0,70.0)
estoque_produtos=[10, 5, 2, 25,  3, 5, 8]

servicos = ('Manutenção de software','Reparos','Formatação','Montagem','Troca de peças')
precos_servicos = (10.0,20.0,30.0,40.0,50.0)
for i in range(len(servicos)):
    print(i)
               

#Carrinho do usuário
carrinho_produtos = []
quantidade_produto = []
carrinho_servicos = []
quantidade_servico = []
total_carrinho = 0.0
cartao=[]
cedulas=[50, 20, 10, 2, 1]
troco=[]

#Inicialização
print("*****Loja de Informática*****")
print("---------------------------")
print('|     Acessar sistema      |')
print("---------------------------")

while True:

    while True: #Validação do Menu 1
      
      #Opções do Menu 1
      print("A. Acessar")
      print("F. Finalizar")

      #Variável de acesso ao Menu 2
      opcao_menu1=input("Digite A para acessar o sistema ou F para finalizar:\n")
      opcao_menu1 = opcao_menu1.upper()

      if(opcao_menu1=='A'or opcao_menu1=='F'):
        break
        
    #Menu 2
    while(opcao_menu1=='A'):
        
        #Opções do Menu 2
        print("Menu")
        print("""
    1. Lista de produtos
    2. Lista de serviços
    3. Consultar o carrinho
    4. Finalizar compra
    5. Sair""")
        
        while True: #Validação do Menu 2
            opcao_menu2=int(input())
            if(opcao_menu2>=1 and opcao_menu2<=5):
                break
        
        #Entrada do Menu 2
        while(opcao_menu2>=1 and opcao_menu2<=5):
            
            #Mostra a lista de produtos para o usuário
            if(opcao_menu2==1):
                print('Lista de produtos:')
                for i in range(len(produtos)):
                  print(f'{i+1}.{produtos[i]} - R${precos_produtos[i]}') #Mostra na tela os produtos listados e o preço de cada
                
                #Validação da escolha do produto
                while True:
                  escolha = int(input('Escolha o produto pelo índice ou digite 0 para sair:')) #REVER
                  if(estoque_produtos[escolha-1]==0):
                        print('Lamentamos, esse produto não está mais disponível')
                        break
                  if(escolha < 0 and escolha > len(produtos)):
                    continue
                  elif(escolha==0): #Voltar ao Menu 2
                    opcao_menu2=0
                    break
                  else: #Entrada dos produtos selecionados (cálculo de preço e quantidade)
                    quantidade = int(input('Informe a quantidade que quer do produto escolhido: '))
                    while True:
                        if(quantidade<=0):
                            quantidade = int(input('Informe um valor maior que 0: '))
                        elif(quantidade>estoque_produtos[escolha-1]):
                            print(f'A quantidade excedeu o estoque. Temos {estoque_produtos[escolha-1]} unidades desse produto')
                            quantidade = int(input(f'Informe uma quantidade ate {estoque_produtos[escolha-1]}'))
                        else:
                            break
                    estoque_produtos[escolha-1]=estoque_produtos[escolha-1]-quantidade
                    carrinho_produtos.append(escolha-1)
                    quantidade_produto.append(quantidade)
                    total_carrinho = total_carrinho + (precos_produtos[escolha-1]*quantidade)
                    print(f'Subtotal de produtos e serviços: R${total_carrinho}')
            
            #Mostra a lista de serviços para o usuário   
            elif(opcao_menu2==2):
                print('Lista de serviços:')
                for i in range(len(servicos)):
                  print(f'{i+1}.{servicos[i]} - R${precos_servicos[i]}')
                
                while True:
                  escolha = int(input('Escolha o produto pelo índice ou digite 0 para sair:')) #REVER

                  if(escolha < 0 and escolha > len(servicos)):
                    continue
                  elif(escolha==0): #Voltar ao Menu 2
                    opcao_menu2=0
                    break
                  else: #Entrada dos serviços selecionados (cálculo de preço e quantidade)
                    
                    carrinho_servicos.append(escolha-1)
                    quantidade = int(input('Informe a quantidade que quer do produto escolhido: '))
                    while True:
                        if(quantidade<=0):
                            quantidade = int(input('Digite uma quantidade maior que 0: '))
                        else:
                            break
                    quantidade_servico.append(quantidade)
                    print(precos_servicos[escolha-1])
                    total_carrinho = total_carrinho + (precos_servicos[escolha-1]*quantidade)
                    print(f'Subtotal de produtos e serviços: R${total_carrinho}')
            
            #Carrinho
            elif(opcao_menu2==3):
                if(len(carrinho_produtos)>0):
                    print('Produtos')
                    print('nº    -      Produto        -   Qtd -   Valor Unitario   -   Valor Total')
                    for i in range(len(carrinho_produtos)):
                        print(i,   '     -   ',produtos[carrinho_produtos[i]],'     -     ',quantidade_produto[i], '     -     ',precos_produtos[carrinho_produtos[i]], '     -     ', (quantidade_produto[i]*precos_produtos[carrinho_produtos[i]]))
                if(len(carrinho_servicos)>0):
                    print('Serviços')
                    print('nº    -      Produto        -   Qtd -   Valor Unitario   -   Valor Total')
                    for i in range(len(carrinho_servicos)):
                        print(i+1,   '     -   ',servicos[carrinho_servicos[i]],'     -     ',quantidade_servico[i], '     -     ',precos_servicos[carrinho_servicos[i]], '     -     ', (quantidade_servico[i]*precos_servicos[carrinho_servicos[i]]))
                if(len(carrinho_servicos)==0 and len(carrinho_produtos)==0):
                    print('Você ainda não adicionou nenhum produto ao carrinho')
                if(len(carrinho_servicos)!=0 or len(carrinho_produtos)!=0):
                    print('                             Valor total:', total_carrinho) 
                while True:
                    opcao=int(input('''
                    1. Deseja ir para a forma de pagamento
                    2.Limpar o carrinho
                    3. Voltar'''))
                    
                    if(opcao>=1 or opcao<=3):
                        break
                    
                if opcao==1:
                    opcao_menu2=4
                    print(opcao)
                    
                elif opcao==3:
                    opcao_menu2=0
                    
                    
                elif opcao==2:
                    carrinho_produtos = []
                    quantidade_produto = []
                    carrinho_servicos = []
                    quantidade_servico = []
                    total_carrinho = 0.0
                    print('Carrinho limpo')
                    opcao_menu2=0
                    
                        
                        
                    
                    
                
                
                
            elif(opcao_menu2==4):
                if(len(carrinho_produtos)>0):
                    print('Produtos')
                    print('nº    -      Produto        -   Qtd -   Valor Unitario   -   Valor Total')
                    for i in range(len(carrinho_produtos)):
                        print(i,   '     -   ',produtos[carrinho_produtos[i]],'     -     ',quantidade_produto[i], '     -     ',precos_produtos[carrinho_produtos[i]], '     -     ', (quantidade_produto[i]*precos_produtos[carrinho_produtos[i]]))
                if(len(carrinho_servicos)>0):
                    print('Serviços')
                    print('nº    -      Produto        -   Qtd -   Valor Unitario   -   Valor Total')
                    for i in range(len(carrinho_servicos)):
                        print(i+1,   '     -   ',servicos[carrinho_servicos[i]],'     -     ',quantidade_servico[i], '     -     ',precos_servicos[carrinho_servicos[i]], '     -     ', (quantidade_servico[i]*precos_servicos[carrinho_servicos[i]]))
                if(len(carrinho_servicos)==0 and len(carrinho_produtos)==0):
                    print('Você ainda não adicionou nenhum produto ao carrinho')
                if(len(carrinho_servicos)!=0 or len(carrinho_produtos)!=0):
                    print(f'O valor total é {total_carrinho}')
                while True:
                    print('Informe a forma de pagamento')
                    opcao=int(input('''1. Cartão de Credito ou Crédito
                    2. Pix
                    3. Boleto
                    4. Dinheiro
                    5. Desitir da compra e limpar o carrinho'''))
                    if(opcao>=1 and opcao<=5):
                        break
                if opcao==1:
                    print('Informe os dados do cartão de credito')
                elif opcao ==2:
                    print('Scanei o QRCode')
                elif opcao ==3:
                    print('O codigo barras é XXXXXXXXXXXXX. Vecimento em ')
                elif opcao ==4:
                    while True:
                        pagamento=input(f'O valor total é {total_carrinho}. Informe o valor para calcular o troco')
                        pagamento=int(pagamento)
                        if(pagamento>=total_carrinho):
                            break
                    pagamento=pagamento-total_carrinho
                    for i in cedulas:
                        tr=pagamento//i
                        pagamento=pagamento%i
                        troco.append(tr)
                    for i in range(len(troco)):
                        if(troco[i]>0):
                            print(f'O seu troco será {int(troco[i])} cedulas de {cedulas[i]}')
                    
                        
                    
                    
                opcao_menu2=0
                        
                
                    
                    
                
                
                
                 
                
                                              
                
                
                
                

            #elif(opcao_menu2==4):  
            elif(opcao_menu2==5):
                opcao_menu2=0
                opcao_menu1='F'
                break 
