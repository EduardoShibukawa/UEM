class Tabuleiro:
    def __init__(self, valor):
        self.valor = []
        self.tamanho = 4
        for i in range(0, self.tamanho):
            self.valor([])
            for i in range(0, self.tamanho):
                self.valor.append([])

    def getvalorpeca(self, x, y):
        return self.valor[x][y]

    def __str__(self):
        return " ".join(str(v) for r in self.valor for v in r)

