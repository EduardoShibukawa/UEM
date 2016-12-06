#include <stdio.h>
#include <stdlib.h>
#include <semaphore.h>
#include <stdbool.h>
#include <pthread.h>
#include <time.h>

#define NUM_FILAS 15
#define NUM_CLIENTES 10

//sem_t semClientes;
//sem_t semFilas[NUM_FILAS];

pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;

int clientes[NUM_CLIENTES];
int tamanhoFila[NUM_FILAS];
int indiceCliente;
int quantidadeZeros;

/// <summary>
/// Encontra a quantidade de algarismos o valor possui.
/// </summary>
/// <param name="valor">Valor do inteiro a ser calculado.</param>
/// <returns>Retorna o tamanho, quantidade, de algarismos o valor informado possui.</returns>
int tamanhoDigito(int valor)
{
    int tamanho = 1;
    if(valor == 0)
        return tamanho;

    for(tamanho = 0; valor > 0; valor /= 10)
        tamanho++;

    return tamanho;
}

/// <summary>
/// Cria um identificador para o cliente.
/// </summary>
/// <returns>Retorno, um inteiro, o identificador criado para o cliente.</returns>
int gerarIdCliente()
{
    return (rand() % (NUM_CLIENTES * 10)) + 1;
}

/// <summary>
/// Método que informa em qual caixa o cliente será atendido.
/// </summary>
/// <param name="idClienteAtendido">Identificador do cliente a ser atendido.</param>
/// <param name="idFilaAtendido">Identificador da fila no qual o cliente foi atendido.</param>
void atenderCliente(int idClienteAtendido, int idFilaAtendido)
{
    printf("Cliente %0*d atendido no caixa %0*d.\n", quantidadeZeros, idClienteAtendido, quantidadeZeros, idFilaAtendido);
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
/// <param name="idCliente">Identificador do cliente a ser inserido.</param>
/// <returns>Retorna, um inteiro, o identificador da fila que o cliente foi inserido.</returns>
int inserirCliente(int idCliente)
{
    pthread_mutex_lock(&mutex);
    clientes[++indiceCliente] = idCliente;
    int idFilaMenor = recuperarFilaMenor();
    //sem_post(&semClientes);
    tamanhoFila[idFilaMenor]++;
    pthread_mutex_unlock(&mutex);
    //sem_wait(&semFilas[idFilaMenor]);

    return idFilaMenor;
}

/// <summary>
/// Ŕealiza o atendimento da fila desejada.
/// </summary>
/// <param name="idFilaAtendida">Identificador da fila atendida.</param>
/// <returns>Retorna, um inteiro, se a fila foi atendida [1] ou não [0].</returns>
int realizarAtendimentoFila(int idFilaAtendida)
{
    if (tamanhoFila[idFilaAtendida] < 1)
        return false;

    pthread_mutex_lock(&mutex);

    int idClienteAtendido = clientes[indiceCliente--];
    tamanhoFila[idFilaAtendida]--;
    //sem_post(&semFilas[idFilaAtendida]);
    //sem_wait(&semClientes);

    pthread_mutex_unlock(&mutex);

    atenderCliente(idClienteAtendido, idFilaAtendida);

    return true;
}

/// <summary>
/// Realiza o atendimento de todos os clientes da fila
/// </summary>
/// <param name="idFilaAtendida">Identificador da fila atendida.</param>
void atenderTodosClienteFila(int idFilaAtendida)
{
    while (realizarAtendimentoFila(idFilaAtendida));
}

/// <summary>
/// Método que inicializa as principais variáveis do programa.
/// </summary>
void inicializar()
{
    srand(time(NULL));
    indiceCliente = -1;
    quantidadeZeros = tamanhoDigito(NUM_FILAS > NUM_CLIENTES ? NUM_FILAS : NUM_CLIENTES);
    printf("Total de clientes: \t%d\n", NUM_CLIENTES);
    printf("Total de caixas: \t%d\n\n", NUM_FILAS);

    pthread_mutex_init(&mutex, NULL);

    int contador;
    for (contador = 0;  contador < NUM_FILAS; contador++){
        //sem_init(&semFilas[contador], 0, 0);
        tamanhoFila[contador] = 0;
    }

    //sem_init(&semClientes, 0, 0);
}

/// <summary>
/// Método que finaliza as principais variáveis do programa.
/// </summary>
void finalizar() {
    pthread_mutex_destroy(&mutex);
    printf("Finalizado com sucesso!\n\n");
    //int contador;
    //for (contador = 0; contador < NUM_FILAS; contador++)
        //sem_destroy(&semFilas[contador]);

    //sem_destroy(&semClientes);
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
/// Realiza o atendimento de todas os clientes, de todas as filas
/// </summary>
void atenderTodasFilas()
{
    int contador;
    for (contador = 0; contador < NUM_FILAS; ++contador)
        atenderTodosClienteFila(contador);

    printf("Todos clientes devidamente atendidos.\n\n");
}

int main(int argc, char const *argv[])
{
    inicializar();
    preencherFilas();
    atenderTodasFilas();
    finalizar();
}