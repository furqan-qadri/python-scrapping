import random

number=101
while number%5!=0:
    number=random.randrange(100,999)
# print(number)

# lottery question
lottery_list=[]
for i in range(100):
    number=random.randrange(1000000000,9999999999)
    lottery_list.append(number)
winners_list=list(random.sample(lottery_list, k=2))
print(lottery_list)

print(winners_list)
for winner in winners_list:
        print (lottery_list.index(winner))