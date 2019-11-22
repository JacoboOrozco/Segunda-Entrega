import ply.lex as lex
import sys

# list of tokens
tokens = (
    # Reserverd words
    # 'AUTO',
    'ABSOLUTE',
    'AND',
    'ARRAY',
    'ASM',
    'PROGRAM',
    'PACKED',
    'PROCEDURE',
    'ELSE',
    'END',
    'BREAK',
    'BEGIN',
    'CASE',
    'CONST',
    'CONSTRUCTOR',
    'IF',
    'INTEGER',
    'LONG',
    'SHORT',
    'TO',
    'TYPE',
    'TRY',
    'THEN',
    'DOUBLE',
    'FLOAT',
    'CHAR',
    'BOOLEAN',
    'DEFINE',
    'DESTRUCTOR',
    'INCLUDE',
    'DEFAULT',
    'FOR',
    'SWITCH',
    'STRING',
    'REAL',
    'RETURN',
    'RECORD',
    'VOID',
    'WHILE',
    'DO',
    'DOWNTO',
    'FILE',
    'FUNCTION',
    'IMPLEMENTATION',
    'IN',
    'INHERITED',
    'INLINE',
    'INTERFACE',
    'LABEL',
    'MOD',
    'NIL',
    'NOT',
    'OBJECT',
    'OF',
    'ON',
    'OPERATOR',
    'OR',
    'USES',
    'VAR',
    'WITH',

    # Symbols
    'SUM',
    'PLUSPLUS',
    # 'PLUSEQUAL',
    'RES',
    'MINUSMINUS',
    # 'MINUSEQUAL',
    'MUL',
    'DIVI',
    'MENOR',
    'MENORIGUAL',
    'MAYOR',
    'MAYORIGUAL',
    'IGUALNOT',
    'EQUAL',
    'DEQUAL',
    'DISTINT',
    'ISEQUAL',
    'IS',
    'SEMICOLON',
    'COMMA',
    'APAREN',
    'CPAREN',
    'LBRACK',
    'RBRACK',
    'LBLOCK',
    'RBLOCK',
    'COLON',
    'AMPERSANT',
    'HASHTAG',
    'DOT',
    'COMI',

    # Others
    'ID',
    'NUMBER',
)

# Regular expressions rules for a simple tokens
t_SUM = r'\+'
t_RES = r'-'
t_MUL = r'\*'
t_DIVI = r'/'
t_EQUAL = r'='
t_DISTINT = r'!'
t_MENOR = r'<'
t_MAYOR = r'>'
t_IGUALNOT = r'<>'
t_SEMICOLON = ';'
t_COMMA = r','
t_APAREN = r'\('
t_CPAREN = r'\)'
t_LBRACK = r'\['
t_RBRACK = r'\]'
t_LBLOCK = r'{'
t_RBLOCK = r'}'
t_COLON = r':'
t_AMPERSANT = r'\&'
t_HASHTAG = r'\#'
t_DOT = r'\.'
t_COMI = r"'"


def t_AUTO(t):
    r'auto'
    return t


def t_AND(t):
    r'and'
    return t


def t_ARRAY(t):
    r'array'
    return t


def t_ASM(t):
    r'asm'
    return t


def t_ABSOLUTE(t):
    r'absolute'
    return t


def t_BREAK(t):
    r'break'
    return t


def t_BEGIN(t):
    r'Begin|begin|BEGIN'
    return t


def t_CASE(t):
    r'case'
    return t


def t_CONST(t):
    r'const'
    return t


def t_CONSTRUCTOR(t):
    r'constructor'
    return t


def t_CHAR(t):
    r'char'
    return t


def t_BOOLEAN(t):
    r'boolean'
    return t


def t_INCLUDE(t):
    r'include'
    return t


def t_DEFINE(t):
    r'define'
    return t


def t_DESTRUCTOR(t):
    r'destructor'
    return t


def t_CONTINUE(t):
    r'continue'
    return t


def t_DEFAULT(t):
    r'default'
    return t


def t_DO(t):
    r'do'
    return t


def t_DOWNTO(t):
    r'downto'
    return t


def t_DOUBLE(t):
    r'double'
    return t


def t_ELSE(t):
    r'else'
    return t


def t_END(t):
    r'end'
    return t


def t_FLOAT(t):
    r'float'
    return t


def t_FILE(t):
    r'file'
    return t


def t_FOR(t):
    r'for'
    return t


def t_FUNCTION(t):
    r'function'
    return t


def t_IF(t):
    r'if'
    return t


def t_IS(t):
    r'is'
    return t


def t_INTEGER(t):
    r'integer'
    return t


def t_INTERFACE(t):
    r'interface'
    return t


def t_IN(t):
    r'in'
    return t


def t_INLINE(t):
    r'inline'
    return t


def t_INHERITED(t):
    r'inherited'
    return t


def t_IMPLEMENTATION(t):
    r'implementation'
    return t


def t_SHORT(t):
    r'short'
    return t


def t_TO(t):
    r'to'
    return t


def t_TYPE(t):
    r'type'
    return t


def t_TRY(t):
    r'try'
    return t


def t_THEN(t):
    r'then'
    return t


def t_LONG(t):
    r'long'
    return t


def t_LABEL(t):
    r'label'
    return t


def t_MOD(t):
    r'mod'
    return t


def t_NIL(t):
    r'and'
    return t


def t_NOT(t):
    r'not'
    return t


def t_REAL(t):
    r'real'
    return t


def t_RETURN(t):
    r'return'
    return t


def t_RECORD(t):
    r'record'
    return t


def t_OBJECT(t):
    r'object'
    return t


def t_OF(t):
    r'of'
    return t


def t_ON(t):
    r'on'
    return t


def t_OR(t):
    r'or'
    return t


def t_OPERATOR(t):
    r'operator'
    return t


def t_PROGRAM(t):
    r'program'
    return t


def t_PROCEDURE(t):
    r'procedure'
    return t


def t_PACKED(t):
    r'packed'
    return t


def t_USES(t):
    r'uses'
    return t


def t_VAR(t):
    r'var'
    return t


def t_SWITCH(t):
    r'switch'
    return t


def t_STRING(t):
    r'string'
    return t


def t_VOID(t):
    r'void'
    return t


def t_WHILE(t):
    r'while'
    return t


def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t


def t_ID(t):
    r'\w+(_\d\w)*'
    return t


def t_MENORIGUAL(t):
    r'<='
    return t


def t_MAYORIGUAL(t):
    r'>='
    return t


def t_DEQUAL(t):
    r'!='
    return t


def t_ISEQUAL(t):
    r'=='
    return t


def t_MINUSMINUS(t):
    r'--'
    return t


def t_PLUSPLUS(t):
    r'\+\+'
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_comments(t):
    r'(\*(.|\n)*?\*)'
    t.lexer.lineno += t.value.count('\n')


def t_comments_C99(t):
    r'{(.)*?\n}'
    t.lexer.lineno += 1


def t_error(t):
    print("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)


def test(data, lexer):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)


lexer = lex.lex()


if __name__ == '__main__':
    if (len(sys.argv) > 1):
        fin = sys.argv[1]
    else:
        fin = 'evaluacion1'
    f = open(fin, 'r')
    data = f.read()
    print(data)
    lexer.input(data)
    test(data, lexer)
    input()
