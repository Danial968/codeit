def player(biggest, total):
    my_list = list(range(1,biggest+1))
    # my_list = [i for i in range(1, max+1)]

    player_2 = 1

    # total -= 1
    print(total)
    total -= max(my_list) - 1
    print(total)

    # print(max(my_list))


player(10, 15)