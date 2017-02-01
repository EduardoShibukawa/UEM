#include <stdlib.h>  // rand(), srand()
#include <time.h>    // time()
#include "stdio.h"
#include "stdlib.h"
#include "mpi.h"
#include <getopt.h>
#include <limits.h>

#define ID_PROCESSO_GERENTE 0
#define INTERNAL_SLEEP_VALUE INT_MAX

void internal_sleep(){
	int i;
	for (i = 0; i < INTERNAL_SLEEP_VALUE; i++)
		;
}


int gera_cliente() {
	return (rand() % 1000) + 1;  
}

void atender_cliente(int cliente, int caixa){  
  internal_sleep();
  printf("Caixa %d Atendendo Cliente %d.\n", caixa, cliente);
}

void gerente_cliente(int numero_clientes, int numero_processadores) {
	int id_processo, cliente, clientes_atendidos = 0, caixas_fechados = 0;
	MPI_Status status_processo;

	for (id_processo = 1; id_processo <= numero_processadores; id_processo++){
		cliente = gera_cliente();		
		MPI_Ssend(&cliente, 1, MPI_INT, id_processo, id_processo, MPI_COMM_WORLD);
		clientes_atendidos++;
	}
			
	while (caixas_fechados < (numero_processadores)){		
		if (caixas_fechados < (numero_processadores)){
			MPI_Recv(&cliente, 1, MPI_INT, MPI_ANY_SOURCE, MPI_ANY_TAG, MPI_COMM_WORLD, &status_processo);					
			id_processo = status_processo.MPI_SOURCE;    
			if (cliente != -1){								    			
				if (clientes_atendidos < numero_clientes){
					cliente = gera_cliente();			
					clientes_atendidos += 1;
					printf("Cliente %d indo para o caixa %d\n", cliente, id_processo);
					MPI_Ssend(&cliente, 1, MPI_INT, id_processo, id_processo, MPI_COMM_WORLD);						
				}
				else {				
					cliente = -1;
					caixas_fechados += 1;								
					MPI_Ssend(&cliente, 1, MPI_INT, id_processo, id_processo, MPI_COMM_WORLD);					
				}	
			}
			else {
				printf("Caixa %d fechado.\n", id_processo);							
			}			
		}
	}	

	printf("----------------------------.\n");				
	printf("Clientes atendidos: %d.\n", clientes_atendidos);						
	printf("Caixas fechados: %d.\n", caixas_fechados);						
	printf("----------------------------.\n");						
}
void trabalhador_caixa(int id_processo){
	int cliente = 1;
	MPI_Status status_processo;
	while (cliente > 0){       		
		MPI_Recv(&cliente, 1, MPI_INT, ID_PROCESSO_GERENTE, id_processo, MPI_COMM_WORLD, &status_processo);		
		if (cliente > 0) {
			atender_cliente(cliente, id_processo);
		}
		MPI_Send(&cliente, 1, MPI_INT, ID_PROCESSO_GERENTE, id_processo, MPI_COMM_WORLD);	
	}			
}


void printHelp() {
    printf("Parâmetros:\n");
    printf("-n integer (Parâmetro para informar o numero de clientes do arquivo)\n");   
};


void main(int argc, char* argv[]) {
	int option, id_processo, numero_processadores, numero_clientes = 0;	    
    while ((option = getopt(argc, argv, "hn:")) != -1) {
        switch (option) {
            case 'n' :                
                numero_clientes = atoi(optarg);
                break;            
            default:
                printHelp();
                exit(0);
        }
    }

    if (numero_clientes <= 0) {
        printf("Erro, é necessario informar os parâmetros corretos!\n");
        printHelp();
        exit(EXIT_FAILURE);
    }


	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &id_processo);
	MPI_Comm_size(MPI_COMM_WORLD, &numero_processadores);

	if (numero_processadores < 2) {
		MPI_Abort(MPI_COMM_WORLD, 1);
	}

	srand(time(NULL));
	printf("Processo %d começou.\n", id_processo);
	if (id_processo == 0) {		
		printf("----------------------------.\n");			
		printf("Numero clientes: %d.\n", numero_clientes);						
		printf("Numero caixas: %d.\n", numero_processadores);						
		printf("----------------------------.\n");					
		gerente_cliente(numero_clientes, numero_processadores - 1);
	} else {				
		trabalhador_caixa(id_processo);
	}

	MPI_Finalize();
}
	
