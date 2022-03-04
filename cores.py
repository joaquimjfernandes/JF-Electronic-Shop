a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7:30m'}
nome = 'Joaquim'
print('Muito prazer em te conhecer, {}{}{}!'.format(cores['amarelo'], nome, cores['limpa']))
