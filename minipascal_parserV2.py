import ply.yacc as yacc
from minipascal_lexer import tokens
import minipascal_lexer
import sys

VERBOSE = 1


def p_programa(p):
    'programa : declaration_list'
    pass


def p_declaration_list_1(p):
    'declaration_list : declaration_list  declaration'
    pass


def p_declaration_list_2(p):
    'declaration_list : declaration'
    pass


def p_declaration(p):
    '''declaration : var_declaration
                              | proce_declaration
                              | cons_declaration
                              | nom_declaration
                              | tipo_declaration
                              | impo_declaration
    '''
    pass


def p_nom_declaration_1(p):
    'nom_declaration : PROGRAM ID SEMICOLON'
    pass


def p_nom_declaration_2(p):
    '''nom_declaration : PROGRAM ID NUMBER SEMICOLON
                                   | PROGRAM NUMBER SEMICOLON
                                   | PROGRAM NUMBER ID SEMICOLON
    '''
    pass


def p_impo_declaration(p):
    'impo_declaration : USES ID SEMICOLON'


def p_var_declaration_1(p):
    'var_declaration : VAR var_declaration2 COLON type_specifier SEMICOLON '
    pass


def p_var_declaration_2(p):
    '''var_declaration2 : ID COMMA var_declaration2
                                   | ID var_declaration2
                                   | ID NUMBER var_declaration2
                                   | ID
                                   | ID NUMBER

    '''
    pass


def p_cons_declaration_1(p):
    'cons_declaration : CONST cons_declaration2 COLON type_specifier SEMICOLON '
    pass


def p_cons_declaration_2(p):
    '''cons_declaration2 : ID COMMA cons_declaration2
                                   | ID cons_declaration2
                                   | ID NUMBER cons_declaration2
                                   | ID
                                   | ID NUMBER

    '''
    pass


def p_tipo_declaration_1(p):
    'tipo_declaration : TYPE tipo_declaration2 COLON type_specifier SEMICOLON '
    pass


def p_tipo_declaration_2(p):
    'tipo_declaration : TYPE tipo_declaration2 EQUAL RECORD SEMICOLON '
    pass


def p_cons_declaration_3(p):
    '''tipo_declaration2 : ID
                                   | ID NUMBER
    '''
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
    'param_list : param_list COLON type_specifier SEMICOLON param'
    pass


def p_param_list_2(p):
    'param_list : param_list COMMA param'
    pass


def p_param_list_3(p):
    'param_list : param'
    pass


def p_param_list_4(p):
    'param_list : empty'
    pass


def p_param_1(p):
    'param : ID COLON type_specifier'
    pass


def p_compount_stmt_1(p):
    'compount_stmt : var_declaration BEGIN local_declaration statement_list END'
    pass


def p_compount_stmt_2(p):
    'compount_stmt : BEGIN local_declaration statement_list END'
    pass


def p_local_declarations_1(p):
    'local_declaration : empty'
    pass


def p_local_declarations_2(p):
    '''local_declaration : ID COLON EQUAL ID
                                    | ID COLON EQUAL NUMBER
                                    | NUMBER COLON EQUAL NUMBER
                                    | ID NUMBER COLON EQUAL ID
                                    | NUMBER COLON EQUAL ID
    '''
    pass


def p_statement_list_1(p):
    'statement_list : statement_list statement'
    pass


def p_statement_list_2(p):
    'statement_list : empty'
    pass


def p_statement(p):
    '''statement : expression_stmt
                            | compount_stmt
                            | selection_stmt
                            | iteration_stmt
                            | return_stmt
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


def p_return_stmt_1(p):
    'return_stmt : RETURN SEMICOLON'
    pass


def p_return_stmt_2(p):
    'return_stmt : RETURN expression SEMICOLON'
    pass


def p_expression_1(p):
    'expression : var COLON EQUAL expression'
    pass


def p_expression_2(p):
    'expression : simple_expression'
    pass


def p_expression_3(p):
    'expression : var EQUAL AMPERSANT ID'
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
                    | MENORIGUAL
                    | MAYOR
                    | MAYORIGUAL
                    | IGUALNOT
    '''
    pass


def p_additive_expression_1(p):
    '''additive_expression : additive_expression addop term

    '''
    pass


def p_additive_expression_2(p):
    'additive_expression : term'
    pass


def p_addop(p):
    '''addop : SUM
                    | RES
    '''
    pass


def p_term_1(p):
    'term : term mulop factor'
    pass


def p_term_2(p):
    'term : factor'
    pass


def p_mulop(p):
    '''mulop : 	MUL
                            | DIVI
    '''
    pass


def p_factor_1(p):
    'factor : APAREN expression CPAREN'
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


def p_call_1(p):
    'call : ID SEMICOLON'
    pass


def p_call_2(p):
    'call : ID APAREN args CPAREN SEMICOLON'
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
        fin = 'evaluacion3'

    f = open(fin, 'r')
    data = f.read()
    #print (data)
    parser.parse(data, tracking=True)
    print("Compilado Correctamente")
    # input()
