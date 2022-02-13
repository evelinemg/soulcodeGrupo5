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
print('*****Loja de Informática*****')
print('---------------------------')
print('|     Acessar sistema      |')
print('---------------------------')

while True:

    while True:
        print('MENU INICIAL\n')
        print('A. Acessar')
        print('F. Finalizar')
        opcao_menu1=input('\nDigite A para acessar o sistema ou F para finalizar: ')
        opcao_menu1=opcao_menu1.upper()

        #Controle de entrada inválida
        if(opcao_menu1=='A'or opcao_menu1=='F'):
            break
        else:
            print('Entrada inválida!')

    if(opcao_menu1=='F' and total_carrinho==0): #Saída do sistema e controle para que não saia sem pagar
        print('Obrigado pela visita!')
        break
    elif(opcao_menu1=='F' and total_carrinho>0): #Direciona para o pagamento se tiver débito
        
        if(len(carrinho_produtos)>0): #Lista de produtos no carrinho
            print('Produtos')
            print('nº    -      Produto        -   Qtd -   Valor Unitario   -   Valor Total')
            
            for i in range(len(carrinho_produtos)):
                print(i+1,   '     -   ',produtos[carrinho_produtos[i]],'     -     ',quantidade_produto[i], '     -     ',precos_produtos[carrinho_produtos[i]], '     -     ', (quantidade_produto[i]*precos_produtos[carrinho_produtos[i]])) 
        
        if(len(carrinho_servicos)>0): #Lista de serviços no carrinho
            print('Serviços')
            print('nº    -      Produto        -   Qtd -   Valor Unitario   -   Valor Total')
            
            for i in range(len(carrinho_servicos)):
                print(i+1,   '     -   ',servicos[carrinho_servicos[i]],'     -     ',quantidade_servico[i], '     -     ',precos_servicos[carrinho_servicos[i]], '     -     ', (quantidade_servico[i]*precos_servicos[carrinho_servicos[i]]))
            
        if(controle_pag): #Exibe o que já foi pago
            print(f'O total gasto foi: {total_carrinho}')
            break
        else: #Direciona para o pagamento
            print('Os produtos listados acima estão pendente de pagamento')
            opcao_menu1=input('Se você deseja voltar e concluir o pagamento digite A ou sair digite F: ')
            opcao_menu1=opcao_menu1.upper()
            
            if(opcao_menu1=='F'): #Desistência: esvazia o carrinho e encerra o programa
                carrinho_produtos=[]
                quantidade_produto=[]
                carrinho_servicos=[]
                quantidade_servico=[]
                total_carrinho=0.0
                print('Carrinho vazio!')
                break

    while(opcao_menu1=='A'):
        
        #Menu 2
        print('  \nMENU PRINCIPAL')
        print("""
    1. Lista de produtos
    2. Lista de serviços
    3. Consultar o carrinho
    4. Finalizar compra
    5. Voltar para o menu inicial
    """)

        while True: #Validação do Menu 2
            opcao_menu2=input('Digite a opção desejada: ')
            opcao_menu2=int(opcao_menu2)
            
            #Controle de entrada inválida
            if(opcao_menu2>=1 and opcao_menu2<=5):
                break
            else:
                print('Entrada inválida!')
        
        #Entrada do Menu 2
        while(opcao_menu2>=1 and opcao_menu2<=5):
            
            #Mostra a lista de produtos para o usuário
            if(opcao_menu2==1):
                print('\nLista de produtos:')
                tamanho_p=len(produtos)
                
                for i in range(tamanho_p):
                  print(f'{i+1}.{produtos[i]} - R${precos_produtos[i]}') #Mostra na tela os produtos listados e o preço de cada
                
                print('\nPara comprar um produto digite o número do índice correspondente ou 0 para concluir')

                #Validação da escolha do produto
                while True:
                    while True:
                        escolha=int(input('Digite o número de sua escolha: '))

                        #Controle de entrada inválida
                        if(escolha>=0 and escolha<=tamanho_p): 
                            break
                        else:
                            print('Entrada inválida!')

                    if(estoque_produtos[escolha-1]==0): #Controle de estoque
                        print('Lamentamos, esse produto não está mais disponível!')
                        break

                    if(escolha==0): #Voltar ao Menu 2
                        opcao_menu2=0
                        break
                    else: #Entrada dos produtos selecionados (cálculo de preço e quantidade)
                        quantidade=int(input('Informe a quantidade que deseja do produto escolhido: '))

                        
                        while True:
                            if(carrinho_produtos.count(escolha-1)>=1): #Atualização do estoque e carrinho com agrupamento de itens em comum
                                pos1=carrinho_produtos.index(escolha-1)
                                quantidade_produto[pos1]=quantidade_produto[pos1]+quantidade
                                #REVER: estoque_produtos[escolha-1]=estoque_produtos[escolha-1]-quantidade
                                total_carrinho=total_carrinho+(precos_produtos[escolha-1]*quantidade)
                            else: #Atualização do estoque e carrinho
                                estoque_produtos[escolha-1]=estoque_produtos[escolha-1]-quantidade
                                carrinho_produtos.append(escolha-1)
                                quantidade_produto.append(quantidade)
                                total_carrinho=total_carrinho+(precos_produtos[escolha-1]*quantidade)
                            
                            if(quantidade<=0): #Controle de entrada inválida
                                quantidade=int(input('Informe um valor maior que 0: '))
                            elif(quantidade>estoque_produtos[escolha-1]): #Controle de estoque
                                print(f'A quantidade excedeu o estoque. Temos {estoque_produtos[escolha-1]} unidades desse produto')
                                quantidade=int(input(f'Informe uma quantidade até {estoque_produtos[escolha-1]} unidades: '))
                            else:
                                break
                    
                    print(f'Subtotal de produtos e serviços: R${total_carrinho}') #Valor parcial da compra até o momento

                #Menu 3 em produtos
                while True:
                    opcao_menu3=int(input('''
                    1. Deseja ir para a forma de pagamento
                    2. Limpar o carrinho
                    3. Voltar
                    
                    Digite a opção escolhida: '''))
                    
                    #Controle de entrada inválida
                    if(opcao_menu3>=1 or opcao_menu3<=3):
                        break
                    else:
                        print('Entrada inválida!')
                
                #Ir para a finalização da compra
                if opcao_menu3==1:
                    opcao_menu2=4
                elif opcao_menu3==3: #Voltar ao Menu 2
                    opcao_menu2=0
                elif opcao_menu3==2: #Desistência da compra
                    
                    while True:
                        print('Você está desistindo da compra dos seguintes itens:')

                        if(len(carrinho_produtos)>0): #Lista de produtos no carrinho
                          print('Produtos')
            
                          for i in range(len(carrinho_produtos)):
                              print(f'{produtos[carrinho_produtos[i]]}-{quantidade_produto[i]} un.')
                        
                        if(len(carrinho_servicos)>0): #Lista de serviços no carrinho
                          print('Serviços')
            
                          for i in range(len(carrinho_servicos)):
                            print(f'{servicos[carrinho_servicos[i]]}-{quantidade_servico[i]} un.')                    
                        
                        while True: #Confirmação da desistência
                            opcao_desistir=input('Digite S se deseja desistir da compra e N para continuar comprando: ') 
                            opcao_desistir=opcao_desistir.upper()

                            #Controle de entrada inválida
                            if(opcao_desistir=='S'or opcao_desistir=='N'):
                                break
                            else:
                                print('Entrada inválida!')

                        #Esvaziar carrinh0
                        if(opcao_desistir=='S'):
                            carrinho_produtos=[]
                            quantidade_produto=[]
                            carrinho_servicos=[]
                            quantidade_servico=[]
                            total_carrinho=0.0
                            print('Carrinho vazio! Siga sua operação através do menu principal')
                            opcao_menu2=0 
                            break
                        elif(opcao_desistir=='N'): #Desistir de desistir
                            print('Carrinho mantido! Siga sua operação!')
                            opcao_menu2=1
                            break
                        
                        
            #Mostra a lista de serviços para o usuário   
            elif(opcao_menu2==2):
                print('\nLista de serviços:')
                tamanho_s=len(servicos)
                
                for i in range(tamanho_s):
                  print(f'{i+1}.{servicos[i]} - R${precos_servicos[i]}') #Mostra na tela os serviços listados e o preço de cada

                print('\nPara comprar um serviço digite o número do índice correspondente ou 0 para concluir')

                #Validação da escolha do serviço
                while True:
                    while True:
                      escolha=int(input('Digite o número de sua escolha: '))
                      
                      #Controle de entrada inválida
                      if(escolha>=0 and escolha<=tamanho_s):
                        break
                      else:
                          print('Entrada inválida!')

                    if(escolha==0): #Voltar ao Menu 2
                        opcao_menu2=0
                        break

                    else: #Entrada dos serviços selecionados (cálculo de preço e quantidade)
                        quantidade=int(input('Informe a quantidade que deseja do serviço escolhido: '))
                        
                        while True:
                            if(quantidade<=0): #Controle de entrada inválida
                                quantidade=int(input('Digite uma quantidade maior que 0: '))
                            else:
                                break

                    #Agrupar serviços no carrinho
                    if(carrinho_servicos.count(escolha-1)>0):
                        pos2=carrinho_servicos.index(escolha-1)
                        quantidade_servico[pos2]=quantidade_servico[pos2]+quantidade
                        total_carrinho=total_carrinho+(precos_servicos[escolha-1]*quantidade)
                        print(f'Subtotal de produtos e serviços: R${total_carrinho}')
                    else: #Atualização do carrinho
                        carrinho_servicos.append(escolha-1)
                        quantidade_servico.append(quantidade)
                        total_carrinho=total_carrinho+(precos_servicos[escolha-1]*quantidade)
                        print(f'Subtotal de produtos e serviços: R${total_carrinho}')
                
                #Menu 3 em serviços      
                while True:
                    opcao_menu3=int(input('''
                    1. Deseja ir para a forma de pagamento
                    2. Limpar o carrinho
                    3. Voltar
                    
                    Digite a opção escolhida: '''))
                    
                    #Controle de entrada inválida
                    if(opcao_menu3>=1 or opcao_menu3<=3):
                        break
                    else:
                        print('Entrada inválida!')
                
                #Ir para a finalização da compra
                if opcao_menu3==1:
                    opcao_menu2=4
                elif opcao_menu3==3: #Voltar ao Menu 2
                    opcao_menu2=0
                elif opcao_menu3==2: #Desistência da compra
                    while True:
                        print('Você está desistindo da compra dos seguintes itens:')
                        
                        if(len(carrinho_produtos)>0): #Lista de produtos no carrinho
                          print('Produtos')
            
                          for i in range(len(carrinho_produtos)):
                              print(f'{produtos[carrinho_produtos[i]]}-{quantidade_produto[i]} un.')
                        
                        if(len(carrinho_servicos)>0): #Lista de serviços no carrinho
                          print('Serviços')
            
                          for i in range(len(carrinho_servicos)):
                            print(f'{servicos[carrinho_servicos[i]]}-{quantidade_servico[i]} un.') 
                        
                        while True: #Confirmação da desistência
                            opcao_desistir=input('Digite S se deseja desistir da compra e N para continuar comprando: ')
                            opcao_desistir=opcao_desistir.upper()
                            if(opcao_desistir=='S'or opcao_desistir=='N'):
                                break
                            else:
                                print('Entrada inválida!')

                        #Esvaziar carrinho        
                        if(opcao_desistir=='S'):
                            carrinho_servico=[]
                            quantidade_servico=[]
                            carrinho_servicos=[]
                            quantidade_servico=[]
                            total_carrinho=0.0
                            print('Carrinho vazio! Siga sua operação através do menu principal!')
                            opcao_menu2=0 
                            break
                        elif(opcao_desistir=='N'): #Desistir de desistir
                            print('Carrinho mantido! Siga sua operação')
                            opcao_menu2=1
                            break
            
            #Carrinho
            elif(opcao_menu2==3):
                
                if(len(carrinho_produtos)>0):
                    print('Produtos')
                    print('nº    -      Produto        -   Qtd -   Valor Unitario   -   Valor Total')
                    
                    for i in range(len(carrinho_produtos)):
                        print(i+1,   '     -   ',produtos[carrinho_produtos[i]],'     -     ',quantidade_produto[i], '     -     ',precos_produtos[carrinho_produtos[i]], '     -     ', (quantidade_produto[i]*precos_produtos[carrinho_produtos[i]]))
                

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
                    3. Voltar
                    
                    Digite a opção escolhida:'''))
                    
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
                        print(i+1,   '     -   ',produtos[carrinho_produtos[i]],'     -     ',quantidade_produto[i], '     -     ',precos_produtos[carrinho_produtos[i]], '     -     ', (quantidade_produto[i]*precos_produtos[carrinho_produtos[i]]))
                
                #Serviços adicionados ao carrinho
                if(len(carrinho_servicos)>0):
                    print('Serviços')
                    print('nº    -      Produto        -   Qtd -   Valor Unitario   -   Valor Total')
                    
                    for i in range(len(carrinho_servicos)):
                        print(i+1,   '     -   ',servicos[carrinho_servicos[i]],'     -     ',quantidade_servico[i], '     -     ',precos_servicos[carrinho_servicos[i]], '     -     ', (quantidade_servico[i]*precos_servicos[carrinho_servicos[i]]))
                
                #Saída quando não há itens
                if(len(carrinho_servicos)==0 and len(carrinho_produtos)==0):
                    print('Você ainda não adicionou nenhum item ao carrinho!')
                    break
                
                #Valor final de produtos e serviços
                if(len(carrinho_servicos)!=0 or len(carrinho_produtos)!=0):
                    print(f'O valor total é {total_carrinho}')
                
                #Menu 4
                while True:
                    print('\nFormas de pagamento')
                    opcao_menu4=int(input('''
                    1. Cartão de crédito ou dédito
                    2. Pix
                    3. Boleto
                    4. Dinheiro
                    5. Desitir da compra e limpar o carrinho
                    6. Voltar ao menu principal
                    
                    Digite a opção escolhida: '''))
                    
                    #Controle de entrada inválida
                    if(opcao_menu4>=1 and opcao_menu4<=6):
                        break
                    else:
                        print('Entrada inválida!')
                
                #Cartão de crédito ou débito
                if opcao_menu4==1: 
                    
                    while True: #Escolha do cartão
                            cartao=input('''
                            C. Crédito
                            D. Débito
                            
                            Digite a opção escolhida:''')
                            cartao=cartao.upper()
                            
                            #Controle de entrada inválida
                            if(cartao=='C'or cartao=='D'):
                                break
                            else:
                                print('Entrada inválida!')

                    print('Informe os dados do cartão') #REVER
                    cartao_nome=input('Nome: ')
                    cartao_num=input('Número: ')
                    cartao_data=input('Data de validade: ')
                    cartao_cvv=input('CVV: ')

                    #Validação do cartão de crédito
                    if(cartao=='C'):
                        
                        while True:
                           cartao_parcelas=int(input('Número de parcelas (Máximo 3x sem juros): '))

                           #Controle de entrada inválida
                           if(cartao_parcelas>0 and cartao_parcelas<4):
                               break
                           else:
                                print('Entrada inválida!')
                              
                    print('Pagamento efetuado com sucesso!')
                    
                    #Liberar carrinho
                    carrinho_produtos=[]
                    quantidade_produto=[]
                    carrinho_servicos=[]
                    quantidade_servico=[]
                    total_carrinho=0.0
                    controle_pag=True
                elif opcao_menu4 ==2: #Pix
                    print('Escaneie o QRCode:')
                    print('''
                    ######
                    ######
                    ######
                    ''')
                    print('Compra concluída! O status do pagamento será atualizado em até 24h após o pagamento!')
                    
                    #Liberar carrinho
                    carrinho_produtos=[]
                    quantidade_produto=[]
                    carrinho_servicos=[]
                    quantidade_servico=[]
                    total_carrinho=0.0
                    controle_pag=True
                elif opcao_menu4 ==3: #Boleto
                    print('''
                    O codigo barras é XXXX.XXXXX.XXXXX.XXXXXX XXXXX.XXXXXX X XXXXXXXXXXXXXX 
                    Vencimento em: DD/MM/AAAA
                    ''')
                    print('Compra concluída! O status do pagamento será atualizado em até 24h após o pagamento!')
                    
                    #Liberar carrinho
                    carrinho_produtos=[]
                    quantidade_produto=[]
                    carrinho_servicos=[]
                    quantidade_servico=[]
                    total_carrinho=0.0
                    controle_pag=True
                elif opcao_menu4 ==4: #Dinheiro
                    
                    while True: #Especificação da entrada
                        pagamento=input(f'O valor total é {total_carrinho}. Para cálculo do troco, informe o valor de entrada:')
                        pagamento=float(pagamento)

                        #Validação do valor de entrada
                        if(pagamento>=total_carrinho):
                            break
                        else:
                            print('Informe um valor igual ou superior ao total da compra')
                    
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
        
                    print(f'O seu troco é {total_troco}, disponível em {a}')
                    print('Pagamento efetuado com sucesso!')
                    
                    #Liberar carrinho
                    carrinho_produtos=[]
                    quantidade_produto=[]
                    carrinho_servicos=[]
                    quantidade_servico=[]
                    total_carrinho=0.0
                    controle_pag=True
                    opcao_menu2=0
                elif opcao_menu4 ==5: #Desistência da compra
                    while True:
                        print('Você está desistindo da compra dos seguintes itens:')

                        if(len(carrinho_produtos)>0): #Lista de produtos no carrinho
                            print('Produtos')

                            for i in range(len(carrinho_produtos)):
                                print(f'{produtos[carrinho_produtos[i]]}-{quantidade_produto[i]} un.')

                        if(len(carrinho_servicos)>0): #Lista de serviços no carrinho
                            print('Serviços')

                            for i in range(len(carrinho_servicos)):
                                print(f'{servicos[carrinho_servicos[i]]}-{quantidade_servico[i]} un.')
                            
                        while True: #Confirmação da desistência
                            opcao_desistir=input('Digite S se deseja desistir da compra e N para continuar comprando')
                            opcao_desistir=opcao_desistir.upper()
                            
                            #Controle de entrada inválida
                            if(opcao_desistir=='S'or opcao_desistir=='N'):
                                break
                            else:
                                print('Entrada inválida!')
                        if(opcao_desistir=='S'):
                            carrinho_servico=[]
                            quantidade_servico=[]
                            carrinho_servicos=[]
                            quantidade_servico=[]
                            total_carrinho=0.0
                            print('Carrinho vazio! Siga sua operação através do menu principal!')
                            opcao_menu2=0 #Voltar ao Menu 2
                            break
                        elif(opcao_desistir=='N'):
                            opcao_menu2=0
                            print('Carrinho mantido! Siga sua operação através do menu principal!')
                            break
                elif opcao_menu4==6:
                    opcao_menu2=0
                     
            elif(opcao_menu2==5):
                opcao_menu2=0 #Voltar ao Menu 2
                opcao_menu1='F' #Finalizar o programa
                break 
          
