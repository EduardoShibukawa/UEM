import os
import re
import time

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


def main():
    """
      Execução dos arquivos da past .//in//*.txt
    """
    for file in sorted(os.listdir(".//in"), key=natural_keys):
        if file.endswith(".txt"):
            try:
                arquivo_saida_esperada = open('.//out//{name}'.format(name=file), 'r')
                tspu = TSPU()
                ini = time.time()
                tspu.gerar_matriz('.//in//{name}'.format(name=file))
                tspu.gerar_caminho_minimo()
                fim = time.time()
                print('------------------------')
                print('Arquivo: {arquivo}\nTempo Exec: {tempo}'.format(
                    arquivo=file,
                    tempo=fim-ini
                ))
                print('---------SAIDA----------')
                print(tspu.output_caminho_minimo())
                print('---------ESPERADO-------')
                print(arquivo_saida_esperada.read().strip())
            except Exception as exception:
                print(exception)

    print('Pressione qualquer tecla para sair.')
    input()

if __name__ == '__main__':
    main()
