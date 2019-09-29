def bank(test):

    counter = 0
    timing = 0
    bank = test['branch_officers_timings']
    my_dict = {}
    
    

    for i in range(len(bank)):
        if i + 1 not in my_dict:
            my_dict[i+1] = [bank[i],1]
            counter += 1

    

    print(my_dict)



bank({"N":6,"branch_officers_timings":[2,3]})