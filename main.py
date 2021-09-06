from ListaHibrida import Lista
from ListaHibrida import ListaException


if __name__ == "__main__":
    # Instâncias da classe Lista
    l1 = Lista()
    l2 = Lista()
    l3 = Lista()
    l4 = Lista()
    l5 = Lista()

    # definição da lista padrão (1)
    listaAtual = l1

    # aqui é apenas um id que fica no top da lista para identicar em qual lista estamos.
    if listaAtual == l1:
        id = 1
    elif listaAtual == l2:
        id = 2
    elif listaAtual == l3:
        id = 3
    elif listaAtual == l4:
        id = 4
    elif listaAtual == l5:
        id = 5

    # Menu
    print('      ------------------------------------------')
    print(f'      Lista [{id}]')
    print('      ------------------------------------------')
    print(''' 
      (i) Inserir no início
      (f) Inserir no final
      (b) Procurar um valor na lista
      (e) Consultar o conteúdo de um elemento
      (t) Trocar ordem dos elementos
      (v) Consultar se a lista está vazia
      (s) Obter o tamanho da lista
      (r) Remover do início
      (o) Remover do final
      (l) Remover todos os elementos da lista
      (p) Imprimir lista
      (m) Mudar a lista
      (x) Sair do programa
      ''')
    # input do menu
    opcao = input()
    while True:
        # Cadeia de ifs de acordo com as opções do menu
        if opcao == 'i':

            posicao = int(input('Informe a posicao a ser inserido: '))
            valor = int(input('Informe o valor a ser inserido: '))
            listaAtual.inserir_inicio(posicao, valor)

        if opcao == 'f':
            try:
                valor = int(input('Informe o valor a ser inserido: '))
                listaAtual.inserir_final(valor)
            except TypeError:
                raise ListaException('Informe um valor do tipo Inteiro')
            except IndexError:
                raise ListaException(
                    'Posição informada para consulta é inválida')
            except AssertionError:
                raise ListaException(
                    'Posição negativa não é válida para a lista')
            except ValueError:
                raise ListaException('Valor não encontrado')

        if opcao == 'b':
            try:
                valor = int(input('Informe o valor a ser pesquisado: '))
                print(listaAtual.busca(valor))
            except TypeError:
                raise ListaException('Informe um valor do tipo Inteiro')
            except IndexError:
                raise ListaException(
                    'Posição informada para consulta é inválida')
            except AssertionError:
                raise ListaException(
                    'Posição negativa não é válida para a lista')
            except ValueError:
                raise ListaException('Valor não encontrado')

        if opcao == 'e':
            try:
                valor = int(input('Informe o valor do índice: '))
                print(listaAtual.elemento(valor))
            except TypeError:
                raise ListaException('Informe um valor do tipo Inteiro')
            except IndexError:
                raise ListaException(
                    'Posição informada para consulta é inválida')
            except AssertionError:
                raise ListaException(
                    'Posição negativa não é válida para a lista')
            except ValueError:
                raise ListaException('Valor não encontrado')

        if opcao == 'v':
            print(listaAtual.estaVazia())

        if opcao == 's':
            print(listaAtual.tamanho())

        if opcao == 'r':
            posicao = int(input('Informe a posição: '))
            listaAtual.remover_inicio(posicao)

        if opcao == 'o':
            listaAtual.remover_final()
            print('Removido')

        if opcao == 'l':
            listaAtual.remove_todos()
            print('Todos os elementos removidos!')

        if opcao == 'p':
            print(listaAtual.imprimir_lista())

        if opcao == 'm':
            print('''
      1 - Lista 1
      2 - Lista 2
      3 - Lista 3
      4 - Lista 4
      5 - Lista 5
            ''')
            mudarLista = int(input('Escolha a nova lista: '))
            # Aqui escolhemos qual lista vamos trabalhar de acordo com a opção 'm'
            if mudarLista == 1:
                listaAtual = l1
            elif mudarLista == 2:
                listaAtual = l2
            elif mudarLista == 3:
                listaAtual = l3
            elif mudarLista == 4:
                listaAtual = l4
            elif mudarLista == 5:
                listaAtual = l5

        if opcao == 'x':
            break

        if listaAtual == l1:
            id = 1
        elif listaAtual == l2:
            id = 2
        elif listaAtual == l3:
            id = 3
        elif listaAtual == l4:
            id = 4
        elif listaAtual == l5:
            id = 5

        print('      ------------------------------------------')
        print(f'      Lista [{id}]')
        print('      ------------------------------------------')
        print(''' 
      (i) Inserir no início
      (f) Inserir no final
      (b) Procurar um valor na lista
      (e) Consultar o conteúdo de um elemento
      (t) Trocar ordem dos elementos
      (v) Consultar se a lista está vazia
      (s) Obter o tamanho da lista
      (r) Remover do início
      (o) Remover do final
      (l) Remover todos os elementos da lista
      (p) Imprimir lista
      (m) Mudar a lista
      (x) Sair do programa
      ''')
        opcao = input()
