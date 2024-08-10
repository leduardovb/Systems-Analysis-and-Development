#include <stdio.h>
#include <stdlib.h>
#include <math.h>


/*
int soma(int num1 , int num2 , int *point) {
  int result;

  result = num1 + num2;
  *point = num1 + num2;

  return (result);
}

int main() {
  int num1 , num2 , result;

  printf("Digite um número: ");
  scanf("%d" , &num1);
  printf("\nDigite outro número: ");
  scanf("%d" , &num2);

  printf("\nO resultado da soma é: %d" , soma(num1 , num2 , &result));

  printf("\nO que tem dentro do result? %d" , result);
}
*/

/*
float vol_esf(float raio) {
  float volume;

  volume = (4 * 3.14 * pow(raio , 3)) / 3;

  return volume;
}

int main() {
  float raio , result;

  printf("Defina o raio da esfera cm: ");
  scanf("%f" , &raio);
  result = vol_esf(raio);
  printf("\nVolume: %.2f cm3" , result);
}
*/

/*
void maior_menor(float *vetor , int tam) {
  float vetor_num[tam] , num;
  vetor[1] = 0;

  for (int inicio = 0; inicio <= tam - 1; inicio ++) {
    printf("\nDigite um número: ");
    scanf("%f" , &num);
    if (num >= vetor[0]) {
      vetor[0] = num;
      if (vetor[1] == 0) {
        vetor[1] = num;
      }
    }
    if (num <= vetor[1]) {
      vetor[1] = num;
    }
  }
}

int main() {
  int tam , inicio = 0;
  float result , vetor[2];

  printf("Defina quantos números: ");
  scanf("%d" , &tam);
  maior_menor(vetor , tam);
  printf("\nMaior: %.1f; Menor: %.1f" , vetor[0] , vetor[1]);
}
*/

/*
void media_menor(int *vetor) {
  int num2 , media = 0;

  printf("Digite o 1 número: ");
  scanf("%d" , &vetor[0]);
  media = vetor[0];

  for (int inicio = 1; inicio <= 49; inicio ++) {
    printf("\nDigite o %d número: " , inicio + 1);
    scanf("%d" , &num2);
    if (num2 <= vetor[0]) {
      vetor[0] = num2;
    }
    media += num2;
  }
  vetor[1] = media / 50;
}

int main() {
  int vetor[2];

  media_menor(vetor);

  printf("\nO menor número digitado: %d; A média de todos os números: %d" , vetor[0] , vetor[1]); 
}
*/

/*
int quant_par(int *vetor) {
  int quant = 0;

  for (int inicio = 0; inicio <= 14; inicio ++) {
    if (vetor[inicio] % 2 == 0) {
      quant += 1;
    }
  }
  return quant;
}

int main() {
  int vetor[15] , result;

  result = quant_par(vetor);
  printf("A quantidade de pares no vetor é: %d" , result);
}
*/

/*
int soma_int(int n1 , int n2) {
  int soma = 0;

  for (int inicio = n1; inicio <= n2; inicio ++) {
    soma += inicio;
  }
  return soma;
}

int main() {
  int result , num1 , num2 , *n1 , *n2;

  printf("Digite um intervalo, inicio: ");
  scanf("%d" , &num1);
  n1 = &num1;
  printf("\nDigite um intervalo, fim: ");
  scanf("%d" , &num2);
  n2 = &num2;
  result = soma_int(*n1, *n2);
  printf("\nO resultado do intervalo: %d" , result);
}
*/
/*
int quant_div(int p_n) {
  int quant = 0;

  for (int inicio = 1; inicio <= p_n; inicio ++) {
    if (p_n % inicio == 0) {
      quant += 1;
    }
  }
  return quant;
}

int main() {
  int num , *p_n , result;

  printf("Digite um número: ");
  scanf("%d" , &num);
  p_n = &num;
  result = quant_div(*p_n);
  printf("\nO número %d tem %d divisores" , num , result);
}
*/

/*
void soma2(int num , int *soma) {
  *soma = num + 1;
}

int main() {
  int num , soma;

  printf("Defina um número: ");
  scanf("%d" , &num);
  soma2(num , &soma);
  printf("\n%d" , soma);
}*/

//char* representa string
