#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <stdbool.h>
#include <stdlib.h>

#define NUM_FILAS 5
#define NUM_THREADS_CLIENTE 5
#define NUM_CLIENTES_POR_THREAD 10000000

sem_t sem_fila[NUM_FILAS];
sem_t sem_cliente[NUM_FILAS];
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_barrier_t barrier;

int tamanho_fila[NUM_FILAS];
int clientes[NUM_THREADS_CLIENTE * NUM_CLIENTES_POR_THREAD];
int index_cliente;
int lojaAberta;

void inicializar() {
    index_cliente = -1;
    lojaAberta = true;

    pthread_mutex_init(&mutex, NULL);
    pthread_barrier_init(&barrier, NULL, NUM_THREADS_CLIENTE);

    for (int i = 0; i < NUM_FILAS; i++)
        sem_init(&sem_fila[i], 0, 0);

    for (int i = 0; i < NUM_THREADS_CLIENTE; i++)
        sem_init(&sem_cliente[i], 0, 0);
}

void finalizar() {
    pthread_mutex_destroy(&mutex);

    for (int i = 0; i < NUM_FILAS; i++)
        sem_destroy(&sem_fila[i]);

    for (int i = 0; i < NUM_THREADS_CLIENTE; i++)
        sem_destroy(&sem_cliente[i]);
}

int buscarFilaComMenorTamanho() {
    if (tamanho_fila[0] == 0)
        return 0;

    int menorFila = 0;
    for (int i = 1; i < NUM_FILAS; i++) {
        if (tamanho_fila[i] == 0) {
            return i;
        }

        if (tamanho_fila[i] < tamanho_fila[menorFila]) {
            menorFila = i;
        }
    }

    return menorFila;
}

void serAtendido(int cliente) {
    printf("Cliente %d sendo atendido\n", cliente);
}

int getIdCliente() {
    return rand() % 10000;
}

void novoCliente() {
    int cliente = getIdCliente();
    printf("Cliente %d chegou.\n", cliente);

    pthread_mutex_lock(&mutex);
    index_cliente += 1;
    clientes[index_cliente] = cliente;
    int menorFila = buscarFilaComMenorTamanho();
    sem_post(&sem_cliente[menorFila]);
    tamanho_fila[menorFila] += 1;
    pthread_mutex_unlock(&mutex);

    printf("Cliente %d entrou na fila %d.\n", cliente, menorFila);

    sem_wait(&sem_fila[menorFila]);
    serAtendido(cliente);
}

int todasFilasVazias() {
    pthread_mutex_lock(&mutex);

    int todasVazias = true;
    for (int i = 0; i < NUM_FILAS; i++)
        if (tamanho_fila[i] > 0) {
            todasVazias = false;
            break;
        }

    pthread_mutex_unlock(&mutex);
    return todasVazias;
}

void atenderCliente(int fila, int cliente) {
    printf("Caixa %d atendendo cliente %d \n", fila, cliente);
}

int atenderClienteFila(int fila_origem, int fila_atendendo) {
    pthread_mutex_lock(&mutex);
    if (tamanho_fila[fila_origem] > 0) {
        int cliente = clientes[index_cliente];
        index_cliente -= 1;
        tamanho_fila[fila_origem] -= 1;
        sem_post(&sem_fila[fila_origem]);

        pthread_mutex_unlock(&mutex);

        sem_wait(&sem_cliente[fila_origem]);
        if (fila_origem != fila_atendendo) {
            printf("Cliente %d saiu do caixa %d para o caixa %d.\n",
                   cliente, fila_origem, fila_atendendo);
        }
        atenderCliente(fila_atendendo, cliente);

        return true;
    }

    pthread_mutex_unlock(&mutex);
    return false;
}

void atenderTodosClienteFila(int fila) {
    while (atenderClienteFila(fila, fila));
}

void filaVaziaAtenderOutraFila(int fila) {
    for (int i = 0; i < NUM_FILAS; i++) {
        if ((fila != i)
            && (atenderClienteFila(i, fila)))
            break;
    }
}

void bloquearFilaSeTodasEstiveremVazia(int fila) {
    if (todasFilasVazias()
        && lojaAberta) {
        printf("bloqueando fila %d vazia. \n", fila);
        sem_wait(&sem_cliente[fila]);
    }
}

void desbloquearTodosFilas() {
    for (int i = 0; i < NUM_FILAS; i++) {
        sem_post(&sem_cliente[i]);
    }
}

int continuarAtendendo() {
    return lojaAberta || !todasFilasVazias();
}

void atendimentoFila(int fila) {
    while (continuarAtendendo()) {
        atenderTodosClienteFila(fila);
        filaVaziaAtenderOutraFila(fila);
        bloquearFilaSeTodasEstiveremVazia(fila);
    }
}

void *threadNovosCliente(void *args) {
    for (int i = 0; i < NUM_CLIENTES_POR_THREAD; i++)
        novoCliente();

    if (pthread_barrier_wait(&barrier) != 0) {
        lojaAberta = false;
        if (todasFilasVazias())
            desbloquearTodosFilas();
    }

    pthread_exit(NULL);
}

void *threadAtenderFila(void *fila) {
    int index = (int) fila;

    atendimentoFila(index);

    pthread_exit(NULL);
}

int main() {
    int i;
    srand((unsigned int) time(NULL));
    pthread_t tfila[NUM_FILAS];
    pthread_t tclientes[NUM_THREADS_CLIENTE];

    inicializar();

    for (i = 0; i < NUM_THREADS_CLIENTE; i++)
        if (pthread_create(&tclientes[i], NULL, &threadNovosCliente, NULL)) {
            printf("Erro na criacao da thread.");
        };

    for (i = 0; i < NUM_FILAS; i++)
        if (pthread_create(&tfila[i], NULL, &threadAtenderFila, (void *) i)) {
            printf("Erro na criacao da thread.");
        };

    for (i = 0; i < NUM_FILAS; i++) {
        pthread_join(tfila[i], NULL);
    }

    finalizar();
}



