#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <stdbool.h>
#include <stdlib.h>

#define NUM_FILAS 4
#define NUM_THREADS_CLIENTE 4
#define NUM_CLIENTES_POR_THREAD 100

sem_t sem_fila[NUM_FILAS];
sem_t sem_cliente[NUM_FILAS];
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;

int tamanho_fila[NUM_FILAS];
int clientes[NUM_THREADS_CLIENTE * NUM_CLIENTES_POR_THREAD];
int index_cliente;
int clientes_restantes;

void inicializar() {
    index_cliente = -1;
    clientes_restantes = NUM_THREADS_CLIENTE * NUM_CLIENTES_POR_THREAD;

    pthread_mutex_init(&mutex, NULL);

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

    int menorFila = buscarFilaComMenorTamanho();
    sem_post(&sem_cliente[menorFila]);
    tamanho_fila[menorFila] += 1;
    clientes_restantes -= 1;
    index_cliente += 1;
    clientes[index_cliente] = cliente;

    pthread_mutex_unlock(&mutex);
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
    sleep(1);
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
    for (int fila_origem = 0; fila_origem < NUM_FILAS; fila_origem++) {
        if ((fila != fila_origem)
            && (atenderClienteFila(fila_origem, fila)))
            break;
    }
}

void desbloquearTodasFilas() {
    for (int i = 0; i < NUM_FILAS; i++) {
        sem_post(&sem_cliente[i]);
    }
}

void bloquearFila(int fila) {
    printf("bloqueando fila %d vazia. \n", fila);
    sem_wait(&sem_cliente[fila]);
}

void atendimentoFila(int fila) {
    while (true) {
        atenderTodosClienteFila(fila);
        filaVaziaAtenderOutraFila(fila);
        /*
         * Se todas filas estiverem vazias deveria bloquear,
         * porem  no nosso caso devemos parar a thread
         */
        if (todasFilasVazias()) {
            if (clientes_restantes <= 0){
                desbloquearTodasFilas();
                break;
            }

            bloquearFila(fila);
        }
    }
}

void *threadNovosCliente(void *id) {
    int _id = (int) id;
    for (int i = 0; i < NUM_CLIENTES_POR_THREAD; i++)
        novoCliente();

    if (clientes_restantes <= 0) {
        desbloquearTodasFilas();
        printf("Todos clientes devidamente enfileirados.\n\n");
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

    printf("Total de clientes: \t%d\n", NUM_THREADS_CLIENTE * NUM_CLIENTES_POR_THREAD);
    printf("Total de caixas: \t%d\n\n", NUM_FILAS);


    for (i = 0; i < NUM_THREADS_CLIENTE; i++)
        if (pthread_create(&tclientes[i], NULL, &threadNovosCliente, (void *) i)) {
            printf("Erro na criacao da thread.");
        };

    for (i = 0; i < NUM_FILAS; i++)
        if (pthread_create(&tfila[i], NULL, &threadAtenderFila, (void *) i)) {
            printf("Erro na criacao da thread.");
        };

    for (i = 0; i < NUM_FILAS; i++) {
        pthread_join(tfila[i], NULL);
    }

    printf("Todos clientes devidamente atendidos.\n\n");

    finalizar();

    return 0;
}



