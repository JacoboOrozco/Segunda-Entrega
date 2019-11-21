import ply.yacc as yacc
from minipascal_lexer import tokens
import minipascal_lexer
import sys

VERBOSE = 1


def p_program(p):
    'program : declaration_list'
    pass


def p_declaration_list_1(p):
    'declaration_list : declaration_list declaration'
    pass


def p_delcaration_list_2(p):
    'declaration_list : declaration'
    pass


def p_declaration(p):
    '''declaration : var_declaration
                          | proce_declaration
                          | header_declararion
    '''
    pass


def p_header_declaration_1(p):
    'header_declaration : HASHTAG DEFINE ID NUMBER'
    pass


def p_header_declaration_2(p):
    'header_declaration : HASHTAG INCLUDE ID DOT ID'
    pass


def p_var_declaration_1(p):
    'var_declaration : VAR var_declaration2 COLON type_specifier SEMICOLON'
    pass


def p_var_declaration_2(p):
    '''var_declaration2 : ID COMMA var_declaration2
                                    | ID
                                    | ID NUMBER COMMA var_declaration2
                                    | ID NUMBER'''
    pass


def p_type_specifier_1(p):
    'type_specifier : INTEGER'
    pass


def p_type_specifier_2(p):
    'type_specifier : REAL'
    pass


def p_type_specifier_3(p):
    'type_specifier : STRING'
    pass


def p_type_specifier_4(p):
    'type_specifier : BOOLEAN'
    pass


def p_type_specifier_5(p):
    'type_specifier : CHAR'
    pass


def p_proce_declaration_1(p):
    'proce_declaration : PROCEDURE ID APAREN params CPAREN SEMICOLON compount_stmt'
    pass


def p_proce_declaration_2(p):
    'proce_declaration : PROCEDURE ID SEMICOLON compount_stmt'
    pass


def p_params_1(p):
    'params : param_list'
    pass


def p_param_list_1(p):
    'param_list : param COLON type_specifier SEMICOLON param'
    pass


def p_param_list_2(p):
    '''param : ID   param
               |ID NUMBER param
               |ID
               |ID NUMBER
    '''
    pass


def p_compount_stmt_1(p):
    'compount_stmt : var_declarations BEGIN local_declarations statement_list END'
    pass


def p_compount_stmt_2(p):
    'compount_stmt : BEGIN local_declarations statement_list END'
    pass


def p_local_declarations_1(p):
    'local_declarations : local_declarations var_declarations'
    pass


def p_local_declarations_2(p):
    'local_declarations : empty'
    pass


def p_statement_list_1(p):
    'statement_list : statement_list statement'
    pass


def p_statement_list_2(p):
    'stantement_list : empty'
    pass


def p_statement(p):
    '''statement : expressions_stmt
                   |compount_stmt
                   |selection_stmt
                   |iterarion_stmt
    '''
    pass


def p_expression_stmt_1(p):
    'expression_stmt : expression SEMICOLON'
    pass


def p_expression_stmt_2(p):
    'expression_stmt : SEMICOLON'
    pass


def p_selection_stmt_1(p):
    'selection_stmt : IF expression THEN statement SEMICOLON'
    pass


def p_selection_stmt_2(p):
    'selection_stmt : IF expression THEN BEGIN proce_declaration SEMICOLON'
    pass


def p_selection_stmt_3(p):
    'selection_stmt : IF expression THEN BEGIN proce_declaration SEMICOLON END ELSE BEGIN'
    pass


def p_selection_stmt_4(p):
    'selection_stmt : CASE expression OF statement END SEMICOLON'
    pass


def p_iteration_stmt_1(p):
    'iteration_stmt : WHILE expression DO BEGIN statement END SEMICOLON'
    pass


def p_iteration_stmt_2(p):
    'iteration_stmt : FOR expression TO expression DO BEGIN statement END SEMICOLON'
    pass


def p_expression_1(p):
    'expression : var COLON EQUAL expression'
    pass


def p_expression_2(p):
    'expression : simple_expression'
    pass


def p_var_1(p):
    'var : ID'
    pass


def p_simple_expression_1(p):
    'simple_expression : additive_expression relop additive_expression'
    pass


def p_simple_expression_2(p):
    'simple_expression : additive_expression'
    pass


def p_relop(p):
    '''relop : MENOR
                |MENORIGUAL
                |MAYOR
                |MAYORIGUAL
                |IGUALNOT
    '''
    pass


def p_additive_expressions_1(p):
    'additive_expression : additive_expression addop term'
    pass


def p_additive_expressions_2(p):
    'additive_expression : term'
    pass


def p_addop(p):
    '''addop : SUM
              |RES
    '''
    pass


def p_term_1(p):
    'term : term mulop factor'
    pass


def p_term_2(p):
    'term : factor'
    pass


def p_mulop(p):
    ''' mulop : MULTI
               | DIVI '''
    pass


def p_factor_1(p):
    'factor : LPAREN expression RPAREN'
    pass


def p_factor_2(p):
    'factor : var'
    pass


def p_factor_3(p):
    'factor : call'
    pass


def p_factor_4(p):
    'factor : NUMBER'
    pass


def p_call(p):
    'call : ID LPAREN args RPAREN'
    pass


def p_args(p):
    '''args : args_list
                    | empty
    '''
    pass


def p_args_list_1(p):
    'args_list : args_list COMMA expression'
    pass


def p_args_list_2(p):
    'args_list : expression'
    pass


def p_empty(p):
    'empty :'
    pass


def p_error(p):
    if VERBOSE:
        if p is not None:
            print("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) +
                  " NO SE ESPERABA EL Token  " + str(p.value))
        else:
            print("ERROR SINTACTICO EN LA LINEA: " + str(cminus_lexer.lexer.lineno))
    else:
        raise Exception('syntax', 'error')


parser = yacc.yacc()

if __name__ == '__main__':

    if (len(sys.argv) > 1):
        fin = sys.argv[1]
    else:
        fin = 'evaluacion1'

    f = open(fin, 'r')
    data = f.read()
    #print (data)
    parser.parse(data, tracking=True)
    print("Amiguito, tengo el placer de informarte que Tu parser reconocio correctamente todo")
    # input()
