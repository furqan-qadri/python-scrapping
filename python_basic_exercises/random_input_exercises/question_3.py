# # generating a secure 6 digit OTP
import secrets
import random
import string
# secretsGenerator=secrets.SystemRandom()

# for i in range(100):
#     number=secretsGenerator.randrange(100000,999999)
#     if (number==123456) or (number==234567):
#         print(True)
        
# #picking a random char from string

# string1="hello how are you"
# random_char=print(random.choice(string1))
# letters=string.ascii_letters
# print(letters)


# Exercise 6: Generate a random Password which meets the following conditions

# Password length must be 10 characters long.
# It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.

letters=string.ascii_letters

two_letters=''.join(random.choice(letters) for i in range(2))
seven_digits=random.randrange(1000000,9999999)

special_characters="!@#$%"
one_special=random.choice(special_characters)
print(str(seven_digits)+two_letters+one_special)