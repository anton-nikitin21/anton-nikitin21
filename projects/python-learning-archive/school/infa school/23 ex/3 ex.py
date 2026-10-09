def f(a,b,p):
    if a==b:
        return 1
    if a>b or ('+1+1+1' in p or '*2*2*2' in p):
        return 0 
    if a<b:
        return f(a + 1,b,p +'+1') + f(a * 2,b,p +'*2')
print(f(1,14,''))
        