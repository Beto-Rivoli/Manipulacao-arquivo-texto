def criar():
    try:
        nome = input('Digite o nome do arquivo: ')
        arquivo = open(f'{nome}.html', 'w')
        arquivo.write(f'<html>\n')
        arquivo.write(f'    <head>\n')
        nome = input('Digite o Título: ')
        arquivo.write(f'        <title>"{nome}"</title>\n')
        while True:
            var = input('Escreva uma linha para o "head": ')
            arquivo.write(f'        {var}\n')
            if input(
                    'Deseja adicionar outra linha? Digite s para continuar ou qualquer tecla para cancelar: ') != 's':
                break

        arquivo.write(f'    </head>\n')
        arquivo.write(f'    <body>\n')
        while True:
            var = input('Escreva uma linha para o "body": ')
            arquivo.write(f'        {var}\n')
            if input(
                    'Deseja adicionar outra linha? Digite s para continuar ou qualquer tecla para cancelar: ') != 's':
                break
        arquivo.write(f'    </body>\n')
        arquivo.write(f'</html>')

        arquivo.close()
        return 1
    except Exception as erro:
        print(erro)
        return 0

if criar() == 0:
    print('\nERRO AO CRIAR O ARQUIVO')
