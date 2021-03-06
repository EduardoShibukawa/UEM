#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

#define NUM_FILAS 5
#define NUM_CLIENTES 100000

int clientes[NUM_CLIENTES];
int tamanhoFila[NUM_FILAS];
int indiceCliente;
int quantidadeZeros;

/// <summary>
/// Encontra a quantidade de algarismos o valor possui.
/// </summary>
/// <param name="valor" type="int">Valor do inteiro a ser calculado.</param>
/// <returns>Retorna o tamanho, quantidade, de algarismos o valor informado possui.</returns>
int tamanhoDigito(int valor)
{
    int tamanho = 1;
    if (valor == 0)
        return tamanho;

    for (tamanho = 0; valor > 0; valor /= 10)
        tamanho++;

    return tamanho;
}

/// <summary>
/// Cria um identificador para o cliente.
/// </summary>
/// <returns>Retorno, um inteiro, o identificador criado para o cliente.</returns>
int gerarIdCliente()
{
    return (rand() % NUM_CLIENTES) + 1;
}

/// <summary>
/// Método que informa em qual caixa o cliente será atendido.
/// </summary>
/// <param name="idClienteAtendido" type="int">Identificador do cliente a ser atendido.</param>
/// <param name="idFilaAtendido" type="int">Identificador da fila no qual o cliente foi atendido.</param>
void atenderCliente(int idClienteAtendido, int idFilaAtendido)
{
    printf("Cliente %0*d recebendo atendimento no caixa %0*d.\n", quantidadeZeros, idClienteAtendido, quantidadeZeros, idFilaAtendido);
}

/// <summary>
/// Recupera o identificador da fila menos populada
/// </summary>
/// <returns>Retorna, um inteiro, o identificador da fila menos populada encontrada.</returns>
int recuperarFilaMenor()
{
    int idFilaMenor = 0;
    int contador;
    if (tamanhoFila[idFilaMenor] > 0)
        for (contador = 1; contador < NUM_FILAS; ++contador)
            if (tamanhoFila[contador] < tamanhoFila[idFilaMenor])
            {
                idFilaMenor = contador;
                if (tamanhoFila[idFilaMenor] == 0)
                    break;
            }

    return idFilaMenor;
}

/// <summary>
/// Recupera o identificador da fila mais populada
/// </summary>
/// <returns>Retorna, um inteiro, o identificador da fila mais populada encontrada.</returns>
int recuperarFilaMaior()
{
    int idFilaMaior = 0;
    int contador;
    for (contador = 1; contador < NUM_FILAS; ++contador)
        if (tamanhoFila[contador] > tamanhoFila[idFilaMaior])
            idFilaMaior = contador;

    return idFilaMaior;
}

/// <summary>
/// Adiciona o cliente na menor fila.
/// </summary>
/// <param name="idCliente" type="int">Identificador do cliente a ser inserido.</param>
/// <returns>Retorna, um inteiro, o identificador da fila que o cliente foi inserido.</returns>
int inserirCliente(int idCliente)
{
    clientes[++indiceCliente] = idCliente;
    int idFilaMenor = recuperarFilaMenor();
    tamanhoFila[idFilaMenor]++;

    return idFilaMenor;
}

/// <summary>
/// Ŕealiza o atendimento da fila desejada.
/// </summary>
/// <param name="idFila" type="int">Identificador da fila atendida.</param>
/// <returns>Retorna, um inteiro, se a fila foi atendida [1] ou não [0].</returns>
int realizarAtendimentoFila(int idFila)
{
    int idClienteAtendido = clientes[indiceCliente--];
    int idFilaAtendida = idFila;
    if (tamanhoFila[idFila] < 1)
    {
        idFilaAtendida = recuperarFilaMaior();
        if (idFila != idFilaAtendida)
            printf("Cliente %0*d saiu do caixa %0*d para o caixa %0*d.\n", quantidadeZeros, idClienteAtendido, quantidadeZeros, idFila, quantidadeZeros, idFilaAtendida);
    }

    tamanhoFila[idFilaAtendida]--;

    atenderCliente(idClienteAtendido, idFilaAtendida);

    return true;
}

/// <summary>
/// Método que inicializa as principais variáveis do programa.
/// </summary>
void inicializar()
{
    srand(time(NULL));
    indiceCliente = -1;
    quantidadeZeros = tamanhoDigito(NUM_FILAS > NUM_CLIENTES ? NUM_FILAS : NUM_CLIENTES);
    printf("Quantidade de clientes: \t%d\n", NUM_CLIENTES);
    printf("Quantidade de caixas: \t%d\n\n", NUM_FILAS);

    int contador;
    for (contador = 0;  contador < NUM_FILAS; contador++)
        tamanhoFila[contador] = 0;
}

/// <summary>
/// Método que finaliza as principais variáveis do programa.
/// </summary>
void finalizar() {
    printf("Finalizado com sucesso!\n\n");
}

/// <summary>
/// Preenche as filas com todos os clientes existentes.
/// </summary>
void preencherFilas()
{
    int idClienteInserido;
    int idFilaInserida;
    int contador;
    for (contador = 0; contador < NUM_CLIENTES; ++contador)
    {
        idClienteInserido = gerarIdCliente();
        printf("Cliente %0*d chegou.\n", quantidadeZeros, idClienteInserido);

        idFilaInserida = inserirCliente(idClienteInserido);
        printf("Cliente %0*d inserido na fila do caixa %0*d\n", quantidadeZeros, idClienteInserido, quantidadeZeros, idFilaInserida);
    }

    printf("Todos clientes devidamente enfileirados.\n\n");
}

/// <summary>
/// Conta quantas filas estão vazias
/// </summary>
/// <returns>Retorna, um inteiro, a quantidade de filas vazias.</returns>
int quantidadeFilasVazias()
{
    int idFila;
    int contador = 0;
    for (idFila = 0; idFila < NUM_FILAS; idFila++)
        if (tamanhoFila[idFila] == 0)
            contador++;

    return contador;
}

/// <summary>
/// Realiza o atendimento de todas os clientes, de todas as filas
/// </summary>
void atenderTodasFilas()
{
    printf("Iniciando atendimento dos caixas.\n");
    int idFila;
    while (quantidadeFilasVazias() < NUM_FILAS)
        for (idFila = 0; idFila < NUM_FILAS; ++idFila)
            realizarAtendimentoFila(idFila);

    printf("Todos clientes devidamente atendidos.\n\n");
}

int main(int argc, char const *argv[])
{
    inicializar();
    preencherFilas();
    atenderTodasFilas();
    finalizar();
}