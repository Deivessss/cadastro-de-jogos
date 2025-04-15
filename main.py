def arquivo_existe_criar(arq):
    try:
        with open(arq,'r') as arquive:
            return True
    except:
        with open(arq,'wt+') as arquive:
            print(f'Arquivo {arq} criado')

def input_int(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 0:
                print('Erro. Digite um número inteiro válido (não digite números negativos).')
                continue
            else: return n
        except:
            print('Erro. Digite um número inteiro válido (não digite números negativos).')


arquivo_existe_criar('jogos_python.txt')

while True:
    menu = input_int('1 - Cadastrar novo item\n'
                     '2 - Mostrar lista\n'
                     '3 - Sair\n'
                     'Sua escolha: ')

    if menu == 1:
        print('Cadastrar novo item: ')
        jogo = input('Nome do jogo: ')
        v_game = input('Videogame: ')
        with open('jogos_python.txt', 'at') as arquivo:
            arquivo.write(f'{jogo};{v_game}\n')            
            #pulo uma linha, para quando for registrar um jogo novo, já ir para a linha 2.

    elif menu == 2:
        print('Mostrar lista: ')
        with open('jogos_python.txt', 'rt') as a:
            for linha in a:
                dado = linha.split(';')
                print(f'Jogo: {dado[0]:<25}Plataforma: {dado[1]:>3}')

    elif menu == 3:
        print('Saindo do programa...')
        break
