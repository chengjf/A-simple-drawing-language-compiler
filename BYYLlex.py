import ply.lex as lex

tokens=(
    'ORIGIN','SCALE','ROT','IS','TO','STEP','DRAW','FOR','FROM','T',
    'SEMICO','L_BRACKET','R_BRACKET','COMMA',
    'PLUS','MINUS','MUL','DIV','POWER',
    'COS','SIN','TAN','EXP','LN','SQRT',
    'NUMBER','PI','E',
    'NONTOKEN',
    'ERRTOKEN'
)

t_ORIGIN=r'ORIGIN'
t_SCALE=r'SCALE'
t_ROT=r'ROT'
t_IS=r'IS'
t_TO=r'TO'
t_STEP=r'STEP'
t_DRAW=r'DRAW'
t_FOR=r'FOR'
t_FROM=r'FROM'
t_T=r'T'

t_COS=r'COS'
t_SIN=r'SIN'
t_TAN=r'TAN'
t_EXP=r'EXP'
t_LN=r'LN'
t_SQRT=r'SQRT'

t_PI=r'PI'
t_E=r'E'

t_PLUS=r'\+'
t_MINUS=r'-'
t_MUL=r'\*'
t_DIV=r'/'
t_POWER=r'\*\*'


t_SEMICO=r'\;'
t_L_BRACKET=r'\('
t_R_BRACKET=r'\)'
t_COMMA=r'\,'
##t_NUMBER=r'[+-]?\d+(\.\d+)?' 
t_ignore=' '
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    try:
        t.value=float(t.value)
    except ValueError:
        print("Interger value too large %s" % t.value)
        t.value=0
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno+=t.value.count('\n')

def t_error(t):
    print "Illegal character '%s'"%t.value[0]
    t.lexer.skip(1)

lexer=lex.lex()

def startlex(file):
##    file=raw_input("Please input your file name:")
    ss=open(file,'r')
    print ('---------LEX RESULT------------')
    for s in ss:
        lexer.input(s.upper())
        while True:
            token=lexer.token()
            if not token:
                break
            
            print ("%10s,%10s,%10d,%10d") % (token.type,token.value,token.lineno,token.lexpos)


    
        


    
