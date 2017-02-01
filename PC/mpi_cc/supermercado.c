#include "stdio.h"
#include "stdlib.h"
#include "mpi.h"

#define ID_PROCESSO_GERENTE 0
#define INTERNAL_SLEEP_VALUE 10000;

void internal_sleep(){
	var i;
	while (i = 0; i < INTERNAL_SLEEP_VALUE; i++);
}


int gera_cliente() {
  return rand() % 1000;  
}

void atender_cliente(int cliente, int caixa){
  printf("Caixa %d Atendendo Cliente %d", caixa, cliente);
  internal_sleep();
}

void gerente_clientes(int numero_clientes, int numero_processadores) {
	var id_processo, cliente;

	for (id_processo = 1; id_processo < numero_processadores; i++){
		cliente = gera_cliente();
		MPI_Send(&cliente, 1, MPI_INT, id_processo, 0, MPI_COMM_WORLD);
	}
		
	int clientes_atendidos = numero_processadores - 1;
	int caixa_fechados = 0;
	while (caixas_fechados < numero_processadores){
		MPI_Recv(&cliente, 1, MPI_INT, MPI_ANY_SOURCE, id_processo, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
		
		if (cliente_atendidos < numero_clientes){
			cliente = gera_cliente();
			MPI_Send(&cliente, 1, MPI_INT, id_processo, 0, MPI_COMM_WORLD);	
			clientes_atendidos += 1;
		}
		else {
			MPI_Send(-1, 1, MPI_INT, id_processo, 0, MPI_COMM_WORLD);	
			caixa_fechados += 1;			
		}
	}
}

void trabalhador_caixa(int id_processo){
	int id_processo;
	int cliente = 1;
	while (cliente > 0){
		MPI_Recv(&cliente, 1, MPI_INT, ID_PROCESSO_GERENTE, id_processo, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
		if (cliente > 0) {
			atender_cliente(cliente, id_processo);
		}
		MPI_Send(&cliente, 1, MPI_INT, ID_PROCESSO_GERENTE, id_processo, MPI_COMM_WORLD);	
	}			
}

void main(int argc, char* argv[]) {
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &id_processo);
	MPI_Comm_size(MPI_COMM_WORLD, &numero_processadores);

	int id_processo;
	int numero_processadores;
	int numero_clientes;

	if (size < 2) {
		MPI_Abort(MPI_COMM_WORLD, 1);
	}

	if (rank == 0) {
		gerente_cliente(numero_clientes, numero_processadores);
	} else {
		srand(time(NULL));
		trabalhador_caixa(numero_processo)
	}

	MPI_Finalize();
}
	
