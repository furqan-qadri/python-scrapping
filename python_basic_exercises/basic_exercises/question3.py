original_string="aeaeaeaeae" #11
print(f"Printing only even place characters")
length=len(original_string) 
length_is_even=(length%2==0)
for i in range(int(length/2) if length_is_even else int(length/2+1)):
    print(original_string[2*i])