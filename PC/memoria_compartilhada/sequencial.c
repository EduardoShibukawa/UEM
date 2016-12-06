#include <stdio.h>
#include <semaphore.h>
#include <stdbool.h>
#include <pthread.h>

#define NUM_FILAS 5

int tamanhoFila[NUM_FILAS];
int proximaFila = 0;
int contador;
sem_t tClientes;
sem_t tFilas[NUM_FILAS];
pthread_mutex_t mutex;

void atenderCliente()
{
    printf("Fila: %d\n", proximaFila);
}

int recuperaFilaMaior()
{
    int maior = 0;
    for (contador = 0; contador < NUM_FILAS; ++contador)
        if (tamanhoFila[contador] > maior)
            maior = contador;

    return maior;
}

int recuperaFilaMenor()
{
    int menor = tamanhoFila[0];
    for (contador = 1; contador < NUM_FILAS; ++contador)
        if (tamanhoFila[contador] < menor)
            menor = contador;

    return menor;
}

void cliente()
{
    pthread_mutex_lock(&mutex);
    proximaFila = recuperaFilaMenor();
    tamanhoFila[proximaFila]++;
    pthread_mutex_unlock(&mutex);
    sem_post(&tClientes);
    sem_wait(&tFilas[proximaFila]);
}

void empregado(int filaAtual)
{
    while(true)
    {
        sem_wait(&tClientes);
        pthread_mutex_lock(&mutex);
        if(tamanhoFila[filaAtual] > 0)
            proximaFila = filaAtual;
        else
            proximaFila = recuperaFilaMaior();

        tamanhoFila[proximaFila]--;
        pthread_mutex_unlock(&mutex);
        sem_post(&tFilas[proximaFila]);
        atenderCliente();
    }
}

int main(int argc, char const *argv[])
{
    for (contador = 0; contador < NUM_FILAS; ++contador)
        sem_init(&tFilas[contador], 0, 0);

    pthread_mutex_init(&mutex, NULL);

    return 0;
}