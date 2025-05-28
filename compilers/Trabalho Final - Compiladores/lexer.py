import ply.lex as lex

# Tokens
tokens = [
    'ID', 'NUMBER', 'CHAR', 'STRING', 'EQUALS',
    'SEMICOLON', 'COMMA'
]

# Palavras reservadas
reserved = {
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR_TYPE'
}
tokens += list(reserved.values())

# Expressões regulares
t_EQUALS = r'='
t_SEMICOLON = r';'
t_COMMA = r','

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    if '.' in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t

def t_CHAR(t):
    r'\'(.|\\n|\\t)\''
    t.value = t.value[1:-1]
    return t

def t_STRING(t):
    r'\"[^\"]*\"'
    t.value = t.value[1:-1]
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caractere inválido: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()
