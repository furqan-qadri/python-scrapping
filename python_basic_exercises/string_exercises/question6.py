# Exercise 6: Create a mixed String using the following rules

s1 = "Abcsdfsdfs"
s2 = "Xyzo"
s3=""
length_smaller=min(len(s1),len(s2))
length_greater=max(len(s1),len(s2))

largest_list = s2 if len(s2) > len(s1) else s1
for i in range(length_greater):
    if i>=length_smaller:
        s3=s3+largest_list[:-i]
        break
    s3=s3+(s1[i])
    s3=s3+(s2[-i-1])
    print(i)
    
print(s3)


# other approach is to reverse TODO the second list and add one element at a time to the first list and then eventually the whole of the last string will be added
    