#Variavéis: lista de produtos, serviços e preços
produtos=('Teclado','Mouse','Memória RAM','Memória HD','Memória SSD','Placa de vídeo','Webcam')
precos_produtos=(10.0,20.0,30.0,40.0,50.0,60.0,70.0)
estoque_produtos=[10,5,2,25,3,5,8]

servicos=('Manutenção de software','Reparos','Formatação','Montagem','Troca de peças')
precos_servicos=(10.0,20.0,30.0,40.0,50.0)

#Carrinho do usuário
carrinho_produtos=[]
quantidade_produto=[]
carrinho_servicos=[]
quantidade_servico=[]
total_carrinho=0.0
cartao=[]
cedulas=[50,20,10,5,2,1]
troco=[]
controle_pag=False
#Inicialização
print("*****Loja de Informática*****")
print("---------------------------")
print('|     Acessar sistema      |')
print("---------------------------")

while True:

    while True:
        print("A. Acessar")
        print("F. Finalizar")
        opcao_menu1=input("Digite A para acessar o sistema ou F para finalizar:\n")
        opcao_menu1=opcao_menu1.upper()
        if(opcao_menu1=='A'or opcao_menu1=='F'):
            break
    if(opcao_menu1=='F' and total_carrinho==0):
        print('Obrigado pela visita!')
        break
    elif(opcao_menu1=='F' and total_carrinho>0):
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
            if(controle_pag):
                print(f'O total gasto foi: {total_carrinho}')
                break
            else:
                print('Os produtos listados acima estão pendente de pagamento')
                opcao_menu1=input('Se você deseja voltar e concluir o pagamento digite A ou sair digite F')
                opcao_menu1=opcao_menu1.upper()
                if(opcao_menu1=='F'):
                    carrinho_produtos=[]
                    break

    #Menu 2
    while(opcao_menu1=='A'):
        
        #Opções do Menu 2
        print('     MENU')
        print("""
    1. Lista de produtos
    2. Lista de serviços
    3. Consultar o carrinho
    4. Finalizar compra
    5. Voltar para o Menu inicial
    """)

        while True: #Validação do Menu 2
            opcao_menu2=input('Digite a opção desejada: ')
            opcao_menu2=int(opcao_menu2)
            
            print(opcao_menu2)
            
            #Controle de entrada inválida
            if(opcao_menu2>=1 and opcao_menu2<=5):
                break
        
        #Entrada do Menu 2
        while(opcao_menu2>=1 and opcao_menu2<=5):
            
            #Mostra a lista de produtos para o usuário
            if(opcao_menu2==1):
                print('Lista de produtos:')
                tamanho_p=len(produtos)
                
                for i in range(tamanho_p):
                  print(f'{i+1}.{produtos[i]} - R${precos_produtos[i]}') #Mostra na tela os produtos listados e o preço de cada
                
                print('Para comprar um produto digite o númeo do índice correspondente ou 0 concluir')

                #Validação da escolha do produto
                while True:
                    while True:
                        escolha=int(input('Digite o número de sua escolha ou 0 para concluir: '))
                        if(escolha>=0 and escolha<=tamanho_p): 
                            break

                    if(estoque_produtos[escolha-1]==0): #Controle de estoque
                        print('Lamentamos, esse produto não está mais disponível!')
                        break

                    if(escolha==0): #Voltar ao Menu 2
                        opcao_menu2=0
                        break
                    else: #Entrada dos produtos selecionados (cálculo de preço e quantidade)
                        quantidade=int(input('Informe a quantidade que quer do produto escolhido: '))

                        
                        while True:
                            if(carrinho_produtos.count(escolha-1)>=1):
                                pos1=carrinho_produtos.index(escolha-1)
                                quantidade_produto[pos1]=quantidade_produto[pos1]+quantidade
                                total_carrinho=total_carrinho+(precos_produtos[escolha-1]*quantidade)
                            else: #Atualização do estoque e carrinho
                                estoque_produtos[escolha-1]=estoque_produtos[escolha-1]-quantidade
                                carrinho_produtos.append(escolha-1)
                                quantidade_produto.append(quantidade)
                                total_carrinho=total_carrinho+(precos_produtos[escolha-1]*quantidade)
                            if(quantidade<=0):
                                quantidade=int(input('Informe um valor maior que 0: '))
                            elif(quantidade>estoque_produtos[escolha-1]): #Controle de estoque
                                print(f'A quantidade excedeu o estoque. Temos {estoque_produtos[escolha-1]} unidades desse produto')
                                quantidade=int(input(f'Informe uma quantidade até {estoque_produtos[escolha-1]}'))
                            else:
                                break
                    
                    print(f'Subtotal de produtos e serviços: R${total_carrinho}')
                            
                    
                
                    
                while True:
                    opcao_menu3=int(input('''
                    1. Deseja ir para a forma de pagamento
                    2. Limpar o carrinho
                    3. Voltar'''))
                    
                    #Controle de entrada inválida
                    if(opcao_menu3>=1 or opcao_menu3<=3):
                        break
                
                #Ir para a finalização da compra
                if opcao_menu3==1:
                    opcao_menu2=4
                    print(opcao_menu3) 
                elif opcao_menu3==3: #Voltar ao Menu 2
                    opcao_menu2=0
                elif opcao_menu3==2: #Esvaziar o carrinho
                    while True:
                        print('Você está desistindo da compra dos seguintes produtos')
                        for i in range(len(carrinho_produtos)):
                            print(f'{produtos[carrinho_produtos[i]]}-{quantidade_produto[i]} un.')
                        while True:
                            opcao_desisti=input('Digite S se deseja desistir da compra e N para continuar comprado')
                            opcao_desisti=opcao_desisti.upper()
                            if(opcao_desisti=='S'or opcao_desisti=='N'):
                                break
                        if(opcao_desisti=='S'):
                            carrinho_produtos=[]
                            quantidade_produto=[]
                            carrinho_servicos=[]
                            quantidade_servico=[]
                            total_carrinho=0.0
                            print('Carrinho vazio!')
                            opcao_menu2=0 #Voltar ao Menu 2
                            break
                        elif(opcao_desisti=='N'):
                            opcao_menu2=1
                            break
                        
                        
            
            #Mostra a lista de serviços para o usuário   
            elif(opcao_menu2==2):
                print('Lista de serviços:')
                tamanho_s=len(servicos)
                
                for i in range(tamanho_s):
                  print(f'{i+1}.{servicos[i]} - R${precos_servicos[i]}') #Mostra na tela os serviços listados e o preço de cada

                print('Para comprar um serviço digite o númeo do índice correspondente ou 0 para sair')
                while True:
                    while True:
                      escolha=int(input('Digite o número de sua escolha ou 0 para concluir: '))
                      if(escolha>=0 and escolha<=tamanho_s):
                        break

                    if(escolha==0): #Voltar ao Menu 2
                        opcao_menu2=0
                        break

                    else: #Entrada dos serviços selecionados (cálculo de preço e quantidade)
                        quantidade=int(input('Informe a quantidade que quer do produto escolhido: '))
                        while True:
                            if(quantidade<=0):
                                quantidade=int(input('Digite uma quantidade maior que 0: '))
                            else:
                                break


                    #Agrupar serviços no carrinho
                    if(carrinho_servicos.count(escolha-1)>0):
                        pos2=carrinho_servicos.index(escolha-1)
                        quantidade_servico[pos2]=quantidade_servico[pos2]+quantidade
                    else: #Atualização do carrinho
                        carrinho_servicos.append(escolha-1)
                        quantidade_servico.append(quantidade)
                        print(precos_servicos[escolha-1])
                        total_carrinho=total_carrinho+(precos_servicos[escolha-1]*quantidade)
                        print(f'Subtotal de produtos e serviços: R${total_carrinho}')
                        
                while True:
                    opcao_menu3=int(input('''
                    1. Deseja ir para a forma de pagamento
                    2. Limpar o carrinho
                    3. Voltar'''))
                    
                    #Controle de entrada inválida
                    if(opcao_menu3>=1 or opcao_menu3<=3):
                        break
                
                #Ir para a finalização da compra
                if opcao_menu3==1:
                    opcao_menu2=4
                elif opcao_menu3==3: #Voltar ao Menu 2
                    opcao_menu2=0
                elif opcao_menu3==2: #Esvaziar o carrinho
                    while True:
                        print('Você está desistindo da compra dos seguintes produtos')
                        for i in range(len(carrinho_servicos)):
                            print(f'{servicos[carrinho_servicos[i]]}-{quantidade_servico[i]} un.')
                        while True:
                            opcao_desisti=input('Digite S se deseja desistir da compra e N para continuar comprado')
                            opcao_desisti=opcao_desisti.upper()
                            if(opcao_desisti=='S'or opcao_desisti=='N'):
                                break
                        if(opcao_desisti=='S'):
                            carrinho_servico=[]
                            quantidade_servico=[]
                            carrinho_servicos=[]
                            quantidade_servico=[]
                            total_carrinho=0.0
                            print('Carrinho vazio!')
                            opcao_menu2=0 #Voltar ao Menu 2
                            break
                        elif(opcao_desisti=='N'):
                            opcao_menu2=1
                            break
            
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
                
                #Saída quando não há itens
                if(len(carrinho_servicos)==0 and len(carrinho_produtos)==0):
                    print('Você ainda não adicionou nenhum item ao carrinho')
                
                #Valor final de produtos e serviços
                if(len(carrinho_servicos)!=0 or len(carrinho_produtos)!=0):
                    print(f'O valor total é {total_carrinho}')
                
                #Menu 3
                while True:
                    opcao_menu3=int(input('''
                    1. Deseja ir para a forma de pagamento
                    2. Limpar o carrinho
                    3. Voltar'''))
                    
                    #Controle de entrada inválida
                    if(opcao_menu3>=1 or opcao_menu3<=3):
                        break
                
                #Ir para a finalização da compra
                if opcao_menu3==1:
                    opcao_menu2=4
                    print(opcao_menu3) 
                elif opcao_menu3==3: #Voltar ao Menu 2
                    opcao_menu2=0
                elif opcao_menu3==2: #Esvaziar o carrinho
                    carrinho_produtos=[]
                    quantidade_produto=[]
                    carrinho_servicos=[]
                    quantidade_servico=[]
                    total_carrinho=0.0
                    print('Carrinho vazio!')
                    opcao_menu2=0 #Voltar ao Menu 2

            #Finalizar compra    
            elif(opcao_menu2==4):

                #Produtos adicionados ao carrinho
                if(len(carrinho_produtos)>0): 
                    print('Produtos')
                    print('nº    -      Produto        -   Qtd -   Valor Unitario   -   Valor Total')
                    
                    for i in range(len(carrinho_produtos)):
                        print(i,   '     -   ',produtos[carrinho_produtos[i]],'     -     ',quantidade_produto[i], '     -     ',precos_produtos[carrinho_produtos[i]], '     -     ', (quantidade_produto[i]*precos_produtos[carrinho_produtos[i]]))
                
                #Serviços adicionados ao carrinho
                if(len(carrinho_servicos)>0):
                    print('Serviços')
                    print('nº    -      Produto        -   Qtd -   Valor Unitario   -   Valor Total')
                    
                    for i in range(len(carrinho_servicos)):
                        print(i+1,   '     -   ',servicos[carrinho_servicos[i]],'     -     ',quantidade_servico[i], '     -     ',precos_servicos[carrinho_servicos[i]], '     -     ', (quantidade_servico[i]*precos_servicos[carrinho_servicos[i]]))
                
                #Saída quando não há itens
                if(len(carrinho_servicos)==0 and len(carrinho_produtos)==0):
                    print('Você ainda não adicionou nenhum item ao carrinho')
                    break
                
                #Valor final de produtos e serviços
                if(len(carrinho_servicos)!=0 or len(carrinho_produtos)!=0):
                    print(f'O valor total é {total_carrinho}')
                
                #Menu 4
                while True:
                    print('Informe a forma de pagamento:')
                    opcao_menu4=int(input('''
                    1. Cartão de crédito ou dédito
                    2. Pix
                    3. Boleto
                    4. Dinheiro
                    5. Desitir da compra e limpar o carrinho'''))
                    
                    #Controle de entrada inválida
                    if(opcao_menu4>=1 and opcao_menu4<=5):
                        break
                
                if opcao_menu4==1:
                    print('Informe os dados do cartão:')
                    cartao=input("")
                    print('Pagamento efetuado com sucesso!')
                    controle_pag=True
                elif opcao_menu4 ==2:
                    print('Ecaneie o QRCode')
                    print('Pagamento efetuado com sucesso!')
                    controle_pag=True
                elif opcao_menu4 ==3: 
                    print('O codigo barras é XXXXXXXXXXXXX. Vecimento em: ')
                    controle_pag=True
                elif opcao_menu4 ==4:
                    
                    while True:
                        pagamento=input(f'O valor total é {total_carrinho}. Informe o valor de entrada para cálculo do troco:')
                        pagamento=float(pagamento)

                        #Validação do valor de entrada
                        if(pagamento>=total_carrinho):
                            break
                    
                    #Definição do troco
                    total_troco=pagamento-total_carrinho
                    pagamento=pagamento-total_carrinho
            
                    
                    #Verificação do menor número de cédulas para o troco
                    for i in cedulas:
                        tr=pagamento//i
                        pagamento=pagamento%i
                        troco.append(tr)
                        
                        
                    a=''
                    for i in range(len(troco)):
                        if(troco[i]>0):
                            if i<(len(troco)-2):
                                a=a+(str(troco[i])+"X R$ "+str(cedulas[i]))+", "
                            else:
                                a=a+(str(troco[i])+"X R$ "+str(cedulas[i]))
        
                            
                    print(f'O seu troco será {total_troco}, disponível em {a}')
                    controle_pag=True
                    opcao_menu2=0
                elif opcao_menu4 ==5:
                    while True:
                        print('Você está desistindo da compra dos seguintes produtos')
                        if(len(carrinho_produtos)>0):
                            for i in range(len(carrinho_produtos)):
                                print(f'{servicos[carrinho_produtos[i]]}-{quantidade_produto[i]} un.')
                        if(len(carrinho_servicos)>0):
                            for i in range(len(carrinho_servicos)):
                                print(f'{servicos[carrinho_servicos[i]]}-{quantidade_servico[i]} un.')
                            
                        while True:
                            opcao_desisti=input('Digite S se deseja desistir da compra e N para continuar comprado')
                            opcao_desisti=opcao_desisti.upper()
                            if(opcao_desisti=='S'or opcao_desisti=='N'):
                                break
                        if(opcao_desisti=='S'):
                            carrinho_servico=[]
                            quantidade_servico=[]
                            carrinho_servicos=[]
                            quantidade_servico=[]
                            total_carrinho=0.0
                            print('Carrinho vazio!')
                            opcao_menu2=0 #Voltar ao Menu 2
                            break
                        elif(opcao_desisti=='N'):
                            opcao_menu2=0
                            break
                     
            elif(opcao_menu2==5):
                opcao_menu2=0 #Voltar ao Menu 2
                opcao_menu1='F' #Finalizar o programa
                break 
          
