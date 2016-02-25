import sys
from operator import attrgetter
INFINITO = sys.maxsize


class ErroGeracaoMatriz(Exception):
    def __init__(self, valor):
        self.valor = 'Erro na geração de matriz!, {erro}! '.format(erro=valor)

    def __str__(self):
        return repr(self.valor)


class Caminho:
    def __init__(self, indice_pai, custo):
        self.indicePai = indice_pai
        self.custo = custo


class TSPU:
    def __init__(self):
        self.matriz = []
        self.numeroLinhas = 0
        self.numeroColunas = 0
        self.memo = []
        self.caminhoMinimo = Caminho(INFINITO, INFINITO)

    def gerar_matriz(self, nome_arquivo):
        try:
            with open(nome_arquivo) as arquivo:
                linha = arquivo.readline()
                header = linha.split(" ")
                self.numeroLinhas = int(header[0])
                self.numeroColunas = int(header[1])
                for n in range(0, self.numeroLinhas):
                    linha = arquivo.readline()
                    linha = linha.split(" ")

                    linha_tsp = []
                    for m in range(0, self.numeroColunas):
                        linha_tsp.append(int(linha[m]))
                    self.matriz.append(linha_tsp)
        except Exception as exception:
            raise ErroGeracaoMatriz(exception)

    def __get_indice_linha_valido(self, indice_linha):
        if indice_linha == -1:
            return self.numeroLinhas - 1
        else:
            return indice_linha % self.numeroLinhas

    def __buscar_caminho_minimo(self, indice_linha, indice_coluna):
        if self.memo[indice_linha][indice_coluna] == INFINITO:
            if indice_coluna == 0:
                self.memo[indice_linha][indice_coluna] = Caminho(-1, self.matriz[indice_linha][indice_coluna])
            else:
                possiveis_caminhos = [
                    Caminho(
                        self.__get_indice_linha_valido(indice_linha - 1),
                        self.__buscar_caminho_minimo(self.__get_indice_linha_valido(indice_linha - 1),
                                                     indice_coluna - 1)
                    ),
                    Caminho(
                        self.__get_indice_linha_valido(indice_linha + 1),
                        self.__buscar_caminho_minimo(self.__get_indice_linha_valido(indice_linha + 1),
                                                     indice_coluna - 1)
                    ),
                    Caminho(
                        indice_linha,
                        self.__buscar_caminho_minimo(indice_linha, indice_coluna - 1)
                    )
                ]

                caminho_minimo = min(possiveis_caminhos, key=attrgetter('custo'))
                self.memo[indice_linha][indice_coluna] = Caminho(
                    caminho_minimo.indicePai,
                    self.matriz[indice_linha][indice_coluna] + caminho_minimo.custo
                )
        return self.memo[indice_linha][indice_coluna].custo

    def gerar_caminho_minimo(self):
        for indice_linha in range(0, self.numeroLinhas):
            self.memo.append([])
            for indice_coluna in range(0, self.numeroColunas):
                self.memo[indice_linha].append(INFINITO)

        for indice_linha in range(0, self.numeroLinhas):
            custo = self.__buscar_caminho_minimo(indice_linha, self.numeroColunas - 1)
            if custo < self.caminhoMinimo.custo:
                self.caminhoMinimo.indicePai = indice_linha
                self.caminhoMinimo.custo = self.memo[indice_linha][self.numeroColunas - 1].custo

    def output_caminho_minimo(self):
        caminho = [self.caminhoMinimo.indicePai + 1]
        indice_coluna = self.numeroColunas - 1
        indice_linha = self.caminhoMinimo.indicePai
        while indice_coluna != -1:
            indice_linha = self.memo[indice_linha][indice_coluna].indicePai
            indice_coluna -= 1
            if indice_linha != -1:
                caminho.append(indice_linha + 1)
        return "{caminho}\n{custo}".format(
            caminho=' '.join(str(e) for e in caminho[::-1]),
            custo=self.caminhoMinimo.custo
        )
