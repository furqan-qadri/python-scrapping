#check if a given number is palindrome
#checking first with last and then moving from there
def is_number_palindrome(number):
    string_number=str(number)
    for i in range(int(len((string_number))/2)):
        if(string_number[i]==string_number[-1-i]):
            continue
        else:
            return "NOT a Palindrome"
    return "Number IS A Palindrome"
        
print(is_number_palindrome(3331333))