import string
str1 = "/*Jon is @developer & musician"
translator=str.maketrans('','',string.punctuation)
str1=str1.translate(translator)
print(str1)
