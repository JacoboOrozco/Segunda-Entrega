import sys
import ply.lex as lex

# Lista de palabras reservadas
reservadas = {
    'absolute': 'ABSOLUTE',
    'and': 'AND',
    'array': 'ARRAY',
    'asm': 'ASM',
    'begin': 'BEGIN',
    'break': 'BREAK',
    'case': 'CASE',
    'const': 'CONST',
    'constructor': 'CONSTRUCTOR',
    'continue': 'CONTINUE',
    'destructor': 'DESTRUCTOR',
    'div': 'DIV',
    'do': 'DO',
    'downto': 'DOWNTO',
    'else': 'ELSE',
    'end': 'END',
    'file': 'FILE',
    'for': 'FOR',
    'function': 'FUNCTION',
    'goto': 'GOTO',
    'if': 'IF',
    'implementation': 'IMPLEMENTATION',
    'in': 'IN',
    'inherited': 'INHERITED',
    'inline': 'INLINE',
    'interface': 'INTERFACE',
    'label': 'LABEL',
    'mod': 'MOD',
    'nil': 'NIL',
    'not': 'NOT',
    'object': 'OBJECT',
    'of': 'OF',
    'on': 'ON',
    'operator': 'OPERATOR',
    'or': 'OR',
    'packed': 'PACKED',
    'procedure': 'PROCEDURE',
    'program': 'PROGRAM',
    'record': 'RECORD',
    'reintroduce': 'REINTRODUCE',
    'repeat': 'REPEAT',
    'self': 'SELF',
    'set': 'SET',
    'shl': 'SHL',
    'shr': 'SHR',
    'string': 'STRING',
    'then': 'THEN',
    'to': 'TO',
    'type': 'TYPE',
    'unit': 'UNIT',
    'until': 'UNTIL',
    'uses': 'USES',
    'var': 'VAR',
    'while': 'WHILE',
    'with': 'WITH',
    'xor': 'XOR',
    'as': 'AS',
    'class': 'CLASS',
    'except': 'EXCEPT',
    'exports': 'EXPORTS',
    'finalization': 'FINALIZATION',
    'finally': 'FINALLY',
    'initialization': 'INITIALIZATION',
    'is': 'IS',
    'library': 'LIBRARY',
    'property': 'PROPERTY',
    'raise': 'RAISE',
    'threadvar': 'THREADVAR',
    'try': 'TRY',
    'dispose': 'DISPOSE',
    'exit': 'EXIT',
    'new': 'NEW',
    'integer': 'INTEGER',
    'real': 'REAL',
    'char': 'CHAR',
    'return': 'RETURN'




}

# Lista de tokens
tokens = ['NUMBER', 'FLOAT', 'ID', 'SUM', 'RES', 'MUL', 'DIVI', 'APAREN', 'CPAREN', 'ERROR_LEXICO', 'MAYOR', 'MAYORIGUAL', 'MENOR', 'MENORIGUAL',
          'DIFERENTE', 'IGUAL', 'BOOLEAN', 'ERROR_SINTAXIS_ABSOLUTE', 'ERROR_SINTAXIS_AND', 'SIMBOLOS', 'COMENTARIOS', 'HASHTAG', 'DOT',
          'SEMICOLON', 'COMMA', 'EQUAL', 'LBLOCK', 'RBLOCK', 'COLON', 'IGUALNOT', 'AMPERSANT', 'RBRAK', 'LBRAK'] + list(reservadas.values())


# Reglas de expresiones regulares para tokens simples
t_RBRAK = r'\['
t_LBRAK = r'\]'
t_AMPERSANT = r'&'
t_IGUALNOT = r'\<>'
t_HASHTAG = r'\#'
t_DOT = r'\.'
t_SEMICOLON = r'\;'
t_COMMA = r'\,'
t_EQUAL = r'\ ='
t_LBLOCK = r'\{'
t_RBLOCK = r'\}'
t_COLON = r'\:'
t_ignore = r'\s'
t_SUM = r'\+'
t_RES = r'-'
t_MUL = r'\*'
t_DIVI = r'/'
t_APAREN = r'\('
t_CPAREN = r'\)'
t_NUMBER = r'(([0-9]+)|([0-9]+.[0-9]+))'
t_MAYOR = r'>'
t_MAYORIGUAL = r'>='
t_MENOR = r'<'
t_MENORIGUAL = r'<='
t_ID = r'([a-z]|[A-Z]|[0-9]|\s|_)+'
t_ERROR_LEXICO = r'([0-9])+([a-z]|[A-Z])+'
t_SIMBOLOS = r"([-]|[_]|[?]|[¿]|[%]|[$]|[!]|[&]|[;]|[,]|[=]|[:]|[.]|['])"
t_COMENTARIOS = r'\ [(][*]([a-z]|[A-Z]|[0-9]|\s|[-]|[_]|[?]|[¿]|[%]|[$]|[!]|[&]|[+]|[(]|[)]|[*]|[/]|[;]|[,]|[=]|[:]|[.]|[|]|["]|[@])*[*][)] | [{]([a-z]|[A-Z]|[0-9]|\s|[-]|[_]|[?]|[¿]|[%]|[$]|[!]|[&]|[+]|[(]|[)]|[*]|[/]|[;]|[,]|[=]|[:]|[.]|[|]|["]|[@])*[}] '


def t_ABSOLUTE(t):
    r'absolute'
    t.type = reservadas.get(t.value, 'ABSOLUTE')
    return t


def t_AND(t):
    r'and'
    t.type = reservadas.get(t.value, 'AND')
    return t


def t_ARRAY(t):
    r'array'
    t.type = reservadas.get(t.value, 'ARRAY')
    return t


def t_ASM(t):
    r'asm'
    t.type = reservadas.get(t.value, 'ASM')
    return t


def t_BEGIN(t):
    r'begin'
    t.type = reservadas.get(t.value, 'BEGIN')
    return t


def t_BREAK(t):
    r'break'
    t.type = reservadas.get(t.value, 'BREAK')
    return t


def t_CASE(t):
    r'case'
    t.type = reservadas.get(t.value, 'CASE')
    return t


def t_CONSTRUCTOR(t):
    r'constructor'
    t.type = reservadas.get(t.value, 'CONSTRUCTOR')
    return t


def t_CONST(t):
    r'const'
    t.type = reservadas.get(t.value, 'CONST')
    return t


def t_CONTINUE(t):
    r'continue'
    t.type = reservadas.get(t.value, 'CONTINUE')
    return t


def t_CHAR(t):
    r'char'
    t.type = reservadas.get(t.value, 'CHAR')
    return t


def t_DESTRUCTOR(t):
    r'destructor'
    t.type = reservadas.get(t.value, 'DESTRUCTOR')
    return t


def t_DIV(t):
    r'div'
    t.type = reservadas.get(t.value, 'DIV')
    return t


def t_DOWNTO(t):
    r'downto'
    t.type = reservadas.get(t.value, 'DOWNTO')
    return t


def t_DO(t):
    r'do'
    t.type = reservadas.get(t.value, 'DO')
    return t


def t_ELSE(t):
    r'downto'
    t.type = reservadas.get(t.value, 'ELSE')
    return t


def t_END(t):
    r'end'
    t.type = reservadas.get(t.value, 'END')
    return t


def t_FILE(t):
    r'file'
    t.type = reservadas.get(t.value, 'FILE')
    return t


def t_FOR(t):
    r'for'
    t.type = reservadas.get(t.value, 'FOR')
    return t


def t_FUNCTION(t):
    r'function'
    t.type = reservadas.get(t.value, 'FUNCTION')
    return t


def t_GOTO(t):
    r'goto'
    t.type = reservadas.get(t.value, 'GOTO')
    return t


def t_IF(t):
    r'if'
    t.type = reservadas.get(t.value, 'IF')
    return t


def t_IMPLEMENTATION(t):
    r'implementation'
    t.type = reservadas.get(t.value, 'IMPLEMENTATION')
    return t


def t_INHERITED(t):
    r'inherited'
    t.type = reservadas.get(t.value, 'INHERITED')
    return t


def t_INTEGER(t):
    r'integer'
    t.type = reservadas.get(t.value, 'INTEGER')
    return t


def t_INLINE(t):
    r'inline'
    t.type = reservadas.get(t.value, 'INLINE')
    return t


def t_INTERFACE(t):
    r'interface'
    t.type = reservadas.get(t.value, 'INTERFACE')
    return t


def t_INITIALIZATION(t):
    r'initialization'
    t.type = reservadas.get(t.value, 'INITIALIZATION')
    return t


def t_IN(t):
    r'in'
    t.type = reservadas.get(t.value, 'IN')
    return t


def t_LABEL(t):
    r'label'
    t.type = reservadas.get(t.value, 'LABEL')
    return t


def t_MOD(t):
    r'mod'
    t.type = reservadas.get(t.value, 'MOD')
    return t


def t_NIL(t):
    r'nil'
    t.type = reservadas.get(t.value, 'NIL')
    return t


def t_NOT(t):
    r'not'
    t.type = reservadas.get(t.value, 'NOT')
    return t


def t_OBJECT(t):
    r'object'
    t.type = reservadas.get(t.value, 'OBJECT')
    return t


def t_OF(t):
    r'of'
    t.type = reservadas.get(t.value, 'OF')
    return t


def t_ON(t):
    r'on'
    t.type = reservadas.get(t.value, 'ON')
    return t


def t_OPERATOR(t):
    r'operator'
    t.type = reservadas.get(t.value, 'OPERATOR')
    return t


def t_OR(t):
    r'or'
    t.type = reservadas.get(t.value, 'OR')
    return t


def t_PACKED(t):
    r'packed'
    t.type = reservadas.get(t.value, 'PACKED')
    return t


def t_PROGRAM(t):
    r'program'
    t.type = reservadas.get(t.value, 'PROGRAM')
    return t


def t_PROCEDURE(t):
    r'procedure'
    t.type = reservadas.get(t.value, 'PROCEDURE')
    return t


def t_REAL(t):
    r'real'
    t.type = reservadas.get(t.value, 'REAL')
    return t


def t_RECORD(t):
    r'record'
    t.type = reservadas.get(t.value, 'RECORD')
    return t


def t_REINTRODUCE(t):
    r'reintroduce'
    t.type = reservadas.get(t.value, 'REINTRODUCE')
    return t


def t_REPEAT(t):
    r'repeat'
    t.type = reservadas.get(t.value, 'REPEAT')
    return t


def t_RETURN(t):
    r'return'
    t.type = reservadas.get(t.value, 'RETURN')
    return t


def t_SELF(t):
    r'self'
    t.type = reservadas.get(t.value, 'SELF')
    return t


def t_SET(t):
    r'set'
    t.type = reservadas.get(t.value, 'SET')
    return t


def t_SHL(t):
    r'shl'
    t.type = reservadas.get(t.value, 'SHL')
    return t


def t_SHR(t):
    r'shr'
    t.type = reservadas.get(t.value, 'SHR')
    return t


def t_STRING(t):
    r'string'
    t.type = reservadas.get(t.value, 'STRING')
    return t


def t_THEN(t):
    r'then'
    t.type = reservadas.get(t.value, 'THEN')
    return t


def t_TO(t):
    r'to'
    t.type = reservadas.get(t.value, 'TO')
    return t


def t_TYPE(t):
    r'type'
    t.type = reservadas.get(t.value, 'TYPE')
    return t


def t_UNIT(t):
    r'unit'
    t.type = reservadas.get(t.value, 'UNIT')
    return t


def t_UNTIL(t):
    r'until'
    t.type = reservadas.get(t.value, 'UNTIL')
    return t


def t_USES(t):
    r'uses'
    t.type = reservadas.get(t.value, 'USES')
    return t


def t_VAR(t):
    r'var'
    t.type = reservadas.get(t.value, 'VAR')
    return t


def t_WHILE(t):
    r'while'
    t.type = reservadas.get(t.value, 'WHILE')
    return t


def t_WITH(t):
    r'with'
    t.type = reservadas.get(t.value, 'WITH')
    return t


def t_XOR(t):
    r'xor'
    t.type = reservadas.get(t.value, 'XOR')
    return t


def t_TRUE(t):
    r'True'
    t.type = reservadas.get(t.value, 'BOOLEAN')
    return t


def t_FALSE(t):
    r'False'
    t.type = reservadas.get(t.value, 'BOOLEAN')
    return t


def t_AS(t):
    r'as'
    t.type = reservadas.get(t.value, 'AS')
    return t


def t_CLASS(t):
    r'class'
    t.type = reservadas.get(t.value, 'CLASS')
    return t


def t_EXCEPT(t):
    r'except'
    t.type = reservadas.get(t.value, 'EXCEPT')
    return t


def t_EXPORTS(t):
    r'exports'
    t.type = reservadas.get(t.value, 'EXPORTS')
    return t


def t_FINALIZATION(t):
    r'finalization'
    t.type = reservadas.get(t.value, 'FINALIZATION')
    return t


def t_FINALLY(t):
    r'finally'
    t.type = reservadas.get(t.value, 'FINALLY')
    return t


def t_IS(t):
    r'is'
    t.type = reservadas.get(t.value, 'IS')
    return t


def t_LIBRARY(t):
    r'library'
    t.type = reservadas.get(t.value, 'LIBRARY')
    return t


def t_PROPERTY(t):
    r'property'
    t.type = reservadas.get(t.value, 'PROPERTY')
    return t


def t_RAISE(t):
    r'raise'
    t.type = reservadas.get(t.value, 'RAISE')
    return t


def t_THREADVAR(t):
    r'threadvar'
    t.type = reservadas.get(t.value, 'THREADVAR')
    return t


def t_TRY(t):
    r'try'
    t.type = reservadas.get(t.value, 'TRY')
    return t


def t_DISPOSE(t):
    r'dispose'
    t.type = reservadas.get(t.value, 'DISPOSE')
    return t


def t_EXIT(t):
    r'exit'
    t.type = reservadas.get(t.value, 'EXIT')
    return t


def t_NEW(t):
    r'new'
    t.type = reservadas.get(t.value, 'NEW')
    return t

# def t_ID(t):
#    r'([a-z]|[A-Z])'
#    t.type = reservadas.get(t.value,'ID')    # Revisa las palabras reservadas
#    return t


# def t_FLOAT(t):
#    r'[0-9]+.[0-9]+'
#    return t
# def t_DIVI(t):
#    r'/'
#    return t


# Definicion de error que se va a mostrar cuando un caracter ingresado no es valido
def t_error(t):
    print("******Caracter no valido: {}".format(t.value[0]))
    t.lexer.skip(1)
    return t


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
        fin = 'evaluacion3'
    f = open(fin, 'r')
    data = f.read()
    print(data)
    lexer.input(data)
    test(data, lexer)
    input()
