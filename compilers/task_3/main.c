#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

typedef enum {
    TOKEN_ID, TOKEN_NUM, TOKEN_OP, TOKEN_ASSIGN, TOKEN_END, TOKEN_INVALID
} TokenType;

typedef struct {
    TokenType type;
    char lexeme[100];
} Token;

const char *input;
int pos = 0;

// Função para pular espaços
void skip_whitespace() {
    while (isspace(input[pos])) pos++;
}

// Função para reconhecer identificadores (ID)
Token get_id() {
    Token token;
    token.type = TOKEN_ID;
    int i = 0;
    while (isalpha(input[pos]) || isdigit(input[pos]) || input[pos] == '_') {
        token.lexeme[i++] = input[pos++];
    }
    token.lexeme[i] = '\0';
    return token;
}

// Função para reconhecer números (NUM)
Token get_num() {
    Token token;
    token.type = TOKEN_NUM;
    int i = 0;
    while (isdigit(input[pos])) {
        token.lexeme[i++] = input[pos++];
    }
    token.lexeme[i] = '\0';
    return token;
}

// Retorna o próximo token
Token get_next_token() {
    skip_whitespace();
    Token token;

    char current = input[pos];
    if (current == '\0') {
        token.type = TOKEN_END;
        return token;
    }

    if (isalpha(current) || current == '_') {
        return get_id();
    }

    if (isdigit(current)) {
        return get_num();
    }

    if (current == '+' || current == '-' || current == '*' || current == '/') {
        token.type = TOKEN_OP;
        token.lexeme[0] = current;
        token.lexeme[1] = '\0';
        pos++;
        return token;
    }

    if (current == '=') {
        token.type = TOKEN_ASSIGN;
        token.lexeme[0] = current;
        token.lexeme[1] = '\0';
        pos++;
        return token;
    }

    token.type = TOKEN_INVALID;
    token.lexeme[0] = current;
    token.lexeme[1] = '\0';
    pos++;
    return token;
}

// Variáveis globais para tokens
Token current_token;

// Avança para o próximo token
void advance() {
    current_token = get_next_token();
}

// Verifica se o token atual é do tipo esperado
int match(TokenType type) {
    if (current_token.type == type) {
        advance();
        return 1;
    }
    return 0;
}

// <termo> ::= <ID> | <NUM>
int termo() {
    return match(TOKEN_ID) || match(TOKEN_NUM);
}

// <expressao> ::= <termo> | <expressao> <op> <termo>
int expressao() {
    if (!termo()) return 0;

    while (current_token.type == TOKEN_OP) {
        advance();
        if (!termo()) return 0;
    }

    return 1;
}

// <linha> ::= <ID> "=" <expressao>
int linha() {
    if (!match(TOKEN_ID)) return 0;
    if (!match(TOKEN_ASSIGN)) return 0;
    if (!expressao()) return 0;
    return current_token.type == TOKEN_END;
}

int validar(char *linha_input) {
    input = linha_input;
    pos = 0;
    advance();
    return linha();
}

int main() {
    char *testes_validos[] = {
        "salario = salario * 3",
        "salario = salario * bonus",
        "salario = 1000 * 50",
        "salario = salario - descontos + beneficios"
    };

    char *testes_invalidos[] = {
        "salario = salario *",
        "salario = *",
        "salario =",
        "salario"
    };

    printf("Testes válidos:\n");
    for (int i = 0; i < 4; i++) {
        printf("'%s' => %s\n", testes_validos[i], validar(testes_validos[i]) ? "ACEITO" : "REJEITADO");
    }

    printf("\nTestes inválidos:\n");
    for (int i = 0; i < 4; i++) {
        printf("'%s' => %s\n", testes_invalidos[i], validar(testes_invalidos[i]) ? "ACEITO" : "REJEITADO");
    }

    return 0;
}
