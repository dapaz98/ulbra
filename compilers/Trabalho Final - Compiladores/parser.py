import ply.yacc as yacc
from lexer import tokens

# Declarações de variáveis
def p_declaracoes(p):
    '''declaracoes : tipo lista_variaveis SEMICOLON'''
    print("Declaração válida:", p[1], p[2])

def p_tipo(p):
    '''tipo : INT
            | FLOAT
            | CHAR_TYPE'''
    p[0] = p[1]

def p_lista_variaveis(p):
    '''lista_variaveis : variavel
                       | lista_variaveis COMMA variavel'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_variavel(p):
    '''variavel : ID
                | ID EQUALS valor'''
    if len(p) == 2:
        p[0] = (p[1], None)
    else:
        p[0] = (p[1], p[3])

def p_valor(p):
    '''valor : NUMBER
             | CHAR
             | STRING'''
    p[0] = p[1]

# Comandos de controle
def p_comando_if(p):
    '''comando : IF LPAREN condicao RPAREN LBRACE comandos RBRACE
               | IF LPAREN condicao RPAREN LBRACE comandos RBRACE ELSE LBRACE comandos RBRACE'''
    print("Comando IF reconhecido")

def p_comando_switch(p):
    '''comando : SWITCH LPAREN ID RPAREN LBRACE lista_cases RBRACE'''
    print("Comando SWITCH reconhecido")

def p_lista_cases(p):
    '''lista_cases : lista_cases case
                   | case
                   | default'''
    pass

def p_case(p):
    '''case : CASE valor COLON LBRACE comandos BREAK SEMICOLON RBRACE'''
    pass

def p_default(p):
    '''default : DEFAULT COLON LBRACE comandos RBRACE'''
    pass

def p_condicao(p):
    '''condicao : ID relop valor'''
    pass

def p_relop(p):
    '''relop : EQEQ
             | NE
             | LT
             | GT
             | LE
             | GE'''
    p[0] = p[1]

# Expressões e comandos matemáticos
def p_comandos(p):
    '''comandos : comandos comando_matematico
                | comando_matematico'''
    pass

def p_comando_matematico(p):
    '''comando_matematico : ID EQUALS expressao SEMICOLON'''
    print(f"Comando matemático: {p[1]} = ...")

def p_expressao(p):
    '''expressao : valor
                 | valor operador valor'''
    pass

def p_operador(p):
    '''operador : PLUS
                | MINUS
                | TIMES
                | DIVIDE'''
    p[0] = p[1]

def p_error(p):
    print("Erro de sintaxe", p)

parser = yacc.yacc()

def main():
    entradas = [
        "int a;",
        "float x, y = 2.5, z;",
        "char c = 'a';",
        "char nome = \"Ana\";",
        "if (x > 5) { a = 3; } else { a = 2; }",
        "switch(x) { case 1: { y = 10; break; } default: { y = 0; } }"
    ]

    for entrada in entradas:
        print("\nAnalisando:", entrada)
        parser.parse(entrada)

if __name__ == '__main__':
    main()
