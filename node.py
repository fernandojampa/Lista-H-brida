# Classe Node que é responsável pelo encadeamento das listas
class Node:
    def __init__(self, dado):
        self._dado = dado
        self._prox = -1


@property
def dado(self):
    return self._dado


@property
def prox(self):
    return self._prox


@dado.setter
def dado(self, novoDado):
    self._dado = novoDado


@prox.setter
def prox(self, novoProx):
    self._prox = novoProx


def __str__(self):
    return self._dado
