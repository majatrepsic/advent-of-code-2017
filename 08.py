'bla'
code = 'a=0 \n\
b=0 \n\
if a > 1: \n\
    b += 5 \n\
if b < 5: \n\
    a += 1 \n\
print max(a,b)'

exec(code)