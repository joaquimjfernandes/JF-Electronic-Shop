opcao = int(input('Qual é a sua Opção? '))
print('-' * 50)
print(f'\033[1;32m{"Tabela Produtos":^50}\033[m')
print('-' * 50)
# --------------- Laços ---------------
# for item in range(0, len(produtos)):
# if item % 2 == 0:
# print(f'\033[1;34m{produtos[item]:.<30}', end='')
# else:
# print(f'{produtos[item]:>7}kz\033[m')
cores = {'limpa': '\033[m',
         'azul': '\033[1;34m',
         'amarelo': '\033[1;33m',
         'verde': '\033[1;32m',
         'pretoebranco': '\033[7:30m'}
if opcao == 1:
    compradorNome = str(input('Qual é o seu Nome? '))
    # comprador = str(input('Oque Desejas Comprar: '))
    cont = str(input('Quer Continuar?[s/n] '))
    while cont not in 'Nn':
        compra = str(input('Oque Desejas Comprar: '))
        custo = int(input('Valor do Produto: '))
        if compra not in produtos:
            print('Sentimos Muito, Não temos esse Produto!')
        else:
            print('Produto adicionado no Carrinho de Compras!!')
            itemcompra += 1
            # totcompra += compra
        paga = str(input('Pagar ou Continuar?[P/C] '))
        if paga == 'Pp':
            dinheiro = int(input('Pagando: '))
            troco = custo - dinheiro
            print(f'Você comprou {compra} Produtos no valor de {totcompra}')
            print(f'Pagaste {dinheiro} nas Compras efetuadas, o seu troco é de {troco}')
elif opcao == 3:
    print('-' * 50)
    # print(f'Nome do Cliente: {compradorNome}')
    print('-' * 50)
    print('''        For any Service, Please Call us: 943034157
    email: shopjfelectronic@gamil.com
    Processado por Programa Shop's Simulator
    Luanda (Cacuaco) Electronic Shop
    Obrigado, Volte Sempre!''')
    print('-' * 50)