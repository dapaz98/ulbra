import ply.lex as lex

# Tokens
tokens = [
    'ID', 'NUMBER', 'CHAR', 'STRING', 'EQUALS',
    'SEMICOLON', 'COMMA',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'EQEQ', 'NE', 'LT', 'GT', 'LE', 'GE',
    'COLON'
]

# Palavras reservadas
reserved = {
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR_TYPE',
    'if': 'IF',
    'else': 'ELSE',
    'switch': 'SWITCH',
    'case': 'CASE',
    'default': 'DEFAULT',
    'break': 'BREAK'
}
tokens += list(reserved.values())

# Expressões regulares
t_EQUALS     = r'='
t_SEMICOLON  = r';'
t_COMMA      = r','
t_LPAREN     = r'\('
t_RPAREN     = r'\)'
t_LBRACE     = r'\{'
t_RBRACE     = r'\}'
t_PLUS       = r'\+'
t_MINUS      = r'-'
t_TIMES      = r'\*'
t_DIVIDE     = r'/'
t_EQEQ       = r'=='
t_NE         = r'!='
t_LE         = r'<='
t_GE         = r'>='
t_LT         = r'<'
t_GT         = r'>'
t_COLON      = r':'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
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
