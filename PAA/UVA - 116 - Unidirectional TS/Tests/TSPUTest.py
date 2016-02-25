import unittest
import os
import re
from TSPU import TSPU


def atoi(text):
    return int(text) if text.isdigit() else text


def natural_keys(text):
    """
    :param text:
        list.sort(key=natural_keys) sorts in human order
        http://nedbatchelder.com/blog/200712/human_sorting.html
        (See Toothy's implementation in the comments)
    """
    return [atoi(c) for c in re.split('(\d+)', text)]


class TSPUTest(unittest.TestCase):
    def testFun(self):
        for file in sorted(os.listdir("..//in"), key=natural_keys):
            if file.endswith(".txt"):
                arquivo_saida_esperada = open('..//out//{name}'.format(name=file), 'r')
                tspu = TSPU()
                tspu.gerar_matriz('..//in//{name}'.format(name=file))
                tspu.gerar_caminho_minimo()
                caminho_esperado = arquivo_saida_esperada.read().strip()
                self.assertEqual(
                    tspu.output_caminho_minimo(),
                    caminho_esperado,
                    '\nArquivo: {nome_arquivo}'
                    '\nSaida: \n{saida}'
                    '\nEsperado: \n{esperado}'.format(
                        nome_arquivo=file,
                        saida=tspu.output_caminho_minimo(),
                        esperado=caminho_esperado
                    )
                )


if __name__ == '__main__':
    unittest.main()
