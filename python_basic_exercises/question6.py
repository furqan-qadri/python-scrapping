def display_nums_divisble_by_5(given_list):
    for num in given_list:
        if num%5==0:
            print (num)
    # with range loop
    # for x in range(len(given_list)):
    #     if (given_list[x]%5==0):
    #         print(given_list[x])
    return 0


display_nums_divisble_by_5([10, 20, 33, 46, 55])