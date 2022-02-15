#Biblioteca Rich https://rich.readthedocs.io/en/stable/
clear_output()
from rich.console import Console
from rich.markdown import Markdown
from rich import print
from rich.table import Table

nome="""
# Infortech 
Prestamos um excelente serviço
- Peças e acessórios
- Manutenção
- Autoatendimento"""
menu="""
# Menu Principal
Digite A para acessar o sistema ou F para finalizar
- A - Acessar
- F - Finalizar
"""
menu2="""
# Efetue suas compras
Digite de 1 a 5 conforme sua opção
1. Lista de produtos
2. Lista de serviços
3. Consultar o carrinho
4. Finalizar compra
5. Voltar para o Menu Principal
"""
menu3="""
# Finalizar a compra

1. Ir para o carrinho
2. Voltar
"""
menu4='''
# Formas de Pagamento
1. Cartão de crédito ou dédito
2. Dinheiro
3. Desistir da compra e limpar o carrinho
4. Voltar'''

menu5='''
# Débito ou Crédito
- C. Crédito
- D. Débito
- V. Voltar para o menu anterior
'''
menu6='''
# Pagamento em dinheiro
- V para voltar
- P para prosseguir com o pagamento
'''

#Variavéis: lista de produtos, serviços, preços e estoque
produtos=('Teclado','Mouse','Memória RAM','Memória HD','Memória SSD','Placa de vídeo','Webcam')
precos_produtos=(10.0,20.0,30.0,40.0,50.0,60.0,70.0)
estoque_produtos=[30,5,2,25,3,5,8]

servicos=('Manutenção de software','Reparos','Formatação','Montagem','Troca de peças')
precos_servicos=(10.0,20.0,30.0,40.0,50.0)

#Carrinho do usuário
carrinho_produtos=[]
quantidade_produto=[]
carrinho_servicos=[]
quantidade_servico=[]
carrinho_concluido=[]
quantidade_concluido=[]
total_carrinho=0.0
total_concluido=0.0
cartao=[]
cedulas=[50,20,10,5,2,1]
troco=[]
controle_pag=False
pagou=False

console = Console()
md = Markdown(nome)
console.print(md)

while True:

    #Controla a entrada do Menu Principal
    while True:
        #Menu Principal
        md = Markdown(menu)
        console.print(md)
        opcao_menu1=input('\nDigite A para acessar o sistema ou F para finalizar: ')
        opcao_menu1=opcao_menu1.upper()
        if(opcao_menu1=='A'or opcao_menu1=='F'):
            break
        else:
            print('Entrada inválida!')

    if(opcao_menu1=='F' and total_concluido==0 and total_carrinho==0): #Saída do sistema quando for realizada nenhuma compra
        print('Obrigado pela visita!')
        break
    elif(opcao_menu1=='F'): #Saída do sistema quando houver compra
        
        if(total_concluido>0): #Saída quando não há débito pendente
            table5=Table(title="Produtos e Serviços adquiridos", show_lines=True)
            table5.add_column("Nº", justify="center", style="cyan", no_wrap=True)
            table5.add_column("Item", style="magenta")
            table5.add_column("Quantidade", style="blue")
            for i in range(len(carrinho_concluido)):
                table5.add_row(str(i+1), carrinho_concluido[i], str(quantidade_concluido[i]) )
            console.print(table5)
            print(f'O total gasto foi: R${total_concluido}')
            if(total_carrinho==0):
                break

        if(total_carrinho>0): #Saída quando há débito pendente
            table6=Table(title="Produtos e Serviços pendentes", show_lines=True)
            table6.add_column("Nº", justify="center", style="cyan", no_wrap=True)
            table6.add_column("Item", style="magenta")
            table6.add_column("Quantidade", style="blue")
            for i in range(len(carrinho_produtos)):
                table6.add_row(str(i+1), produtos[carrinho_produtos[i]], str(quantidade_produto[i]) )
            for i in range(len(carrinho_servicos)):
                table6.add_row(str(i+1), servicos[carrinho_servicos[i]], str(quantidade_servico[i]) )
            console.print(table6)
            print('\nOs produtos listados acima estão pendente de pagamento')
            opcao_menu1=input('Se você deseja voltar e concluir o pagamento digite A ou sair digite F: ')
            opcao_menu1=opcao_menu1.upper()

            if(opcao_menu1=='F'): #Desistência: esvazia o carrinho e encerra o programa
                carrinho_produtos=[]
                quantidade_produto=[]
                carrinho_servicos=[]
                quantidade_servico=[]
                total_carrinho=0.0
                print('Obrigado pela visita')
                break

    #Direcionamento para o menu de compras
    while(opcao_menu1=='A'): 

        #Controle para zerar o carrinho após encerrar uma compra
        if(controle_pag==True and pagou):
            carrinho_produtos=[]
            quantidade_produto=[]
            carrinho_servicos=[]
            quantidade_servico=[]
            total_carrinho=0.0

        #Menu 2
        console.print(Markdown(menu2))

        #Controla a entrada do 'efetue suas compras'
        while True:
            n=input('Digite a opção desejada: ')
            if n.isnumeric():
                opcao_menu2=int(n)
            if(opcao_menu2>=1 and opcao_menu2<=5):
                break
            else:
                print('Entrada inválida!')

        #Entrada do Menu 2
        while(opcao_menu2>=1 and opcao_menu2<=5):
            controle_pag=False

            #Mostra a lista de produtos para o usuário
            clear_output()
            if(opcao_menu2==1):
                table1=Table(title="Produtos", show_lines=True)
                table1.add_column("Nº", justify="center", style="cyan", no_wrap=True)
                table1.add_column("Produto", style="magenta")
                table1.add_column("Preço", style="green")
                tamanho_p=len(produtos)
                for i in range(tamanho_p):
                    table1.add_row(str(i+1), produtos[i], str(precos_produtos[i]))
                console.print(table1)

                print('\nPara comprar um produto digite o número do índice correspondente ou 0 para concluir')

                #Controla a entrada da escolha do usuário
                while True:
                    while True:
                        n=input('Digite o número de sua escolha ou 0 para concluir: ')
                        if(n.isnumeric()):
                            escolha=int(n)
                            if(escolha>=0 and escolha<=tamanho_p):
                                break
                        else:
                            print('Entrada inválida!')

                    #Informe de estoque vazio
                    if(estoque_produtos[escolha-1]==0):
                        print('Lamentamos, esse produto não está mais disponível!')
                        opcao_menu2=1
                        break

                    #Critério de parada da compra de produto (direciona ao menu 3)
                    if(escolha==0): 
                        console.print(Markdown(menu3))
                        while True:
                            n=input('Digite a opção escolhida: ')
                            if n.isnumeric():
                                escolha2=int(n)
                            if(escolha2==1 or escolha2==2):
                                break
                            else:
                                print('Entrada inválida!')
                        if(escolha2==1):
                            opcao_menu2=3
                            break
                        elif(escolha2==2):
                            opcao_menu2=0
                            break
                    else: #Recebe a quantidade de produtos desejados
                        while True:
                            n=input(f'Informe a quantidade que deseja de {produtos[escolha-1]} você deseja comprar: ')
                            if n.isnumeric():
                                quantidade=int(n)
                                if(quantidade<=0): 
                                    print('Informe um valor maior que 0.')
                                elif(quantidade>estoque_produtos[escolha-1]): #Controle de estoque
                                    print(f'A quantidade excedeu o estoque. Temos {estoque_produtos[escolha-1]} unidades desse produto')
                                    print(f'Informe uma quantidade até {estoque_produtos[escolha-1]} unidades.')
                                else:
                                    break

                        #Atualização do estoque e carrinho com agrupamento de itens em comum
                        if(carrinho_produtos.count(escolha-1)>=1): 
                            pos1=carrinho_produtos.index(escolha-1)
                            quantidade_produto[pos1]=quantidade_produto[pos1]+quantidade
                            estoque_produtos[escolha-1]=estoque_produtos[escolha-1]-quantidade
                            total_carrinho=total_carrinho+(precos_produtos[escolha-1]*quantidade)
                        else:
                            estoque_produtos[escolha-1]=estoque_produtos[escolha-1]-quantidade
                            carrinho_produtos.append(escolha-1)
                            quantidade_produto.append(quantidade)
                            total_carrinho=total_carrinho+(precos_produtos[escolha-1]*quantidade)

                    #Valor parcial da compra até o momento
                    print(f'Subtotal de produtos e serviços: R${total_carrinho}\n')


            #Mostra a lista de serviços para o usuário
            elif(opcao_menu2==2):
                table2=Table(title="Serviços", show_lines=True)
                table2.add_column("Nº", justify="center", style="cyan", no_wrap=True)
                table2.add_column("Serviço", style="magenta")
                table2.add_column("Preço", style="green")
                tamanho_s=len(servicos)
                for i in range(tamanho_s):
                    table2.add_row(str(i+1), servicos[i], str(precos_servicos[i]))
                console.print(table2)
                print('\nPara comprar um serviço digite o número do índice correspondente ou 0 para concluir')

                #Validação da escolha do serviço
                while True:
                    while True:
                        n=input('Digite o número de sua escolha ou 0 para concluir: ')
                        if n.isnumeric():
                            escolha=int(n)
                            if(escolha>=0 and escolha<=tamanho_s):
                                break
                        else:
                            print('Entrada inválida!')

                    #Critério de parada da compra de produto (direciona ao menu 3)
                    if(escolha==0):
                        console.print(Markdown(menu3))
                        while True:
                            n=input('Digite a opção escolhida: ')
                            if n.isnumeric():
                                escolha2=int(n)
                                if(escolha2==1 or escolha2==2):
                                    break
                            else:
                                print('Entrada inválida!')
                        if(escolha2==1):
                            opcao_menu2=3
                            break
                        elif(escolha2==2):
                            opcao_menu2=0
                            break
                    else: #Recebe a quantidade de serviços desejados
                        while True:
                            n=input(f'Informe a quantidade que deseja do {servicos[escolha-1]} escolhido: ')
                            if n.isnumeric():
                                quantidade1=int(n)
                                if(quantidade1<=0): #Controle de entrada inválida
                                    n=input('Digite uma quantidade maior que 0')
                                else:
                                    break

                    #Atualização do carrinho e agrupamento de itens em comum
                    if(carrinho_servicos.count(escolha-1)>0):
                        pos2=carrinho_servicos.index(escolha-1)
                        quantidade_servico[pos2]=quantidade_servico[pos2]+quantidade1
                        total_carrinho=total_carrinho+(precos_servicos[escolha-1]*quantidade1)
                        print(f'Subtotal de produtos e serviços: R${total_carrinho}\n')
                    else: #Atualização do carrinho
                        carrinho_servicos.append(escolha-1)
                        quantidade_servico.append(quantidade1)
                        total_carrinho=total_carrinho+(precos_servicos[escolha-1]*quantidade1)
                        print(f'Subtotal de produtos e serviços: R${total_carrinho}\n')

            #Carrinho
            elif(opcao_menu2==3):

                #Tabela de produtos e serviços adicionados ao carrinho
                if(len(carrinho_produtos)>0):
                    table3=Table(title="Carrinho Produtos", show_lines=True)
                    table3.add_column("Nº", justify="center", style="cyan", no_wrap=True)
                    table3.add_column("Produto", style="magenta")
                    table3.add_column("Quantidade", style="blue")
                    table3.add_column("Preço unitário", style="green")
                    table3.add_column("Preço total", style="red")
                    for i in range(len(carrinho_produtos)):
                        precototal=(precos_produtos[carrinho_produtos[i]])*(quantidade_produto[i])
                        table3.add_row(str(i+1), produtos[carrinho_produtos[i]], str(quantidade_produto[i]), "R$"+str(precos_produtos[carrinho_produtos[i]]),"R$"+str(precototal) )
                    console.print(table3)
                if(len(carrinho_servicos)>0):
                    table4=Table(title="Carrinho Serviçoos", show_lines=True)
                    table4.add_column("Nº", justify="center", style="cyan", no_wrap=True)
                    table4.add_column("Serviços", style="magenta")
                    table4.add_column("Quantidade", style="blue")
                    table4.add_column("Preço unitário", style="green")
                    table4.add_column("Preço total", style="red")
                    for i in range(len(carrinho_servicos)):
                        precototal=(precos_produtos[carrinho_servicos[i]])*(quantidade_servico[i])
                        table4.add_row(str(i+1), servicos[carrinho_servicos[i]], str(quantidade_servico[i]), "R$"+str(precos_servicos[carrinho_servicos[i]]),"R$"+str(precototal) )
                    console.print(table4)

                #Saída quando não há itens
                if(len(carrinho_servicos)==0 and len(carrinho_produtos)==0):
                    print('Você ainda não adicionou nenhum item ao carrinho')
                    opcao_menu2=0

                #Valor final de produtos e serviços
                if(len(carrinho_servicos)!=0 or len(carrinho_produtos)!=0):
                    print(f'O valor total é R${total_carrinho}')
                    opcao_menu2=4

            #Finalizar compra
            elif(opcao_menu2==4):

                #Saída quando não há itens
                if(len(carrinho_servicos)==0 and len(carrinho_produtos)==0):
                    print('Você ainda não adicionou nenhum item ao carrinho!')
                    break

                #Controla a entrada do menu 'formas de pagamento' (4)
                while True:
                    console.print(Markdown(menu4))
                    print('\nFormas de pagamento')
                    n=(input('Digite a opção escolhida: '))
                    if n.isnumeric:
                        opcao_menu4= int(n)
                        if(opcao_menu4>=1 and opcao_menu4<=6):
                            break
                    else:
                        print('Entrada inválida!')

                #Cartão de crédito ou débito
                if opcao_menu4==1:
                    while True:
                        console.print(Markdown(menu5))
                        cartao=input('Digite a opção escolhida: ')
                        cartao=cartao.upper()
                        if(cartao=='C'or cartao=='D' or cartao=='V'):
                            break
                        else:
                            print('Entrada inválida!')

                    if(cartao=='C'or cartao=='D'):
                        print('Informe os dados do cartão')
                        cartao_nome=input('Nome: ')
                        cartao_num=input('Número: ')
                        cartao_data=input('Data de validade: ')
                        cartao_cvv=input('CVV: ')

                        if(cartao=='C'):
                            while True:
                                cartao_parcelas=input('Número de parcelas (Máximo 3x sem juros): ')
                                if(cartao_parcelas>'0' and cartao_parcelas<'4'):
                                    break
                                else:
                                    print('Entrada inválida!')
                        controle_pag=True
                    elif(cartao=='V'): #Volta para o menu 'formas de pagamento'
                        controle_pag=False
                        opcao_menu2=4

                #Dinheiro
                elif opcao_menu4==2: 
                    while True:
                        console.print(Markdown(menu6))
                        troca=input('Digite a opção escolhida: ')
                        troca=troca.upper()
                        if(troca=='V' or troca=='P'):
                            break
                        else:
                            print('Entrada inválida!')

                    if(troca=='P'):
                        while True: #Especificação da entrada
                            pagamento=input(f'O valor total é R${total_carrinho}. Para cálculo do troco, informe o valor de entrada:')
                            pagamento=float(pagamento)

                            #Validação do valor de entrada
                            if(pagamento>=total_carrinho):
                                break
                            else:
                                print('Informe um valor igual ou superior ao total da compra')

                        #Definição e controle do troco
                        total_troco=pagamento-total_carrinho
                        pagamento=pagamento-total_carrinho
                        troco=[]

                        #Verificação do menor número de cédulas para o troco
                        for i in cedulas:
                            tr=pagamento//i
                            pagamento=pagamento%i
                            troco.append(tr)
                        a=''
                        if(total_troco>0):
                            for i in range(len(troco)):
                                if(troco[i]>0):
                                    if i<(len(troco)-1):
                                        a=a+(str(int(troco[i]))+" cédula(s) de R$ "+str(cedulas[i]))+", "
                                    else:
                                        a=a+(str(int(troco[i]))+" cédula(s) de R$ "+str(cedulas[i]))+"."
                            print(f'O seu troco é R${total_troco}, disponível em {a}')
                        controle_pag=True
                    elif(troca=='V'): #Volta para o menu 'formas de pagamento'
                        controle_pag=False
                        opcao_menu2=4

                #Controle de pagamento
                if(controle_pag):
                    pagou=True
                    total_concluido=total_carrinho
                    print('Pagamento efetuado com sucesso!')
                    if(len(carrinho_produtos)>0):
                        for i in range(len(carrinho_produtos)):
                            carrinho_concluido.append(produtos[carrinho_produtos[i]])
                            quantidade_concluido.append(quantidade_produto[i])
                    if(len(carrinho_servicos)>0):
                        for i in range(len(carrinho_servicos)):
                            carrinho_concluido.append(servicos[carrinho_servicos[i]])
                            quantidade_concluido.append(quantidade_servico[i])
                    opcao_menu2=0

                #Desistência da compra
                elif opcao_menu4==3: 
                    while True:
                        print('Você está desistindo da compra dos seguintes itens:')
                        if(len(carrinho_produtos)>0):
                            table3=Table(title="Carrinho Produtos", show_lines=True)
                            table3.add_column("Nº", justify="center", style="cyan", no_wrap=True)
                            table3.add_column("Produto", style="magenta")
                            table3.add_column("Quantidade", style="blue")
                            for i in range(len(carrinho_produtos)):
                                precototal=(precos_produtos[carrinho_produtos[i]])*(quantidade_produto[i])
                                table3.add_row(str(i+1), produtos[carrinho_produtos[i]], str(quantidade_produto[i]) )
                            console.print(table3)
                        if(len(carrinho_servicos)>0):
                            table4=Table(title="Carrinho Serviços", show_lines=True)
                            table4.add_column("Nº", justify="center", style="cyan", no_wrap=True)
                            table4.add_column("Serviços", style="magenta")
                            table4.add_column("Quantidade", style="blue")
                            for i in range(len(carrinho_servicos)):
                                precototal=(precos_produtos[carrinho_servicos[i]])*(quantidade_servico[i])
                                table4.add_row(str(i+1), servicos[carrinho_servicos[i]], str(quantidade_servico[i]) )
                            console.print(table4)

                        #Confirmação da desistência
                        while True: 
                            opcao_desistir=input('Digite S se deseja desistir da compra e N para continuar comprando: ')
                            opcao_desistir=opcao_desistir.upper()
                            if(opcao_desistir=='S'or opcao_desistir=='N'):
                                break
                            else:
                                print('Entrada inválida!')
                        if(opcao_desistir=='S'):
                            quantidade_servico=[]
                            carrinho_servicos=[]
                            carrinho_produtos=[]
                            quantidade_produto=[]
                            total_carrinho=0.0
                            total_concluido=0.0
                            print('Carrinho vazio! Siga sua operação através do menu principal!')
                            opcao_menu2=0 #Volta para o menu 'efetue as compras' (2)
                            break
                        elif(opcao_desistir=='N'):
                            opcao_menu2=0 #Volta para o menu 'efetue as compras' (2)
                            print('Carrinho mantido! Siga sua operação através do menu principal!')
                            break
                elif opcao_menu4==4: #Volta para o menu 'efetue as compras' (2)
                    opcao_menu2=0

            #Finalizar o programa
            elif(opcao_menu2==5):
                opcao_menu1='F'
                break
