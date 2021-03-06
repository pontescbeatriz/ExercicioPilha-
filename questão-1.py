class Stack:
    def __init__(self):
        self._itens = list()

    def isVazio(self):
        return len(self._itens)==0

    def peek(self):
        return self._itens[-1]

    def pop(self):
        if self.isVazio():
            return False
        return self._itens.pop()

    def push(self, item):
        return self._itens.append(item)

    def lenght(self):
        return len(self._itens())
