
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABSOLUTE AMPERSANT AND APAREN ARRAY AS ASM BEGIN BOOLEAN BREAK CASE CHAR CLASS COLON COMENTARIOS COMMA CONST CONSTRUCTOR CONTINUE CPAREN DESTRUCTOR DIFERENTE DISPOSE DIV DIVI DO DOT DOWNTO ELSE END EQUAL ERROR_LEXICO ERROR_SINTAXIS_ABSOLUTE ERROR_SINTAXIS_AND EXCEPT EXIT EXPORTS FILE FINALIZATION FINALLY FLOAT FOR FUNCTION GOTO HASHTAG ID IF IGUAL IGUALNOT IMPLEMENTATION IN INHERITED INITIALIZATION INLINE INTEGER INTERFACE IS LABEL LBLOCK LBRAK LIBRARY MAYOR MAYORIGUAL MENOR MENORIGUAL MOD MUL NEW NIL NOT NUMBER OBJECT OF ON OPERATOR OR PACKED PROCEDURE PROGRAM PROPERTY RAISE RBLOCK RBRAK REAL RECORD REINTRODUCE REPEAT RES RETURN SELF SEMICOLON SET SHL SHR SIMBOLOS STRING SUM THEN THREADVAR TO TRY TYPE UNIT UNTIL USES VAR WHILE WITH XORprograma : declaration_listdeclaration_list : declaration_list  declarationdeclaration_list : declarationdeclaration : var_declaration\n                              | proce_declaration\n                              | cons_declaration\n                              | nom_declaration\n                              | tipo_declaration\n                              | impo_declaration\n    nom_declaration : PROGRAM ID SEMICOLONnom_declaration : PROGRAM ID NUMBER SEMICOLON\n                                   | PROGRAM NUMBER SEMICOLON\n                                   | PROGRAM NUMBER ID SEMICOLON\n    impo_declaration : USES ID SEMICOLONvar_declaration : VAR var_declaration2 COLON type_specifier SEMICOLON var_declaration2 : ID COMMA var_declaration2\n                                   | ID var_declaration2\n                                   | ID NUMBER var_declaration2\n                                   | ID\n                                   | ID NUMBER\n\n    cons_declaration : CONST cons_declaration2 COLON type_specifier SEMICOLON cons_declaration2 : ID COMMA cons_declaration2\n                                   | ID cons_declaration2\n                                   | ID NUMBER cons_declaration2\n                                   | ID\n                                   | ID NUMBER\n\n    tipo_declaration : TYPE tipo_declaration2 COLON type_specifier SEMICOLON tipo_declaration : TYPE tipo_declaration2 EQUAL RECORD SEMICOLON tipo_declaration2 : ID\n                                   | ID NUMBER\n    type_specifier : INTEGERtype_specifier : REALtype_specifier : STRINGtype_specifier : BOOLEANtype_specifier : CHARproce_declaration : PROCEDURE ID APAREN params CPAREN SEMICOLON compount_stmtproce_declaration : PROCEDURE ID SEMICOLON compount_stmtparams : param_listparam_list : param_list COLON type_specifier SEMICOLON paramparam_list : param_list COMMA paramparam_list : paramparam_list : emptyparam : ID COLON type_specifiercompount_stmt : var_declaration BEGIN local_declaration statement_list ENDcompount_stmt : BEGIN local_declaration statement_list ENDlocal_declaration : emptylocal_declaration : ID COLON EQUAL ID\n                                    | ID COLON EQUAL NUMBER\n                                    | NUMBER COLON EQUAL NUMBER\n                                    | ID NUMBER COLON EQUAL ID\n                                    | NUMBER COLON EQUAL ID\n    statement_list : statement_list statementstatement_list : emptystatement : expression_stmt\n                            | compount_stmt\n                            | selection_stmt\n                            | iteration_stmt\n                            | return_stmt\n    expression_stmt : expression SEMICOLONexpression_stmt : SEMICOLONselection_stmt : IF expression THEN statement SEMICOLONselection_stmt : IF expression THEN BEGIN proce_declaration SEMICOLONselection_stmt : IF expression THEN BEGIN proce_declaration SEMICOLON END ELSE BEGINselection_stmt : CASE expression OF statement END SEMICOLONiteration_stmt : WHILE expression DO BEGIN statement END SEMICOLONiteration_stmt : FOR expression TO expression DO BEGIN statement END SEMICOLONreturn_stmt : RETURN SEMICOLONreturn_stmt : RETURN expression SEMICOLONexpression : var COLON EQUAL expressionexpression : simple_expressionexpression : var EQUAL AMPERSANT IDvar : IDsimple_expression : additive_expression relop additive_expressionsimple_expression : additive_expressionrelop : MENOR\n                    | MENORIGUAL\n                    | MAYOR\n                    | MAYORIGUAL\n                    | IGUALNOT\n    additive_expression : additive_expression addop term\n\n    additive_expression : termaddop : SUM\n                    | RES\n    term : term mulop factorterm : factormulop : \tMUL\n                            | DIVI\n    factor : APAREN expression CPARENfactor : varfactor : callfactor : NUMBERcall : ID SEMICOLONcall : ID APAREN args CPAREN SEMICOLONargs : args_list\n                    | empty\n    args_list : args_list COMMA expressionargs_list : expressionempty :'
    
_lr_action_items = {'VAR':([0,2,3,4,5,6,7,8,9,16,32,37,39,44,58,60,64,65,68,73,74,75,78,79,80,82,85,86,87,91,93,94,95,96,97,98,99,100,102,121,122,127,146,147,149,150,151,152,155,167,169,171,177,184,185,187,189,193,194,],[10,10,-3,-4,-5,-6,-7,-8,-9,-2,10,-10,-12,-14,-37,-98,-11,-13,-15,-98,-98,-46,-21,-27,-28,10,-98,10,-53,-36,10,-45,-52,-54,-55,-56,-57,-58,-60,-44,-59,-67,-47,-48,-49,-51,10,10,-68,-50,-98,10,-61,-62,-64,10,-65,-63,-66,]),'PROCEDURE':([0,2,3,4,5,6,7,8,9,16,37,39,44,58,64,65,68,78,79,80,91,94,121,169,],[11,11,-3,-4,-5,-6,-7,-8,-9,-2,-10,-12,-14,-37,-11,-13,-15,-21,-27,-28,-36,-45,-44,11,]),'CONST':([0,2,3,4,5,6,7,8,9,16,37,39,44,58,64,65,68,78,79,80,91,94,121,],[12,12,-3,-4,-5,-6,-7,-8,-9,-2,-10,-12,-14,-37,-11,-13,-15,-21,-27,-28,-36,-45,-44,]),'PROGRAM':([0,2,3,4,5,6,7,8,9,16,37,39,44,58,64,65,68,78,79,80,91,94,121,],[13,13,-3,-4,-5,-6,-7,-8,-9,-2,-10,-12,-14,-37,-11,-13,-15,-21,-27,-28,-36,-45,-44,]),'TYPE':([0,2,3,4,5,6,7,8,9,16,37,39,44,58,64,65,68,78,79,80,91,94,121,],[14,14,-3,-4,-5,-6,-7,-8,-9,-2,-10,-12,-14,-37,-11,-13,-15,-21,-27,-28,-36,-45,-44,]),'USES':([0,2,3,4,5,6,7,8,9,16,37,39,44,58,64,65,68,78,79,80,91,94,121,],[15,15,-3,-4,-5,-6,-7,-8,-9,-2,-10,-12,-14,-37,-11,-13,-15,-21,-27,-28,-36,-45,-44,]),'$end':([1,2,3,4,5,6,7,8,9,16,37,39,44,58,64,65,68,78,79,80,91,94,121,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-2,-10,-12,-14,-37,-11,-13,-15,-21,-27,-28,-36,-45,-44,]),'ID':([10,11,12,13,14,15,18,21,23,28,30,31,34,36,60,72,73,74,75,85,86,87,92,93,94,95,96,97,98,99,100,102,103,104,105,106,107,114,117,119,121,122,127,132,133,134,135,136,137,138,139,140,141,142,143,144,146,147,148,149,150,151,152,154,155,156,157,167,169,171,176,177,184,185,187,189,193,194,],[18,19,21,22,25,26,18,21,40,18,18,53,21,21,76,53,76,-98,-46,-98,110,-53,53,110,-45,-52,-54,-55,-56,-57,-58,-60,110,110,110,110,110,110,146,150,-44,-59,-67,110,110,110,-75,-76,-77,-78,-79,-82,-83,110,-86,-87,-47,-48,167,-49,-51,110,110,110,-68,110,174,-50,76,110,110,-61,-62,-64,110,-65,-63,-66,]),'NUMBER':([13,18,21,22,25,60,73,74,75,76,85,86,87,93,94,95,96,97,98,99,100,102,103,104,105,106,107,114,117,119,121,122,127,132,133,134,135,136,137,138,139,140,141,142,143,144,146,147,149,150,151,152,154,155,156,167,169,171,176,177,184,185,187,189,193,194,],[23,30,36,38,43,77,77,-98,-46,89,-98,116,-53,116,-45,-52,-54,-55,-56,-57,-58,-60,116,116,116,116,116,116,147,149,-44,-59,-67,116,116,116,-75,-76,-77,-78,-79,-82,-83,116,-86,-87,-47,-48,-49,-51,116,116,116,-68,116,-50,77,116,116,-61,-62,-64,116,-65,-63,-66,]),'COLON':([17,18,20,21,24,25,29,30,31,35,36,43,46,47,48,49,50,51,52,53,55,56,57,62,63,76,77,81,84,89,108,110,120,],[27,-19,33,-25,41,-29,-17,-20,-98,-23,-26,-30,-31,-32,-33,-34,-35,-16,-18,69,71,-41,-42,-22,-24,88,90,-43,-40,118,129,-72,-39,]),'COMMA':([18,21,31,46,47,48,49,50,55,56,57,81,84,108,109,110,111,112,113,115,116,120,131,159,161,162,163,164,165,166,173,174,182,183,],[28,34,-98,-31,-32,-33,-34,-35,72,-41,-42,-43,-40,-89,-70,-72,-74,-81,-85,-90,-91,-39,-92,176,-97,-73,-89,-80,-84,-88,-69,-71,-93,-96,]),'APAREN':([19,60,73,74,75,85,86,87,93,94,95,96,97,98,99,100,102,103,104,105,106,107,110,114,121,122,127,132,133,134,135,136,137,138,139,140,141,142,143,144,146,147,149,150,151,152,154,155,156,167,169,171,176,177,184,185,187,189,193,194,],[31,-98,-98,-98,-46,-98,114,-53,114,-45,-52,-54,-55,-56,-57,-58,-60,114,114,114,114,114,132,114,-44,-59,-67,114,114,114,-75,-76,-77,-78,-79,-82,-83,114,-86,-87,-47,-48,-49,-51,114,114,114,-68,114,-50,-98,114,114,-61,-62,-64,114,-65,-63,-66,]),'SEMICOLON':([19,22,23,26,38,40,45,46,47,48,49,50,58,60,61,66,67,70,73,74,75,83,85,86,87,91,93,94,95,96,97,98,99,100,101,102,107,108,109,110,111,112,113,115,116,121,122,127,128,131,146,147,149,150,151,152,155,162,163,164,165,166,167,168,169,171,173,174,175,177,178,179,182,184,185,186,187,189,192,193,194,],[32,37,39,44,64,65,68,-31,-32,-33,-34,-35,-37,-98,78,79,80,82,-98,-98,-46,92,-98,102,-53,-36,102,-45,-52,-54,-55,-56,-57,-58,122,-60,127,-89,-70,131,-74,-81,-85,-90,-91,-44,-59,-67,155,-92,-47,-48,-49,-51,102,102,-68,-73,-89,-80,-84,-88,-50,177,-98,102,-69,-71,182,-61,184,185,-93,-62,-64,189,102,-65,194,-63,-66,]),'EQUAL':([24,25,43,88,90,108,110,118,129,],[42,-29,-30,117,119,130,-72,148,156,]),'INTEGER':([27,33,41,69,71,],[46,46,46,46,46,]),'REAL':([27,33,41,69,71,],[47,47,47,47,47,]),'STRING':([27,33,41,69,71,],[48,48,48,48,48,]),'BOOLEAN':([27,33,41,69,71,],[49,49,49,49,49,]),'CHAR':([27,33,41,69,71,],[50,50,50,50,50,]),'CPAREN':([31,46,47,48,49,50,54,55,56,57,81,84,108,109,110,111,112,113,115,116,120,131,132,145,158,159,160,161,162,163,164,165,166,173,174,182,183,],[-98,-31,-32,-33,-34,-35,70,-38,-41,-42,-43,-40,-89,-70,-72,-74,-81,-85,-90,-91,-39,-92,-98,166,175,-94,-95,-97,-73,-89,-80,-84,-88,-69,-71,-93,-96,]),'BEGIN':([32,59,60,68,73,74,75,82,85,86,87,93,94,95,96,97,98,99,100,102,121,122,127,146,147,149,150,151,152,153,155,167,169,171,177,181,184,185,187,189,191,193,194,],[60,73,-98,-15,-98,-98,-46,60,-98,60,-53,60,-45,-52,-54,-55,-56,-57,-58,-60,-44,-59,-67,-47,-48,-49,-51,169,60,171,-68,-50,-98,60,-61,187,-62,-64,60,-65,193,-63,-66,]),'RECORD':([42,],[67,]),'END':([60,73,74,75,85,86,87,93,94,95,96,97,98,99,100,102,121,122,127,146,147,149,150,155,167,169,170,177,180,184,185,189,190,193,194,],[-98,-98,-98,-46,-98,94,-53,121,-45,-52,-54,-55,-56,-57,-58,-60,-44,-59,-67,-47,-48,-49,-51,-68,-50,-98,179,-61,186,188,-64,-65,192,-63,-66,]),'IF':([60,73,74,75,85,86,87,93,94,95,96,97,98,99,100,102,121,122,127,146,147,149,150,151,152,155,167,169,171,177,184,185,187,189,193,194,],[-98,-98,-98,-46,-98,103,-53,103,-45,-52,-54,-55,-56,-57,-58,-60,-44,-59,-67,-47,-48,-49,-51,103,103,-68,-50,-98,103,-61,-62,-64,103,-65,-63,-66,]),'CASE':([60,73,74,75,85,86,87,93,94,95,96,97,98,99,100,102,121,122,127,146,147,149,150,151,152,155,167,169,171,177,184,185,187,189,193,194,],[-98,-98,-98,-46,-98,104,-53,104,-45,-52,-54,-55,-56,-57,-58,-60,-44,-59,-67,-47,-48,-49,-51,104,104,-68,-50,-98,104,-61,-62,-64,104,-65,-63,-66,]),'WHILE':([60,73,74,75,85,86,87,93,94,95,96,97,98,99,100,102,121,122,127,146,147,149,150,151,152,155,167,169,171,177,184,185,187,189,193,194,],[-98,-98,-98,-46,-98,105,-53,105,-45,-52,-54,-55,-56,-57,-58,-60,-44,-59,-67,-47,-48,-49,-51,105,105,-68,-50,-98,105,-61,-62,-64,105,-65,-63,-66,]),'FOR':([60,73,74,75,85,86,87,93,94,95,96,97,98,99,100,102,121,122,127,146,147,149,150,151,152,155,167,169,171,177,184,185,187,189,193,194,],[-98,-98,-98,-46,-98,106,-53,106,-45,-52,-54,-55,-56,-57,-58,-60,-44,-59,-67,-47,-48,-49,-51,106,106,-68,-50,-98,106,-61,-62,-64,106,-65,-63,-66,]),'RETURN':([60,73,74,75,85,86,87,93,94,95,96,97,98,99,100,102,121,122,127,146,147,149,150,151,152,155,167,169,171,177,184,185,187,189,193,194,],[-98,-98,-98,-46,-98,107,-53,107,-45,-52,-54,-55,-56,-57,-58,-60,-44,-59,-67,-47,-48,-49,-51,107,107,-68,-50,-98,107,-61,-62,-64,107,-65,-63,-66,]),'MUL':([108,110,112,113,115,116,131,163,164,165,166,182,],[-89,-72,143,-85,-90,-91,-92,-89,143,-84,-88,-93,]),'DIVI':([108,110,112,113,115,116,131,163,164,165,166,182,],[-89,-72,144,-85,-90,-91,-92,-89,144,-84,-88,-93,]),'MENOR':([108,110,111,112,113,115,116,131,163,164,165,166,182,],[-89,-72,135,-81,-85,-90,-91,-92,-89,-80,-84,-88,-93,]),'MENORIGUAL':([108,110,111,112,113,115,116,131,163,164,165,166,182,],[-89,-72,136,-81,-85,-90,-91,-92,-89,-80,-84,-88,-93,]),'MAYOR':([108,110,111,112,113,115,116,131,163,164,165,166,182,],[-89,-72,137,-81,-85,-90,-91,-92,-89,-80,-84,-88,-93,]),'MAYORIGUAL':([108,110,111,112,113,115,116,131,163,164,165,166,182,],[-89,-72,138,-81,-85,-90,-91,-92,-89,-80,-84,-88,-93,]),'IGUALNOT':([108,110,111,112,113,115,116,131,163,164,165,166,182,],[-89,-72,139,-81,-85,-90,-91,-92,-89,-80,-84,-88,-93,]),'SUM':([108,110,111,112,113,115,116,131,162,163,164,165,166,182,],[-89,-72,140,-81,-85,-90,-91,-92,140,-89,-80,-84,-88,-93,]),'RES':([108,110,111,112,113,115,116,131,162,163,164,165,166,182,],[-89,-72,141,-81,-85,-90,-91,-92,141,-89,-80,-84,-88,-93,]),'THEN':([108,109,110,111,112,113,115,116,123,131,162,163,164,165,166,173,174,182,],[-89,-70,-72,-74,-81,-85,-90,-91,151,-92,-73,-89,-80,-84,-88,-69,-71,-93,]),'OF':([108,109,110,111,112,113,115,116,124,131,162,163,164,165,166,173,174,182,],[-89,-70,-72,-74,-81,-85,-90,-91,152,-92,-73,-89,-80,-84,-88,-69,-71,-93,]),'DO':([108,109,110,111,112,113,115,116,125,131,162,163,164,165,166,172,173,174,182,],[-89,-70,-72,-74,-81,-85,-90,-91,153,-92,-73,-89,-80,-84,-88,181,-69,-71,-93,]),'TO':([108,109,110,111,112,113,115,116,126,131,162,163,164,165,166,173,174,182,],[-89,-70,-72,-74,-81,-85,-90,-91,154,-92,-73,-89,-80,-84,-88,-69,-71,-93,]),'AMPERSANT':([130,],[157,]),'ELSE':([188,],[191,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'declaration_list':([0,],[2,]),'declaration':([0,2,],[3,16,]),'var_declaration':([0,2,32,82,86,93,151,152,171,187,],[4,4,59,59,59,59,59,59,59,59,]),'proce_declaration':([0,2,169,],[5,5,178,]),'cons_declaration':([0,2,],[6,6,]),'nom_declaration':([0,2,],[7,7,]),'tipo_declaration':([0,2,],[8,8,]),'impo_declaration':([0,2,],[9,9,]),'var_declaration2':([10,18,28,30,],[17,29,51,52,]),'cons_declaration2':([12,21,34,36,],[20,35,62,63,]),'tipo_declaration2':([14,],[24,]),'type_specifier':([27,33,41,69,71,],[45,61,66,81,83,]),'params':([31,],[54,]),'param_list':([31,],[55,]),'param':([31,72,92,],[56,84,120,]),'empty':([31,60,73,74,85,132,169,],[57,75,75,87,87,160,75,]),'compount_stmt':([32,82,86,93,151,152,171,187,],[58,91,97,97,97,97,97,97,]),'local_declaration':([60,73,169,],[74,85,74,]),'statement_list':([74,85,],[86,93,]),'statement':([86,93,151,152,171,187,],[95,95,168,170,180,190,]),'expression_stmt':([86,93,151,152,171,187,],[96,96,96,96,96,96,]),'selection_stmt':([86,93,151,152,171,187,],[98,98,98,98,98,98,]),'iteration_stmt':([86,93,151,152,171,187,],[99,99,99,99,99,99,]),'return_stmt':([86,93,151,152,171,187,],[100,100,100,100,100,100,]),'expression':([86,93,103,104,105,106,107,114,132,151,152,154,156,171,176,187,],[101,101,123,124,125,126,128,145,161,101,101,172,173,101,183,101,]),'var':([86,93,103,104,105,106,107,114,132,133,134,142,151,152,154,156,171,176,187,],[108,108,108,108,108,108,108,108,108,163,163,163,108,108,108,108,108,108,108,]),'simple_expression':([86,93,103,104,105,106,107,114,132,151,152,154,156,171,176,187,],[109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,]),'additive_expression':([86,93,103,104,105,106,107,114,132,133,151,152,154,156,171,176,187,],[111,111,111,111,111,111,111,111,111,162,111,111,111,111,111,111,111,]),'term':([86,93,103,104,105,106,107,114,132,133,134,151,152,154,156,171,176,187,],[112,112,112,112,112,112,112,112,112,112,164,112,112,112,112,112,112,112,]),'factor':([86,93,103,104,105,106,107,114,132,133,134,142,151,152,154,156,171,176,187,],[113,113,113,113,113,113,113,113,113,113,113,165,113,113,113,113,113,113,113,]),'call':([86,93,103,104,105,106,107,114,132,133,134,142,151,152,154,156,171,176,187,],[115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,]),'relop':([111,],[133,]),'addop':([111,162,],[134,134,]),'mulop':([112,164,],[142,142,]),'args':([132,],[158,]),'args_list':([132,],[159,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> declaration_list','programa',1,'p_programa','minipascal_parserV2.py',10),
  ('declaration_list -> declaration_list declaration','declaration_list',2,'p_declaration_list_1','minipascal_parserV2.py',15),
  ('declaration_list -> declaration','declaration_list',1,'p_declaration_list_2','minipascal_parserV2.py',20),
  ('declaration -> var_declaration','declaration',1,'p_declaration','minipascal_parserV2.py',25),
  ('declaration -> proce_declaration','declaration',1,'p_declaration','minipascal_parserV2.py',26),
  ('declaration -> cons_declaration','declaration',1,'p_declaration','minipascal_parserV2.py',27),
  ('declaration -> nom_declaration','declaration',1,'p_declaration','minipascal_parserV2.py',28),
  ('declaration -> tipo_declaration','declaration',1,'p_declaration','minipascal_parserV2.py',29),
  ('declaration -> impo_declaration','declaration',1,'p_declaration','minipascal_parserV2.py',30),
  ('nom_declaration -> PROGRAM ID SEMICOLON','nom_declaration',3,'p_nom_declaration_1','minipascal_parserV2.py',36),
  ('nom_declaration -> PROGRAM ID NUMBER SEMICOLON','nom_declaration',4,'p_nom_declaration_2','minipascal_parserV2.py',41),
  ('nom_declaration -> PROGRAM NUMBER SEMICOLON','nom_declaration',3,'p_nom_declaration_2','minipascal_parserV2.py',42),
  ('nom_declaration -> PROGRAM NUMBER ID SEMICOLON','nom_declaration',4,'p_nom_declaration_2','minipascal_parserV2.py',43),
  ('impo_declaration -> USES ID SEMICOLON','impo_declaration',3,'p_impo_declaration','minipascal_parserV2.py',49),
  ('var_declaration -> VAR var_declaration2 COLON type_specifier SEMICOLON','var_declaration',5,'p_var_declaration_1','minipascal_parserV2.py',53),
  ('var_declaration2 -> ID COMMA var_declaration2','var_declaration2',3,'p_var_declaration_2','minipascal_parserV2.py',58),
  ('var_declaration2 -> ID var_declaration2','var_declaration2',2,'p_var_declaration_2','minipascal_parserV2.py',59),
  ('var_declaration2 -> ID NUMBER var_declaration2','var_declaration2',3,'p_var_declaration_2','minipascal_parserV2.py',60),
  ('var_declaration2 -> ID','var_declaration2',1,'p_var_declaration_2','minipascal_parserV2.py',61),
  ('var_declaration2 -> ID NUMBER','var_declaration2',2,'p_var_declaration_2','minipascal_parserV2.py',62),
  ('cons_declaration -> CONST cons_declaration2 COLON type_specifier SEMICOLON','cons_declaration',5,'p_cons_declaration_1','minipascal_parserV2.py',69),
  ('cons_declaration2 -> ID COMMA cons_declaration2','cons_declaration2',3,'p_cons_declaration_2','minipascal_parserV2.py',74),
  ('cons_declaration2 -> ID cons_declaration2','cons_declaration2',2,'p_cons_declaration_2','minipascal_parserV2.py',75),
  ('cons_declaration2 -> ID NUMBER cons_declaration2','cons_declaration2',3,'p_cons_declaration_2','minipascal_parserV2.py',76),
  ('cons_declaration2 -> ID','cons_declaration2',1,'p_cons_declaration_2','minipascal_parserV2.py',77),
  ('cons_declaration2 -> ID NUMBER','cons_declaration2',2,'p_cons_declaration_2','minipascal_parserV2.py',78),
  ('tipo_declaration -> TYPE tipo_declaration2 COLON type_specifier SEMICOLON','tipo_declaration',5,'p_tipo_declaration_1','minipascal_parserV2.py',85),
  ('tipo_declaration -> TYPE tipo_declaration2 EQUAL RECORD SEMICOLON','tipo_declaration',5,'p_tipo_declaration_2','minipascal_parserV2.py',90),
  ('tipo_declaration2 -> ID','tipo_declaration2',1,'p_cons_declaration_3','minipascal_parserV2.py',95),
  ('tipo_declaration2 -> ID NUMBER','tipo_declaration2',2,'p_cons_declaration_3','minipascal_parserV2.py',96),
  ('type_specifier -> INTEGER','type_specifier',1,'p_type_specifier_1','minipascal_parserV2.py',102),
  ('type_specifier -> REAL','type_specifier',1,'p_type_specifier_2','minipascal_parserV2.py',107),
  ('type_specifier -> STRING','type_specifier',1,'p_type_specifier_3','minipascal_parserV2.py',112),
  ('type_specifier -> BOOLEAN','type_specifier',1,'p_type_specifier_4','minipascal_parserV2.py',117),
  ('type_specifier -> CHAR','type_specifier',1,'p_type_specifier_5','minipascal_parserV2.py',122),
  ('proce_declaration -> PROCEDURE ID APAREN params CPAREN SEMICOLON compount_stmt','proce_declaration',7,'p_proce_declaration_1','minipascal_parserV2.py',127),
  ('proce_declaration -> PROCEDURE ID SEMICOLON compount_stmt','proce_declaration',4,'p_proce_declaration_2','minipascal_parserV2.py',132),
  ('params -> param_list','params',1,'p_params_1','minipascal_parserV2.py',137),
  ('param_list -> param_list COLON type_specifier SEMICOLON param','param_list',5,'p_param_list_1','minipascal_parserV2.py',142),
  ('param_list -> param_list COMMA param','param_list',3,'p_param_list_2','minipascal_parserV2.py',147),
  ('param_list -> param','param_list',1,'p_param_list_3','minipascal_parserV2.py',152),
  ('param_list -> empty','param_list',1,'p_param_list_4','minipascal_parserV2.py',157),
  ('param -> ID COLON type_specifier','param',3,'p_param_1','minipascal_parserV2.py',162),
  ('compount_stmt -> var_declaration BEGIN local_declaration statement_list END','compount_stmt',5,'p_compount_stmt_1','minipascal_parserV2.py',167),
  ('compount_stmt -> BEGIN local_declaration statement_list END','compount_stmt',4,'p_compount_stmt_2','minipascal_parserV2.py',172),
  ('local_declaration -> empty','local_declaration',1,'p_local_declarations_1','minipascal_parserV2.py',177),
  ('local_declaration -> ID COLON EQUAL ID','local_declaration',4,'p_local_declarations_2','minipascal_parserV2.py',182),
  ('local_declaration -> ID COLON EQUAL NUMBER','local_declaration',4,'p_local_declarations_2','minipascal_parserV2.py',183),
  ('local_declaration -> NUMBER COLON EQUAL NUMBER','local_declaration',4,'p_local_declarations_2','minipascal_parserV2.py',184),
  ('local_declaration -> ID NUMBER COLON EQUAL ID','local_declaration',5,'p_local_declarations_2','minipascal_parserV2.py',185),
  ('local_declaration -> NUMBER COLON EQUAL ID','local_declaration',4,'p_local_declarations_2','minipascal_parserV2.py',186),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list_1','minipascal_parserV2.py',192),
  ('statement_list -> empty','statement_list',1,'p_statement_list_2','minipascal_parserV2.py',197),
  ('statement -> expression_stmt','statement',1,'p_statement','minipascal_parserV2.py',202),
  ('statement -> compount_stmt','statement',1,'p_statement','minipascal_parserV2.py',203),
  ('statement -> selection_stmt','statement',1,'p_statement','minipascal_parserV2.py',204),
  ('statement -> iteration_stmt','statement',1,'p_statement','minipascal_parserV2.py',205),
  ('statement -> return_stmt','statement',1,'p_statement','minipascal_parserV2.py',206),
  ('expression_stmt -> expression SEMICOLON','expression_stmt',2,'p_expression_stmt_1','minipascal_parserV2.py',212),
  ('expression_stmt -> SEMICOLON','expression_stmt',1,'p_expression_stmt_2','minipascal_parserV2.py',217),
  ('selection_stmt -> IF expression THEN statement SEMICOLON','selection_stmt',5,'p_selection_stmt_1','minipascal_parserV2.py',222),
  ('selection_stmt -> IF expression THEN BEGIN proce_declaration SEMICOLON','selection_stmt',6,'p_selection_stmt_2','minipascal_parserV2.py',227),
  ('selection_stmt -> IF expression THEN BEGIN proce_declaration SEMICOLON END ELSE BEGIN','selection_stmt',9,'p_selection_stmt_3','minipascal_parserV2.py',232),
  ('selection_stmt -> CASE expression OF statement END SEMICOLON','selection_stmt',6,'p_selection_stmt_4','minipascal_parserV2.py',237),
  ('iteration_stmt -> WHILE expression DO BEGIN statement END SEMICOLON','iteration_stmt',7,'p_iteration_stmt_1','minipascal_parserV2.py',242),
  ('iteration_stmt -> FOR expression TO expression DO BEGIN statement END SEMICOLON','iteration_stmt',9,'p_iteration_stmt_2','minipascal_parserV2.py',247),
  ('return_stmt -> RETURN SEMICOLON','return_stmt',2,'p_return_stmt_1','minipascal_parserV2.py',252),
  ('return_stmt -> RETURN expression SEMICOLON','return_stmt',3,'p_return_stmt_2','minipascal_parserV2.py',257),
  ('expression -> var COLON EQUAL expression','expression',4,'p_expression_1','minipascal_parserV2.py',262),
  ('expression -> simple_expression','expression',1,'p_expression_2','minipascal_parserV2.py',267),
  ('expression -> var EQUAL AMPERSANT ID','expression',4,'p_expression_3','minipascal_parserV2.py',272),
  ('var -> ID','var',1,'p_var_1','minipascal_parserV2.py',277),
  ('simple_expression -> additive_expression relop additive_expression','simple_expression',3,'p_simple_expression_1','minipascal_parserV2.py',282),
  ('simple_expression -> additive_expression','simple_expression',1,'p_simple_expression_2','minipascal_parserV2.py',287),
  ('relop -> MENOR','relop',1,'p_relop','minipascal_parserV2.py',292),
  ('relop -> MENORIGUAL','relop',1,'p_relop','minipascal_parserV2.py',293),
  ('relop -> MAYOR','relop',1,'p_relop','minipascal_parserV2.py',294),
  ('relop -> MAYORIGUAL','relop',1,'p_relop','minipascal_parserV2.py',295),
  ('relop -> IGUALNOT','relop',1,'p_relop','minipascal_parserV2.py',296),
  ('additive_expression -> additive_expression addop term','additive_expression',3,'p_additive_expression_1','minipascal_parserV2.py',302),
  ('additive_expression -> term','additive_expression',1,'p_additive_expression_2','minipascal_parserV2.py',309),
  ('addop -> SUM','addop',1,'p_addop','minipascal_parserV2.py',314),
  ('addop -> RES','addop',1,'p_addop','minipascal_parserV2.py',315),
  ('term -> term mulop factor','term',3,'p_term_1','minipascal_parserV2.py',321),
  ('term -> factor','term',1,'p_term_2','minipascal_parserV2.py',326),
  ('mulop -> MUL','mulop',1,'p_mulop','minipascal_parserV2.py',331),
  ('mulop -> DIVI','mulop',1,'p_mulop','minipascal_parserV2.py',332),
  ('factor -> APAREN expression CPAREN','factor',3,'p_factor_1','minipascal_parserV2.py',338),
  ('factor -> var','factor',1,'p_factor_2','minipascal_parserV2.py',343),
  ('factor -> call','factor',1,'p_factor_3','minipascal_parserV2.py',348),
  ('factor -> NUMBER','factor',1,'p_factor_4','minipascal_parserV2.py',353),
  ('call -> ID SEMICOLON','call',2,'p_call_1','minipascal_parserV2.py',358),
  ('call -> ID APAREN args CPAREN SEMICOLON','call',5,'p_call_2','minipascal_parserV2.py',363),
  ('args -> args_list','args',1,'p_args','minipascal_parserV2.py',368),
  ('args -> empty','args',1,'p_args','minipascal_parserV2.py',369),
  ('args_list -> args_list COMMA expression','args_list',3,'p_args_list_1','minipascal_parserV2.py',375),
  ('args_list -> expression','args_list',1,'p_args_list_2','minipascal_parserV2.py',380),
  ('empty -> <empty>','empty',0,'p_empty','minipascal_parserV2.py',385),
]
