#approach 1: number->string->list->reverse->join with space
#approach 2: mathematical place value

def int_reverser(integer):
    int_list=(list(str(integer)))
    int_list.reverse()  #in place reversal
    result=' '.join(int_list) 
    print(result)

#place value no conversions
#popular way in python to reverse a number. extract the last digit from the end and keep printing it

def reverse_number(number):
    while number>0:
        digit=number%10
        number=number//10
        print(digit, end=" ")
 
int_reverser(12345)
reverse_number(12345)