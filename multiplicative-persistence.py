def MultiplicativePersistence(num): 
    n = str(num)
    a = 0
    
    def mult(x):
        s = 1
        for i in range(0, len(x)):
            s *= int(x[i])
        return s
    
    while len(n) > 1:
        n = str(mult(n))
        a+=1
        
    return a
 
print MultiplicativePersistence(raw_input())
