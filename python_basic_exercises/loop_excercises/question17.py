# Write a program to calculate the sum of series up to n terms. For example, if n = 5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690

#make the particular and add to the sum and then return

def series_sum(number,terms):
    str_array=[]
    for i in range(1,terms+1,1):
        initial_str=str(f"{number}"*i)
        str_array.append(initial_str)
    int_array= [int(n) for n in str_array]  #kind of map
    print(sum(int_array))
    
series_sum(2,5)

#using a generator
# def series_sum(number, terms):
#     total_sum = sum(int(str(number) * i) for i in range(1, terms + 1))
#     print(total_sum)

square_series=(x**2 for x in range(5))
for i in square_series:
    print(i)

    