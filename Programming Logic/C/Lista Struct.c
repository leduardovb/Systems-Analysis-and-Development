#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//Exercicio 02
/*
struct reg {
  char nome[20] , sexo[1];
  int idade;
  float salario;
};

int main() {
  struct reg s;
  int idade;

  s.salario = 725.54;
  strcpy(s.nome , "José da Silva");
  strcpy(s.sexo , "M");
  printf("Defina a idade: ");
  scanf("%d" , &s.idade);

  printf("\n\n\nNome: %s\nSálario: %.2f\nIdade: %d\t\t\tSexo: %s" , s.nome , s.salario , s.idade , s.sexo);
}*/

//Exercicio 03
/*
struct roupa_inf {
  int cod , quant;
  char desc[50] , nome_forn[25];
  float preco;
};

int main() {
  struct roupa_inf r;

  printf("===Cadastro de Peça===\n\n");
  printf("Código peça: ");
  scanf("%d" , &r.cod);
  printf("\nDescrição: ");
  scanf(" %[^\n]s" , r.desc);
  printf("\nNome fornecedor: ");
  scanf(" %[^\n]s" , r.nome_forn);
  printf("\nQuantidade recebida: ");
  scanf("%d" , &r.quant);
  printf("\nPreço: ");
  scanf("%f" , &r.preco);

  printf("\n\n\n===Produto Cadastrado===\n");
  printf("Código: %d\n\n" , r.cod);
  printf("Descrição: %s\n" , r.desc);
  printf("Nome Forncedor: %s\n" , r.nome_forn);
  printf("Quantidade recebida: %d" , r.quant);
  printf("\n\nPreço Produto: R$ %.2f" , r.preco);
}*/

//Exercicio 04
/*
struct reserva_aviao {
  int cod_aviao;
  char id_voo[8] , nome_cliente[25] , assento[3];
  float valor_passagem;
};

int main() {
  struct reserva_aviao ra;

  printf("===Reserva Viagem===\n\n");
  printf("Cógido Avião: ");
  scanf("%d" , &ra.cod_aviao);
  printf("\nIdVoo: ");
  scanf(" %[^\n]s" , ra.id_voo);
  printf("\nNome passageiro: ");
  scanf(" %[^\n]s" , ra.nome_cliente);
  printf("\nNúmero Assento: ");
  scanf("%s" , ra.assento);
  printf("\nValor Passagem: R$ ");
  scanf("%f" , &ra.valor_passagem);

  printf("\n\n\n===Ticket Voo===\n");
  printf("Código Avião: %d\n\n" , ra.cod_aviao);
  printf("Nome: %s\n" , ra.nome_cliente);
  printf("IdVoo: %s\n" , ra.id_voo);
  printf("Número Assento: %s\n\n" , ra.assento);
  printf("Valor Passagem: R$ %.2f" , ra.valor_passagem);
}*/

//Exercicio 05
/*
struct aluno_dados {
  int ra;
  char nome[35];
  float nota1 , nota2 , nota3;
};

int main() {
  struct aluno_dados a[100];

  int pos;
  float media , media_maior = 0;

  for (int i = 0; i < 3; i ++) {
    printf("Nome aluno: ");
    scanf(" %[^\n]s" , a[i].nome);
    printf("\nRA Aluno: ");
    scanf("%d" , &a[i].ra);
    printf("\nNota[1]: ");
    scanf("%f" , &a[i].nota1);
    printf("\nNota[2]: ");
    scanf("%f" , &a[i].nota2);
    printf("\nNota[2]: ");
    scanf("%f" , &a[i].nota3);
    printf("==============\n\n");

    media = (a[i].nota1 + a[i].nota2 + a[i].nota3) / 3;
    if (media > media_maior) {
      media_maior = media;
      pos = i;
    }
  }
  printf("\n\n\n===Aluno de maior média===\n\n");
  printf("Aluno: %s\nRA: %d" , a[pos].nome , a[pos].ra);
}*/

//Exercicio 07
/*
struct produto {
  int cod , estoque_minimo , estoque_atual;
  float preco;
  char descricao[50];
};

int main() {
  struct produto p[100];
  int cont = -1 , opc = 1;

  while (opc != 0) {
    cont ++;
    printf("===Cadastro Produto===\n\n");
    printf("Codigo: ");
    scanf("%d" , &p[cont].cod);
    printf("\nDescricao: ");
    scanf(" %[^\n]s" , p[cont].descricao);
    printf("\nEstoque minimo: ");
    scanf("%d" , &p[cont].estoque_minimo);
    printf("\nEstoque atual: ");
    scanf("%d" , &p[cont].estoque_atual);
    printf("\nPreco: ");
    scanf("%f" , &p[cont].preco);
    printf("\n\n[ 1 ] Novo cadastro\n[ 0 ] Finalizar\n\n: ");
    scanf("%d" , &opc);
    system("cls");
  }
  printf("===Produtos com estoque baixo===\n\n");
  for (int i = 0; i <= cont; i ++) {
    if (p[i].estoque_atual < p[i].estoque_minimo) {
      printf("[ %d ] %s\n" , p[i].cod , p[i].descricao);
    }
  }
}*/

//Exercicio 12
/*
struct carro {
  int cod , ano;
  float preco;
  char modelo[30] , marca[25] , cor[15] , combustivel[25];
};

int main() {
  struct carro c[100];

  printf("===Cadastro Produto===\n\n");
  for (int i = 0; i < 100; i ++) {
    printf("Codigo: ");
    scanf("%d" , &c[i].cod);
    printf("\nMarca: ");
    scanf(" %[^\n]s" , c[i].marca);
    printf("\nModelo: ");
    scanf(" %[^\n]s" , &c[i].modelo);
    printf("\nCor: ");
    scanf(" %[^\n]s" , &c[i].cor);
    printf("\nPreco: ");
    scanf("%f" , &c[i].preco);
    printf("\nCombustivel: ");
    scanf(" %[^\n]s" , &c[i].combustivel);
    system("cls");
  }

  for (int i = 0; i < 100; i ++) {
    printf("[ %d ] %s [%s] [%s] | %s\n" , c[i].cod , c[i].modelo , c[i].cor , c[i].combustivel , c[i].marca);
    printf("R$: %f" , c[i].preco);
  }

}*/
