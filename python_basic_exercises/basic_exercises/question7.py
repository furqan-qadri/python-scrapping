import string
def count_a_substring(given_string,given_substring):
    translator= str.maketrans('','',string.punctuation)
    given_string=given_string.translate(translator).lower()
    given_list=given_string.split(" ")    
    count=0
    for word in given_list:
        if word==given_substring.lower():
            count+=1
    print(f"{given_substring} appeared {count} times")
    
    
count_a_substring("Emma is a good developer. Emma is a writer as well. A lot of people like working with Emma.","Emma")

