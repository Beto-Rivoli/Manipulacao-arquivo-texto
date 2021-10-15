from prettytable import PrettyTable
import mysql.connector

def abrebanco():
    try:
        global conexao
        global comandosql

        conexao = mysql.connector.Connect(host='localhost', database='univap', user='root', password='')
        if conexao.is_connected():
            informacaobanco = conexao.get_server_info()
            print(f'Conectado ao servidor banco de dados - Versão {informacaobanco}')
            print('Conexão ok')

            comandosql = conexao.cursor()
            comandosql.execute('select database();')
            nomebanco = comandosql.fetchone()
            print(f'Banco de dados acessado = {nomebanco[0]}')
            print('=' * 80)
            return 1
        else:
            print('Conexão não realizada com banco')
            return 0
    except Exception as erro:
        print(f'Erro : {erro}')
        return 0

def contar():
    try:
        comandosql.execute(f'select count(*) from professores;')
        tabela = comandosql.fetchone()
        return tabela

    except Exception as erro:
        return 0

def nomes(profs):
    try:
        if profs == 0:
            print('Não há professores cadastrados')
        else:
            nomes = list()
            comandosql = conexao.cursor()
            comandosql.execute(f'select nomeprof from professores;')
            tabela = comandosql.fetchall()
            if comandosql.rowcount > 0:
                for r in tabela:
                    nomes.append(r[0])
            for y in range(0, profs):
                arquivotexto = open(f'{nomes[y]}.html', 'w')
                arquivotexto.write(f'<html>\n   <head>\n        <title>{nomes[y]}')
                arquivotexto.write(f'</title>\n  </head>\n  <body>\n')
                arquivotexto.write(f'       Disciplinas do professor: {nomes[y]}<br>\n')
                comandosql.execute(
                    f'select curso from disciplinasxprofessores inner join disciplinas '
                    f'on disciplinasxprofessores.coddisciplina= disciplinas.codigodisc inner join professores '
                    f'on professores.registro = disciplinasxprofessores.codprofessor where professores.nomeprof = "{nomes[y]}";')
                tabela = comandosql.fetchall()
                lista = list()
                lista.append(tabela[0][0])
                repeticoes = 0
                if comandosql.rowcount > 0:
                    for r in tabela:
                        if repeticoes == 0 or r[0] not in lista:
                            comandosql.execute(f'select coddisciplina, nomedisc from disciplinasxprofessores inner join '
                                               f'disciplinas on disciplinasxprofessores.coddisciplina= disciplinas.codigodisc '
                                               f'where curso = "{r[0]}"')
                            cursosiguais = comandosql.fetchall()
                            comandosql.execute(f'select count(*) from disciplinasxprofessores where curso = {r[0]};')
                            contadoriguais = comandosql.fetchall()
                            arquivotexto.write(f'\n     <br>Curso: {r[0]}<br>\n')

                            for cont in range(0, contadoriguais[0][0]):
                                arquivotexto.write(f'       {cursosiguais[cont][0]} | {cursosiguais[cont][1]}<br>\n')

                            if r[0] not in lista:
                                lista.append(r[0])

                        repeticoes += 1
                arquivotexto.write(f'\n    </body> \n</html>')
                arquivotexto.close()
                del lista
            comandosql.close()
            conexao.close()

    except Exception as erro:
        print(f'Ocorreu erro: {erro}')
conexao.close()


if abrebanco() == 1:
    quant = contar()
    nomes(quant[0])


else:
    print('FIM DO PROGRAMA!!! Algum problema existente na conexão com banco de dados.')
