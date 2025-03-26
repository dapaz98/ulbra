/*
Crie de forma programática um validador de nome de variável. (Desafio a usarem uma máquina de estados para isso) regras:
- Não usar regex
- Não pode começar com número
- Tamanho máximo 10
- Não pode conter caracteres especiais (exceto o _ )


Abaixo, uma sequenciazinha pronta para testar:
exemplo123,outra_variavel,nome_valido,variavel_1,1a,blabla+,blab*bla
*/


#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>
#include <string.h>

#define MAX_LEN 10

typedef enum { Q0, Q1, Q2, REJEITA } Estado;

typedef struct {
    Estado estado;
    int contador;
} ValidadorVariavel;

void initValidador(ValidadorVariavel *v) {
    v->estado = Q0;
    v->contador = 0;
}

void transicao(ValidadorVariavel *v, char c) {
    switch (v->estado) {
        case Q0:
            if (isalpha(c) || c == '_') {
                v->estado = Q1;
                v->contador++;
            } else {
                v->estado = REJEITA;
            }
            break;
        case Q1:
            if (isalnum(c) || c == '_') {
                v->contador++;
                if (v->contador >= MAX_LEN) {
                    v->estado = Q2;
                }
            } else {
                v->estado = REJEITA;
            }
            break;
        case Q2:
            v->estado = REJEITA;
            break;
        case REJEITA:
            break;
    }
}

bool validar(const char *nome) {
    ValidadorVariavel v;
    initValidador(&v);
    
    for (int i = 0; nome[i] != '\0'; i++) {
        transicao(&v, nome[i]);
        if (v.estado == REJEITA) {
            return false;
        }
    }
    return v.estado == Q1 || v.estado == Q2;
}

int main() {
    
    const char *variaveis[] = {"exemplo123", "outra_variavel", "nome_valido", "variavel_1", "1a", "blabla+", "blab*bla"};
    int numVariaveis = sizeof(variaveis) / sizeof(variaveis[0]);
    
    for (int i = 0; i < numVariaveis; i++) {
        printf("%s: %s\n", variaveis[i], validar(variaveis[i]) ? "Válida" : "Inválida");
    }
    return 0;
}