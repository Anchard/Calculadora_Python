def erro():
    print('Entre com os comandos da maneira correta')
    print('Exemplo: Número Operação Número Operação Número...')
    print('Os espaços são estritamente necessários\n')
    
#Na minha lógica a estrutura do comando do usuário necessita
#no índice par possuir um número e no índice ímpar possuir uma operação
def verificador(lista):
    operacoes = ['+', '-', '/', '*', '**']
    
    for i in range(len(lista)):
        if i % 2 == 0:
            if not lista[i].isnumeric():
                erro()
                return False
            
        else:
            if lista[i] not in operacoes:
                erro()
                return False

    return True

def leitor():
    print('Entrada do usuário: ', end = '')
    entrada = input()
    print()

    if entrada.lower() == 'exit':
        return -1
    
    entrada = entrada.split()

    while verificador(entrada) == False:
        print('Entrada do usuário: ', end = '')
        entrada = input()
        print()
        entrada = entrada.split()
    
    return entrada

def menu():
    print('Instruções de utilização: ')
    print('Digite um número, a operação suportada e outro número')
    print('Exemplo: 32 + 15 - 10')
    print('Operações suportadas: +, -, *, /, **')
    print('Para sair digite: exit\n')

def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def potenciacao(x, f):
    return x ** f

#removo os tokens adicionados com a efetuação das operações prioritárias
def renova_lista(lista):
    nova_lista = []

    for i in range(len(lista)):
        if lista[i] != '@':
            nova_lista.append(lista[i])

    return nova_lista

def efetua_contas(lista, operador):
    qtde = lista.count(operador)
    for i in range(qtde):
        for j in range(1, len(lista)):
            if lista[j] == operador:
                resultado = eval(lista[j - 1] + operador + lista[j + 1])
                lista[j - 1] = '@'
                lista[j] = str(resultado)
                lista[j + 1] = '@'
                lista = renova_lista(lista)
                break

    return lista

#realizo as operações prioritárias e adiciono um token '@' para manter
#a estrutura funcional da lista
def calculadora():
    prioridade = ['**', '*', '/', '+', '-']
    menu()

    lista = leitor()
    while lista != -1:
        
        for i in range(5):
            lista = efetua_contas(lista, prioridade[i])

        print('Resultado:', lista[0])
        print()
        
        lista = leitor()

    print('Obrigado por utilizar\n')

calculadora()
