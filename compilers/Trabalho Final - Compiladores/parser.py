
import ply.yacc as yacc
from lexer import tokens

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

def p_error(p):
    print("Erro de sintaxe", p)

parser = yacc.yacc()


def main():
    # Testes
    entradas = [
        "int a;",
        "float x, y = 2.5, z;",
        "char c = 'a';",
        "char nome = \"Ana\";"
    ]

    for entrada in entradas:
        print("\nAnalisando:", entrada)
        parser.parse(entrada)

if __name__ == '__main__':
    main()