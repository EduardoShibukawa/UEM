#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <stdbool.h>
#include <zconf.h>

#define NUM_FILAS 5
#define NUM_THREADS_CLIENTE 5
#define NUM_CLIENTES_POR_THREAD 50

sem_t sem_fila[NUM_FILAS];
sem_t sem_cliente[NUM_FILAS];
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;

int tamanho_fila[NUM_FILAS];

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

void serAtendido(int fila) {
    printf("Cliente sendo atendido caixa %d \n", fila);
}

void novoCliente() {
    pthread_mutex_lock(&mutex);

    int menorFila = buscarFilaComMenorTamanho();
    sem_post(&sem_cliente[menorFila]);
    tamanho_fila[menorFila] += 1;
    pthread_mutex_unlock(&mutex);

//    printf(
//            "Cliente entrando na fila %d, de tamanho %d \n",
//            menorFila, tamanho_fila[menorFila]
//    );
//
    sem_wait(&sem_fila[menorFila]);
    serAtendido(menorFila);
}

int todasFilasVazias(){
    pthread_mutex_lock(&mutex);

    int todasVazias = true;
    for (int i = 0; i < NUM_FILAS; i++)
        if (tamanho_fila[i] > 0){
            todasVazias = false;
            break;
        }

    pthread_mutex_unlock(&mutex);

    return todasVazias;
}

void atenderCliente(int fila){
    printf("Caixa %d atendendo cliente \n", fila);
    sleep(2);
}

int atenderClienteFila(int fila){
    pthread_mutex_lock(&mutex);
    if (tamanho_fila[fila] > 0){
        tamanho_fila[fila] -= 1;
//        printf(
//                "Cliente indo para atendimento na fila %d, de tamanho %d \n",
//                fila, tamanho_fila[fila]
//        );
        sem_post(&sem_fila[fila]);
        pthread_mutex_unlock(&mutex);

        sem_wait(&sem_cliente[fila]);
        atenderCliente(fila);

        return true;
    }

    pthread_mutex_unlock(&mutex);
    return false;
}

void atenderTodosClienteFila(int fila){
    while (atenderClienteFila(fila));
}

void filaVaziaAtenderOutraFila(int fila_origem){
    for (int i = 0; i < NUM_FILAS; i++){
        if ((fila_origem != i)
            && (atenderClienteFila(i)))
            break;
    }
}

void bloquearFilaSeTodasEstiveremVazia(int fila){
    if (todasFilasVazias()) {
        printf("bloqueando fila %d vazia. \n", fila);
        sem_wait(&sem_cliente[fila]);
    }
}

void atendimentoFila(int fila) {
    while (true){
        atenderTodosClienteFila(fila);
        filaVaziaAtenderOutraFila(fila);
        bloquearFilaSeTodasEstiveremVazia(fila);
    }
}


void inicializarSemaforos() {
    pthread_mutex_init(&mutex, NULL);
    for (int i = 0; i < NUM_FILAS; i++) {
        sem_init(&sem_fila[i], 0, 0);
        sem_init(&sem_cliente[i], 0, 0);
    }
}

void *threadNovosCliente(void *args) {
    while (true) {
        for (int i = 0; i < NUM_CLIENTES_POR_THREAD; i++)
            novoCliente();

        sleep(10);
    }

    pthread_exit(NULL);
}

void *threadAtenderFila(void *fila) {
    int index = (int) fila;
    atendimentoFila(index);
    pthread_exit(NULL);
}

int main() {
    pthread_t tfila[NUM_FILAS];
    pthread_t tclientes[NUM_THREADS_CLIENTE];

    inicializarSemaforos;

    for (int i = 0; i < NUM_FILAS; i++)
        if (pthread_create(&tfila[i], NULL, &threadAtenderFila, (void *)i)){
            printf("Erro na criacao da thread.");
        };

    for (int i = 0; i < NUM_THREADS_CLIENTE; i++)
        if (pthread_create(&tclientes[i], NULL, &threadNovosCliente, NULL)){
            printf("Erro na criacao da thread.");
        };

    pthread_exit(NULL);
}