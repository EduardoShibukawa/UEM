import sys
from operator import itemgetter

INFINITO = sys.maxsize
class TSPU:
    def __init__(self):
        self.matriz = []
        self.numerolinhas = 0
        self.numerocolunas = 0
        self.memo = []
        self.caminhominimo = (-1, INFINITO)

    def gerarmatriz(self, nome_arquivo):
            linha = arquivo.readline()
            header = linha.split(" ")
            self.numerolinhas = int(header[0])
            self.numerocolunas = int(header[1])
            for n in range(0, self.numerolinhas):
                linha = arquivo.readline()
                linha = linha.split(" ")

                linha_tsp = []
                for m in range(0, self.numerocolunas):
                    linha_tsp.append(int(linha[m]))
                self.matriz.append(linha_tsp)

    def __getindicelinhavalido(self, indice_linha):
        if indice_linha == -1:
            return self.numerolinhas - 1
        else:
            return indice_linha % self.numerolinhas

    def __buscarcaminhominimo(self, indice_linha, indice_coluna):
        if indice_coluna == 0:
            self.memo[indice_linha][indice_coluna] = (-1, self.matriz[indice_linha][indice_coluna])
        else:
            if self.memo[indice_linha][indice_coluna] == INFINITO:
                possiveiscaminhos = [
                    (
                        self.__getindicelinhavalido(indice_linha - 1),
                        self.__buscarcaminhominimo(self.__getindicelinhavalido(indice_linha - 1), indice_coluna - 1)
                    ),
                    (
                        self.__getindicelinhavalido(indice_linha + 1),
                        self.__buscarcaminhominimo(self.__getindicelinhavalido(indice_linha + 1), indice_coluna - 1)
                    ),
                    (
                        indice_linha,
                        self.__buscarcaminhominimo(self.__getindicelinhavalido(indice_linha), indice_coluna - 1)
                    )
                ]

                caminhominimo = min(possiveiscaminhos, key=itemgetter(1))
                self.memo[indice_linha][indice_coluna] = (
                    caminhominimo[0],
                    self.matriz[indice_linha][indice_coluna] + caminhominimo[1]
                )
        return self.memo[indice_linha][indice_coluna][1]

    def gerarcaminhominimo(self):
        for indice_linha in range(0, self.numerolinhas):
            self.memo.append([])
            for indice_coluna in range(0, self.numerocolunas):
                self.memo[indice_linha].append(INFINITO)

        for indice_linha in range(0, self.numerolinhas):
            custo = self.__buscarcaminhominimo(indice_linha, self.numerocolunas -1)
            if (custo < self.caminhominimo[1]):
                self.caminhominimo = self.memo[indice_linha][indice_coluna]

    def printcaminhominimo(self):
        caminho = []
        indice_coluna = self.numerocolunas - 1
        indice_linha = self.caminhominimo[0]
        while indice_coluna != -1:
            indice_linha = self.memo[indice_linha][indice_coluna][0]
            if indice_linha != -1:
              caminho.append(indice_linha + 1)
            indice_coluna -= 1
        print(' '.join(str(e) for e in caminho[::-1]))
        print(self.caminhominimo[1])

def main():
    nome_arquivo = 'E:\\Duh\\UEM\\PAA\\tsp\\in\\tsp16.txt'
    tspu = TSPU()
    tspu.gerarmatriz(nome_arquivo)
    tspu.gerarcaminhominimo()
    tspu.printcaminhominimo()

if __name__ == '__main__':
    main()
