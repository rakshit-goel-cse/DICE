import random,time,os
def p1():
     print(' \t *')
def p2():
     print('  \t **')
def p3():
     print(' \t ***')
def p4():
     print('\t **\n\t **')
def p5():
     print(' \t * *\n\t  *\n\t * *')
def p6():
     print(' \t ***\n\t ***')

def call():
     x=input('\n\npress enter to roll dice and e to exit').lower()
     if(x=='e'):
          print('BYE')
          time.sleep(1)
          sys.exit(0)
     else:
          os.system('cls')
          i=random.randint(0,5)
          t=[p1,p2,p3,p4,p5,p6]
          x=t[i]
          print('\n\nout put is:\n\n')
          x()
          call()
call()
