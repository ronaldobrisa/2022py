"""
FAÇA UM PROGRAMA QUE PEÇA AO USUÁRIO DIGITAR UM NÚMERO INTEIRO
INFORME SE ESTE NÚMERO É PAR OU IMPAR. CASO O USUÁRIO NÃO DIGITE UM NÚMERO INTEIRO
INFORME QUE NÃO É UM NÚMERO INTEIRO

passo1 = input('Digite um número inteiro: ')

#isnumeric isdigit isdecimal
#print(passo1.isnumeric())

if passo1.isnumeric():
    passo1 = int(passo1)
    if passo1 % 2 == 0:
        print(f'{passo1} é PAR!')
    else:
        print(f'{passo1} é ÍMPAR!')
else:
    print('Isto não é um número inteiro!')
"""
"""
FAÇA UM PROGRAMA QUE PERGUNTE A HORA AO USUÁRIO E BASEANDO-SE NO HORÁRIO DESCRITO
EXIBA A SAUDAÇÃO APROPRIADA. EXEMPLO: 
BOM DIA 0-11, BOA TARDE 12-17, BOA NOITE 18-23
"""
"""
hora = input('Digite um horário (0-23): ')

if hora.isdigit():
    hora = int(hora)

    if hora < 0 or hora > 23:
        print('Horário deve estar entre 0 e 23')
    else:
        if hora >= 0 and hora<= 11:
            print('Bom dia')
        elif hora > 11 and hora <= 17:
            print('Boa tarde')
        else:
            print('Boa noite')
"""
"""
FAÇA UM PROGRAMA QUE PEÇA O PRIMEIRO NOME DO USUÁRIO. SE O NOME TIVER 4 LETRAS OU MENOS
ESCREVA "SEU NOME É CURTO"; SE TIVER ENTRE 5 E 6 LETRAS, ESCREVA "SEU NOME É NORMAL"; 
MAIOR QUE 6 ESCREVA "SEU NOME É MUITO GRANDE"
"""
nome = input('Digite o seu primeiro nome: ')
tamanho = len(nome)

if tamanho <= 4:
    print('Seu nome é muito curto!')
elif tamanho <= 6:
    print('Seu nome é normal!')
else:
    print('Seu nome é muito grande!')
