def f(x):
    for i in range(x):
        yield i

print (list((f(5))*2))
        
