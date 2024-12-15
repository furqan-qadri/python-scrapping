#Exercise 17: Find words with both alphabets and numbers
given_string="Emma25 is Data scientist50 and AI Expert"

word_list=given_string.split(' ')
for current_word in word_list:
    if any(char.isalpha() for char in current_word) and any(char.isdigit() for char in current_word):
      print(current_word)