import ply.lex as lex
import ply.yacc as yacc

# ==============================
# Analisador Léxico
# ==============================

# Palavras-chave
reserved = {
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR',
}

# Tokens
tokens = [
    'ID', 'NUMBER', 'CHAR_CONST',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'EQUALS', 'SEMI',
    'QUOTE'
] + list(reserved.values())

# Expressões regulares para tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_EQUALS  = r'='
t_SEMI    = r';'
t_QUOTE   = r"'"

# Ignorar espaços e tabulações
t_ignore = ' \t'

def t_CHAR_CONST(t):
    r"\'[a-zA-Z0-9]\'"
    t.value = t.value[1]  # remove aspas
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')  # Verifica se é palavra-chave
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# ==============================
# Analisador Sintático
# ==============================

# Precedência
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

# Regras da gramática

def p_statement(p):
    '''statement : type ID EQUALS expression SEMI'''
    print("Linha válida!")

def p_type(p):
    '''type : INT
            | FLOAT
            | CHAR'''
    p[0] = p[1]

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    p[0] = ('binop', p[2], p[1], p[3])

def p_expression_number(p):
    '''expression : NUMBER'''
    p[0] = p[1]

def p_expression_id(p):
    '''expression : ID'''
    p[0] = p[1]

def p_expression_char(p):
    '''expression : CHAR_CONST'''
    p[0] = p[1]

def p_error(p):
    print("Erro de sintaxe!")

parser = yacc.yacc()

# ==============================
# Execução
# ==============================

if __name__ == '__main__':
    while True:
        try:
            s = input('Código > ')
        except EOFError:
            break
        if not s:
            continue
        result = parser.parse(s)
