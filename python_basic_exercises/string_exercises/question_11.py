# Exercise 11: Reverse a given string
str1 = "PYnative"


# negative slicing
rev_str=str1[::-1]
print(rev_str)

# reversed string

# rev_arr=str1.reversed()
rev_arr=''.join(reversed(str1))
print(rev_arr)


# using for loop and appending from the end of original
rev=""
for i in range(1,len(str1)+1,1):
    rev=rev+str1[-i]
print (rev)

# splitting into array, reversing that and then joining it
word_array=[]
for i in str1:
    word_array.append(i)
word_array.reverse()
final=''.join(word_array)
print(final)
    
    

