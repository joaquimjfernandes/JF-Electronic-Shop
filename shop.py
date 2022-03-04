print('=' * 50)
print(f'\033[1;32m{"JF Electronic Shop":^50}\033[m')
print('=' * 50)
# --------------- Variáveis ---------------
produtos = {'Computador Asus': 320000,
            'Teclado': 3500,
            'Mouse': 2500,
            'Pendrive': 4000,
            'Monitor': 20000,
            'CPU HP i3': 80000,
            'CPU HP i5': 120000,
            'Smart Watch': 25000,
            'Base de PC i7': 95000,
            'Processador i3 Intel': 15000,
            'Processador i5 NVIDIA': 20000,
            'Ipad': 30000}
func = list()
NomeComprador = str(input('Seu Nome: '))
totalproduto = troco = dinheiro = totalcompra = totpagar = 0
# --------------- Inicio ------------------
print('\033[1;32mSejá Bem Vindo a Nossa Loja, Oque Deseja Comprar??\033[m')
# --------------- Corpo ---------------
while True:
    print('-' * 50)
    print('''[1] Selecionar Produtos
[2] Pagar Conta
[3] Pra Vaga de Emprego
[4] Sair da Loja''')
    opcao = int(input('Oque Deseja: '))
    if opcao == 1:
        for pos in range(0, 5):
            escolha = str(input('Nome do Produto: '))
            dinheiro = int(input('Valor do Produto: '))
            if escolha not in produtos:
                print('Sentimos muito, não Temos esse Produto em nosso Stock')
            else:
                print('Produto adicionado, em suas Compras!')
                totalproduto += 1
                troco = dinheiro
                troco += dinheiro
        print(f'No total foram {totalproduto} Produtos Adicionado no Carrinho.')
    elif opcao == 2:
        print(f'Foram {totalproduto} Comprados')
        print(f'O Total a Pagar: {dinheiro}')
        totpagar = int(input('Valor Recebido: '))
        troco = totpagar - dinheiro
        print(f'Troco: {troco}')
    elif opcao == 3:
        print('-' * 50)
        print('FICHA DE CADASTRAMENTO')
        func.append(input('Nome Completo: '))
        func.append(int(input('Ano de Nascimento: ')))
        func.append(input('Nacionalidade: '))
        func.append(int(input('Nº de Telefone:')))
        func.append(input('Graduação: '))
        print('-' * 50)
        print('FUNCIONÁRIO CADASTRADO!')
        print('BEM VINDO A EQUIPE!')
        print('-' * 50)
    elif opcao == 4:
        print('-' * 50)
        print(f'Nome do Cliente: {NomeComprador}')
        print('-' * 50)
        print('''        For any Service, Please Call us: 943034157
            email: shopjfelectronic@gamil.com
            Processado por Programa Shop's Simulator
            Luanda (Cacuaco) Electronic Shop
            Obrigado, Volte Sempre!''')
        print('-' * 50)
        break
