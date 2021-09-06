from node import Node
# Classe que vamos usar para tratar as exceções.


class ListaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class Lista:

    def __init__(self):
        self._head = None
        self._tamanho = 0

    @property
    def head(self):
        return self._head

    @property
    def tamanho(self):
        return self._tamanho

    def estaVazia(self):
        return True if self._tamanho == 0 else False

    def tamanho(self):
        return self._tamanho

    def elemento(self, posicao):

        try:
            assert posicao > 0
            if (self.estaVazia()):
                raise ListaException('A lista está vazia')

            cursor = self._head
            contador = 1

            while ((cursor != None) and (contador < posicao)):
                cursor = cursor.prox
                contador += 1

            if (cursor != None):
                return cursor.dado

            raise ListaException('A posiçao é inválida para a lista')

        except TypeError:
            raise ListaException(
                'O argumento posição deve ser um valor do tipo inteiro')
        except AssertionError:
            raise ListaException('Posição negativa não é válida para a lista')
        except:
            raise

    def busca(self, valor):

        if (self.estaVazia()):
            raise ListaException('A lista está vazia')

        cursor = self._head
        contador = 1

        while (cursor != None):
            if(cursor.dado == valor):
                return contador

            cursor = cursor.prox
            contador += 1
        raise ListaException('O valor informado na busca nao está na lista')

    def inserir_inicio(self, posicao, dado):

        try:
            assert posicao > 0

            # CONDICAO 1: insercao se a lista estiver vazia
            if (self.estaVazia()):
                if (posicao != 1):
                    print('Entrei no posicao = 1')
                    raise ListaException(
                        f'A lista esta vazia. A posicao correta para insercao é 1.')

                self._head = Node(dado)
                self._tamanho += 1
                return

            # CONDICAO 2: insercao na primeira posicao em uma lista nao vazia
            if (posicao == 1):
                novo = Node(dado)
                novo.prox = self._head
                self._head = novo
                self._tamanho += 1
                return

        except TypeError:
            raise ListaException(
                'O argumento posição deve ser um valor do tipo inteiro')
        except AssertionError:
            raise ListaException('Posição negativa não é válida para a lista')

    def inserir_final(self, valor):
        self.vetor.append(valor)

    def trocar_ordem(self, posicao_elem_1, posicao_elem_2):
        try:
            assert posicao_elem_1 > 0

            if (self.estaVazia()):
                raise ListaException('Lista vazia. Não é possível remover')

            cursor = self._head
            contador = 1

            while((cursor != None) and (contador < posicao_elem_1)):
                cursor = cursor._prox
                contador += 1

            if(cursor != None):
                cursor.dado = posicao_elem_2
                return

            raise ListaException('Posição inválida para a lista')

        except TypeError:
            raise ListaException(
                'O argumento posição deve ser um valor do tipo inteiro')
        except AssertionError:
            raise ListaException('Posição negativa não é válida para a lista')

    def remover_final(self):
        pass

    def imprimir_lista(self):
        print(self.__repr__())

    def remover_inicio(self, posicao):
        try:
            assert posicao > 0
            if (self.estaVazia()):
                raise ListaException('Lista vazia. Não é possível remover')

            cursor = self._head
            contador = 1

            while((contador <= posicao-1) and (cursor != None)):
                anterior = cursor
                cursor = cursor._prox
                contador += 1

            if (cursor == None):
                raise ListaException('Posição inválida para remoção')

            dado = cursor.dado

            if(posicao == 1):
                self._head = cursor._prox

            else:
                anterior._prox = cursor._prox

            self._tamanho -= 1

            return dado
        except TypeError:
            raise ListaException(
                'O argumento posição deve ser um valor do tipo inteiro')
        except AssertionError:
            raise ListaException('Posição negativa não é válida para a lista')

    def remove_todos(self):
        self.vetor.clear()

    def __str__(self):
        str = 'Lista: [ '
        cursor = self._head
        while(cursor != None):
            str += f'{cursor.dado}'
            cursor = cursor.prox
            if(cursor != None):
                str += ', '
        str += ']'
        return str
