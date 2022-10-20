#include<stdio.h>

int main(void){
  // declarando o vetor
  int vetor[100];
  int valor = 0;
  int i
  
  //valores do vetor são mostrados com somatórios de 2 
  for(i=0; i<=99; i++){
    valor += 2;
    vetor[i] = valor;
    printf("vetor[%d] = %d", i, vetor[i])
  }
  return 0;
}
