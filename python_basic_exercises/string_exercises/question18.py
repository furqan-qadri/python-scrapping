import string


# def special_character_repalacer(given_string):
#     translator= str.maketrans("/*@&!","#####")
#     given_string=given_string.translate(translator)
#     print(given_string)

# special_character_repalacer("/*Jon is @developer & musician!!")

#using replace
given_string="/*Jon is @developer & musician!!"
for i in string.punctuation:
    given_string=given_string.replace(i,"#")
print(given_string)
    