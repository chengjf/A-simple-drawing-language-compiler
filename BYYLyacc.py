import ply.yacc as yacc
##import math
from BYYLlex import tokens
##import numpy as np
##import matplotlib.pyplot as plt
##from matplotlib.ticker import MultipleLocator

##---------------globle variable-------

def func(string,num):
    for i in string:
        if type(i) is tuple:
            func(i,num+1)
        else:
            if i=='T':
                print num*'\t','\t',i
            elif type(i) is str:
                print num*'\t',i
            else:
                print num*'\t','\t',i


##--------------syntax fanction-----------------
precedence=(
            ('left','PLUS','MINUS'),
            ('left','MUL','DIV'),
            ('left','POWER'),
            ('right','UMINUS')
            )
def p_program(p):
    '''program : program statement SEMICO
               | statement SEMICO'''
##    print type(p[0])

def p_program_error(p):
    '''program : error'''
    p[0] = None
    p.parser.error = 1
##-----------------------statement-----------------------------
def p_statement_for(p):
    '''statement : FOR T FROM expression TO expression STEP expression DRAW L_BRACKET expression COMMA expression R_BRACKET'''
    p[0]=('for statement:',p[4],p[6],p[8],p[11],p[13])
    func(p[0],0)
def p_statement_origin(p):
    '''statement : ORIGIN IS L_BRACKET expression COMMA expression R_BRACKET'''
    p[0]=('origin statement:',p[4],p[6])
    func(p[0],0)
def p_statement_scale(p):
    '''statement : SCALE IS L_BRACKET expression COMMA expression R_BRACKET'''
    p[0]=('scale statement:',p[4],p[6])
    func(p[0],0)
def p_statement_rot(p):
    '''statement : ROT IS expression'''
    p[0]=('rot statement:',p[3])
    func(p[0],0)
##-----------------------expression-----------------------------
def p_expression_power(p):
    "expression : expression POWER expression"
    p[0]=(p[2],p[1],p[3])
##    print p[0]
def p_expression_sin(p):
    '''expression : SIN L_BRACKET expression R_BRACKET'''
    p[0]=(p[1],p[3])
##    print p[0]
##    p[0]=math.sin(p[3])
def p_expression_cos(p):
    '''expression : COS L_BRACKET expression R_BRACKET'''
    p[0]=(p[1],p[3])
##    print p[0]
##    p[0]=math.sin(p[3])
def p_expression_tan(p):
    '''expression : TAN L_BRACKET expression R_BRACKET'''
    p[0]=(p[1],p[3])
##    print p[0]
##    p[0]=math.tan(p[3])
def p_expression_ln(p):
    '''expression : LN L_BRACKET expression R_BRACKET'''
    p[0]=(p[1],p[3])
##    print p[0]
##    p[0]=math.log(p[3])
def p_expression_exp(p):
    '''expression : EXP L_BRACKET expression R_BRACKET'''
    p[0]=(p[1],p[3])
##    print p[0]
##    p[0]=math.exp(p[3])
def p_expression_sqrt(p):
    '''expression : SQRT L_BRACKET expression R_BRACKET'''
    p[0]=(p[1],p[3])
##    print p[0]
##    p[0]=math.sqrt(p[3])
def p_expression_pi(p):
    '''expression : PI'''
    p[0]=3.141592653
def p_expression_e(p):
    '''expression : E'''
    p[0]=2.71828
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MUL expression
                  | expression DIV expression'''
    p[0]=(p[2],p[1],p[3])
##    print p[0]
##    if p[2] == '+'  : p[0] = p[1] + p[3]
##    elif p[2] == '-': p[0] = p[1] - p[3]
##    elif p[2] == '*': p[0] = p[1] * p[3]
##    elif p[2] == '/': p[0] = p[1] / p[3]
def p_expression_uminus(p):
    "expression : MINUS expression %prec UMINUS"
    p[0]=(p[1],0,p[2])
##    print p[0]
##    p[0] = -p[2]
def p_expression_group(p):
    "expression : L_BRACKET expression R_BRACKET"
    p[0] = p[2]
def p_expression_number(p):
    "expression : NUMBER"
    p[0] = p[1]

##    print(p[2])
##    print '\t'+str(p[1])
##    print('\t'+str(p[3]))
##    p[0] = p[1]**p[3]
def p_expression_t(p):
    "expression : T"
    global T
    p[0]='T'
##    print p[0]

def p_error(p):
    if p:
        print "Syntax error %s at %d !"%(str(p.value),p.lexpos)
    else:
        print "Synatx error at EOF"



parser=yacc.yacc()

def startyacc(filename):
##    filename=raw_input("Please input your file name:\n")
    ss=open(filename,'r')
    print ('--------SYNTAX RESULT-----------')
    lineno=0
    for s in ss:
        lineno+=1
        print "----------%d line is checking----------"% lineno
##        print s
##        raw_input()
        result=parser.parse(s.upper())
        if result is None:
            print "----------%d line is checked----------\n\n\n" %lineno
        else:
            print result

##startyacc()





