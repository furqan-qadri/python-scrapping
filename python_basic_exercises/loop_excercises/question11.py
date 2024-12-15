def prime_range():
    for i in range(25,50):
        for j in range(12,1,-1):
         if i%j==0:
             break
        else:  #this else will reach only when no break
         print(i)
         
             
prime_range()

