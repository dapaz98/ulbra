
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BREAK CASE CHAR CHAR_TYPE COLON COMMA DEFAULT DIVIDE ELSE EQEQ EQUALS FLOAT FOR FOR GE GT ID IF INT LBRACE LE LPAREN LT MINUS NE NUMBER PLUS RBRACE RPAREN SEMICOLON STRING SWITCH TIMES WHILE WHILEdeclaracoes : tipo lista_variaveis SEMICOLONtipo : INT\n            | FLOAT\n            | CHAR_TYPElista_variaveis : variavel\n                       | lista_variaveis COMMA variavelvariavel : ID\n                | ID EQUALS valorvalor : NUMBER\n             | CHAR\n             | STRINGcomando : IF LPAREN condicao RPAREN LBRACE comandos RBRACE\n               | IF LPAREN condicao RPAREN LBRACE comandos RBRACE ELSE LBRACE comandos RBRACEcomando : SWITCH LPAREN ID RPAREN LBRACE lista_cases RBRACElista_cases : lista_cases case\n                   | case\n                   | defaultcase : CASE valor COLON LBRACE comandos BREAK SEMICOLON RBRACEdefault : DEFAULT COLON LBRACE comandos RBRACEcondicao : ID relop valorrelop : EQEQ\n             | NE\n             | LT\n             | GT\n             | LE\n             | GEcomando : WHILE LPAREN condicao RPAREN LBRACE comandos RBRACEcomando : FOR LPAREN inicializacao SEMICOLON condicao SEMICOLON incremento RPAREN LBRACE comandos RBRACEinicializacao : ID EQUALS valorincremento : ID EQUALS expressaocomandos : comandos comando_matematico\n                | comando_matematicocomando_matematico : ID EQUALS expressao SEMICOLONexpressao : valor\n                 | valor operador valoroperador : PLUS\n                | MINUS\n                | TIMES\n                | DIVIDE'
    
_lr_action_items = {'INT':([0,],[3,]),'FLOAT':([0,],[4,]),'CHAR_TYPE':([0,],[5,]),'$end':([1,9,],[0,-1,]),'ID':([2,3,4,5,10,],[8,-2,-3,-4,8,]),'SEMICOLON':([6,7,8,12,13,14,15,16,],[9,-5,-7,-6,-8,-9,-10,-11,]),'COMMA':([6,7,8,12,13,14,15,16,],[10,-5,-7,-6,-8,-9,-10,-11,]),'EQUALS':([8,],[11,]),'NUMBER':([11,],[14,]),'CHAR':([11,],[15,]),'STRING':([11,],[16,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'declaracoes':([0,],[1,]),'tipo':([0,],[2,]),'lista_variaveis':([2,],[6,]),'variavel':([2,10,],[7,12,]),'valor':([11,],[13,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> declaracoes","S'",1,None,None,None),
  ('declaracoes -> tipo lista_variaveis SEMICOLON','declaracoes',3,'p_declaracoes','parser.py',6),
  ('tipo -> INT','tipo',1,'p_tipo','parser.py',10),
  ('tipo -> FLOAT','tipo',1,'p_tipo','parser.py',11),
  ('tipo -> CHAR_TYPE','tipo',1,'p_tipo','parser.py',12),
  ('lista_variaveis -> variavel','lista_variaveis',1,'p_lista_variaveis','parser.py',16),
  ('lista_variaveis -> lista_variaveis COMMA variavel','lista_variaveis',3,'p_lista_variaveis','parser.py',17),
  ('variavel -> ID','variavel',1,'p_variavel','parser.py',24),
  ('variavel -> ID EQUALS valor','variavel',3,'p_variavel','parser.py',25),
  ('valor -> NUMBER','valor',1,'p_valor','parser.py',32),
  ('valor -> CHAR','valor',1,'p_valor','parser.py',33),
  ('valor -> STRING','valor',1,'p_valor','parser.py',34),
  ('comando -> IF LPAREN condicao RPAREN LBRACE comandos RBRACE','comando',7,'p_comando_if','parser.py',39),
  ('comando -> IF LPAREN condicao RPAREN LBRACE comandos RBRACE ELSE LBRACE comandos RBRACE','comando',11,'p_comando_if','parser.py',40),
  ('comando -> SWITCH LPAREN ID RPAREN LBRACE lista_cases RBRACE','comando',7,'p_comando_switch','parser.py',44),
  ('lista_cases -> lista_cases case','lista_cases',2,'p_lista_cases','parser.py',48),
  ('lista_cases -> case','lista_cases',1,'p_lista_cases','parser.py',49),
  ('lista_cases -> default','lista_cases',1,'p_lista_cases','parser.py',50),
  ('case -> CASE valor COLON LBRACE comandos BREAK SEMICOLON RBRACE','case',8,'p_case','parser.py',54),
  ('default -> DEFAULT COLON LBRACE comandos RBRACE','default',5,'p_default','parser.py',58),
  ('condicao -> ID relop valor','condicao',3,'p_condicao','parser.py',62),
  ('relop -> EQEQ','relop',1,'p_relop','parser.py',66),
  ('relop -> NE','relop',1,'p_relop','parser.py',67),
  ('relop -> LT','relop',1,'p_relop','parser.py',68),
  ('relop -> GT','relop',1,'p_relop','parser.py',69),
  ('relop -> LE','relop',1,'p_relop','parser.py',70),
  ('relop -> GE','relop',1,'p_relop','parser.py',71),
  ('comando -> WHILE LPAREN condicao RPAREN LBRACE comandos RBRACE','comando',7,'p_comando_while','parser.py',76),
  ('comando -> FOR LPAREN inicializacao SEMICOLON condicao SEMICOLON incremento RPAREN LBRACE comandos RBRACE','comando',11,'p_comando_for','parser.py',80),
  ('inicializacao -> ID EQUALS valor','inicializacao',3,'p_inicializacao','parser.py',84),
  ('incremento -> ID EQUALS expressao','incremento',3,'p_incremento','parser.py',88),
  ('comandos -> comandos comando_matematico','comandos',2,'p_comandos','parser.py',93),
  ('comandos -> comando_matematico','comandos',1,'p_comandos','parser.py',94),
  ('comando_matematico -> ID EQUALS expressao SEMICOLON','comando_matematico',4,'p_comando_matematico','parser.py',98),
  ('expressao -> valor','expressao',1,'p_expressao','parser.py',102),
  ('expressao -> valor operador valor','expressao',3,'p_expressao','parser.py',103),
  ('operador -> PLUS','operador',1,'p_operador','parser.py',107),
  ('operador -> MINUS','operador',1,'p_operador','parser.py',108),
  ('operador -> TIMES','operador',1,'p_operador','parser.py',109),
  ('operador -> DIVIDE','operador',1,'p_operador','parser.py',110),
]
