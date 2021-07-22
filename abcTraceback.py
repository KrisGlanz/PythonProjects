def a():
    print('Start of a()')
    b() #call b().

def b():
    print('Start of b()')
    c() # call c().

def c():
    print('Start of c()')
    42/0 # cause divide by zero error

a() #call a().
