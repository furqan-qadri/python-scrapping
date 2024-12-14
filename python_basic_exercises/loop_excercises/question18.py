         
def loop_pattern(number):
    for i in range(1,number+1,1):
        print("*"*i)
    for i in range(number-1,0,-1):
        print("*"*i)
    
        

loop_pattern(5)