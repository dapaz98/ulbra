/*
Na linguagem de sua preferência, escreva um analisador léxico capaz ler um arquivo de texto e 
identificar tokens do tipo: TOKEN_ID, TOKEN_NUM, TOKEN_OP (Vide autômato desenhado em aula)
*/

#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

#define MAX_TOKEN_SIZE 100

typedef enum {
    TOKEN_ID,
    TOKEN_NUM,
    TOKEN_OP
} TokenType;

void print_token(TokenType type, const char *content) {
    printf("________________________\n");
    switch(type) {
        case TOKEN_ID:
            printf("tipo: TOKEN_ID \n");
            break;
        case TOKEN_NUM:
            printf("tipo: TOKEN_NUM \n");
            break;
        case TOKEN_OP:
            printf("tipo: TOKEN_OP \n");
            break;
    }
    printf("conteúdo: %s\n", content);
    printf("________________________\n\n");
}

int is_op_char(char c) {
    return c == '=' || c == '>' || c == '<' || c == '+' || c == '-' || c == '*' || c == '/';
}

void analyze_file(const char *filename) {
    FILE *fp = fopen(filename, "r");
    if (!fp) {
        perror("Erro ao abrir o arquivo");
        return;
    }

    char c;
    while ((c = fgetc(fp)) != EOF) {
        if (isspace(c)) {
            continue;
        }

        if (isalpha(c)) {
            char buffer[MAX_TOKEN_SIZE] = {0};
            int i = 0;
            buffer[i++] = c;

            while ((c = fgetc(fp)) != EOF && (isalnum(c))) {
                buffer[i++] = c;
            }
            buffer[i] = '\0';
            print_token(TOKEN_ID, buffer);
            if (c != EOF) fseek(fp, -1, SEEK_CUR); 
        }
        else if (isdigit(c)) {
            char buffer[MAX_TOKEN_SIZE] = {0};
            int i = 0;
            buffer[i++] = c;

            while ((c = fgetc(fp)) != EOF && isdigit(c)) {
                buffer[i++] = c;
            }
            buffer[i] = '\0';
            print_token(TOKEN_NUM, buffer);
            if (c != EOF) fseek(fp, -1, SEEK_CUR);
        }
        else if (is_op_char(c)) {
            char buffer[2] = {c, '\0'};
            print_token(TOKEN_OP, buffer);
        }
    }

    fclose(fp);
}

int main() {
    const char *filename = "/home/eduardo-da-paz/Documents/university/ulbra/compilers/task_2/entrada.txt"; // nome do arquivo de entrada
    analyze_file(filename);
    return 0;
}
