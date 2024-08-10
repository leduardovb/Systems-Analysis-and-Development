#include <stdlib.h>
#include <stdio.h>
#include <conio.h>
#include <string.h>

//Ex 1

// int main() {
//   float capacidade , peso , total;
//   int inicio = 0;

//   printf("Digite a capacidade do elevador: kg ");
//   scanf("%f" , &capacidade);

//   for (inicio = 1; inicio <= 5; inicio ++)
//   {
//     printf("\nDigite o peso %dº pessoa: " , inicio);
//     scanf("%f" , &peso);
//     total += peso;
//   }
  
//   if (capacidade >= total) printf("\nO elevador pode subir");
//   else {
//     printf("\nPeso excedido");
//   }
//   return (0);
// }

//Ex 2

// int main() {
//   int num;

//   printf("Digite um número: ");
//   scanf("%d" , &num);

//   if (num % 3 == 0 && num % 7 == 0) printf("\nO numéro %d é divisível por 3 e 7" , num);
//   else {
//     printf("\nO número %d não é divísivel por 3 e 7" , num);
//   }
//   return (0);
// }

//Ex 3

// int main() {

//   float notas , total;
//   int inicio;

//   for (inicio = 1; inicio <= 4; inicio ++) {
//     printf("\nDigite a %dº nota: " , inicio);
//     scanf("%f" , &notas);
//     total += notas;
//   }
//   total = total / 4;

//   if (total >= 7) printf("\nAluno aprovado");
//   else {
//     printf("\nAluno reprovado");
//   }
// }

//Ex 4

// int main() {
//   float num , num2 , dif;

//   printf("Digite um valor: ");
//   scanf("%f" , &num);
//   printf("\nDigite outro valor: ");
//   scanf("%f" , &num2);

//   if (num > num2) {
//     dif = (num - num2) * 0.6;
//     printf("\nMaior: %2f; Menor: %2f" , num , num2);
//     printf("\n60%% diferença: %2f" , dif);
//   }
  
//   else {
//     dif = (num2 - num) * 0.6;
//     printf("\n Maior: %f; Menor: %f" , num2 , num);
//     printf("\n60%% diferença: %f" , dif);
//   }
// }

//Ex 5

// int main() {
//   int num1 , num2;

//   printf("Digite um número: ");
//   scanf("%d" , &num1);

//   printf("\nDigite outro número: ");
//   scanf("%d" , &num2);

//   if (num1 > num2) {
//     printf("\nO número %d é maior que o número %d" , num1 , num2);
//   }
//   else {
//     if (num2 > num1) {
//     printf("\nO número %d é maior que o número %d" , num2 ,num1);
//     }
//     if (num1 == num2) {
//       printf("\nOs números são iguais");
//     }
//   }
// }

//Ex 6

// int main() {

//   float duracao , preco_total , horas;

//   printf("Defina a duração da chamada em minutos: ");
//   scanf("%f" , &duracao);

//   if (duracao >= 11) {
//     preco_total = (0.30 * 10) + ((duracao - 10) * 0.05);
//   }
//   else {
//     preco_total = duracao * 0.3;
//   }
  
//   horas = duracao / 60;
//   printf("\nDuração chamada: %2.fm \nDuração chamada: %.2fh \nPreço total: R$ %.2f" , duracao , horas , preco_total);
// }

//Ex 7

// int main() {

//   float total_compra;
//   int quant_macas;

//   printf("Digite a quantidade de maçãs: ");
//   scanf("%d" , &quant_macas);

//   if (quant_macas >= 12) {
//     total_compra = quant_macas * 0.7;
//   }
//   else {
//     total_compra = quant_macas * 0.8;
//   }

//   printf("\nTotal compra: R$ %.2f" , total_compra);
// }

//Ex 8 

// int main() {

//   int num , inicio , soma = 0;

//   for (inicio = 0; inicio < 4; inicio ++) {
//     printf("Digite um número: ");
//     scanf("%d" , &num);

//     if (num % 2 == 0) {
//       soma += num;
//     }
//   }

//   printf("\nSoma dos pares: %d" , soma);
// }

//Ex 9
/*
int main() {
  char nome2[30];

  printf("Digite seu nome: ");
  gets(nome2);
  
  if (strcmp (nome2, "Luiz Eduardo") == 0) {
      printf("\nSeu nome e igual o meu");
  }
  else {
      printf("\nSeu nome nao e igual o meu");
  }
}*/

//Ex 10
/*
int main() {
    int maior , a , b , c;

    printf("Digite um num: ");
    scanf("%d" , &a);
    maior = a;
    printf("\nDigite outro num: ");
    scanf("%d" , &b);

    if (b > maior) {
        maior = b;
    }

    printf("\nDigite outro num: ");
    scanf("%d" , &c);

    if (c > maior) {
        maior = c;
    }

    printf("\nO num %d e maior" , maior);
}*/
