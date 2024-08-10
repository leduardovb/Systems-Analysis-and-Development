#include <stdio.h>
#include <stdlib.h>

//Ex 1

// int main() {

//   float num , soma = 0;
//   int inicio;

//   for (inicio = 0; inicio < 10; inicio ++) {
//     printf("\nDefina um número: ");
//     scanf("%f" , &num);
//     soma += num;
//   }
//   printf("\nA soma dos num: %.2f" , soma);
// }

//Ex 2 

// int main() {              
//   float num = 0 , media = 0;
//   int cont = 0;

//   while (num < 100) {
//     printf("\nDigite um número: ");
//     scanf("%f" , &num);
//     cont += 1;
//     media += num;
//   }
//   media = media / cont;
//   printf("\nMedia: %.2f" , media);
// }

//Ex 3

// int main() {
//   int num , inicio;

//   printf("Defina um número: ");
//   scanf("%d" , &num);
  
//   for (inicio = 1; inicio < 11; inicio ++) {
//     printf("%d x %d = %d\n" , num , inicio , num * inicio);
//   }
// }

//Ex 4 
/*
int main() {
  int soma = 0 , inicio;

  for (inicio = 1; inicio <= 100; inicio ++) {
    if (inicio % 2 != 0) {
      soma += inicio;
    }
  }
  printf("Soma dos 100 primeiros impares: %d" , soma);
}*/

//Ex 5
/*
int main() {
  int lista_idade[400] , inicio , quant = 0;
  float perc;

  for (int i = 0; i < 400; i ++) {
    printf("\nDefina a idade das pessoas: ");
    scanf("%d" , &lista_idade[i]);
  }

  for (inicio = 0; inicio < 400; inicio ++) {
    if (lista_idade[inicio] >= 60) {
      quant += 1;
    }
  }
  perc = (quant * 100) / 400;
  printf("\nPorcentagem de pessoas acima de 60 anos: %.2f%%" , perc);
}*/

//Ex 8 

// int main() {
//   int inicio;

//   for (inicio = 1; inicio < 100; inicio ++) {
//     if (inicio % 4 == 0) {
//       printf("%d / 4 = %d\n" , inicio , inicio / 4);
//     }
//   }
// }

//Ex 9 

// int main() {
//   int num , inicio;

//   printf("Digite um número: ");
//   scanf("%d" , &num);
  
//   if (num <= 9) {
//     for (inicio = 1; inicio < 11; inicio ++) {
//       printf("%d x %d = %d\n" , num , inicio , num * inicio);
//     }
//   }
//   else {
//     printf("\nNúmero fora do intervalo");
//   }
// }

//Ex 10

// int main() {
//   int soma = 0 , inicio;

//   for (inicio = 100; inicio < 201; inicio ++) {
//     if (inicio % 6 == 0) {
//       printf("%d\n" , inicio);
//       soma += inicio;
//     }
//   }
//   printf("\n%d" , soma);
// }

//Ex 12

// int main() {
//   int inicio;

//   for (inicio = 100; inicio < 201; inicio ++) {
//     if (inicio % 4 == 7) {
//       printf("Achei o ouro: %d\n" , inicio);
//     }
//   }
// }

//Ex 20

// int main() {
//   int num , inicio , cont = 0;

//   for (inicio = 0; inicio < 5; inicio ++) {
//     printf("\nDigite um número: ");
//     scanf("%d" , &num);

//     if (num < 0) {
//       cont += 1;
//     }
//   }
//   printf("\n%d de 5 são números ímpares" , cont);
// }

//Ex 21
/*
int main() {
  int num = 1 , cont = 0;
  float media = 0;

  while (num != 0) {
    printf("\nDigite um número: ");
    scanf("%d" , &num);

    if (num % 2 == 0) {
      media += num;
      cont += 1;
    }
  }
  media = media / cont;
  printf("Média dos numeros pares digitados: %.2f" , media);
}*/
