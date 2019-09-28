def contest(input):
    
    comparator = {}

    for words in input:
        for new_word in input:
            counter = 0
            for i in range(len(new_word)):
                if new_word[i] != words[i]:
                    counter += 1
                    key = new_word + ':'+words
                    if key not in comparator:
                        comparator[key] = counter
                    else:
                        comparator[key]+=1

    my_str = input[0]
    counter = len(input[0])

    actions = ['INPUT']
    word_list = [input[0]]
    
    while(len(word_list) != len(input)):
        to_change = None
        if actions[-1] == 'INPUT':
            actions.append('COPY')
            

        elif actions[-1] == "COPY":
            counter += 1
            actions.append('TRANSFORM')


        else:
            change = 1000000000
            for word in input:
                if word!=my_str:
                    key = my_str +':'+ word
                    if comparator[key] < change:
                        to_change = word
                        change = comparator[key]
            counter += change
            word_list.append(to_change)
            actions.append('COPY')
            

    print(counter)


contest(['laziest','busiest','easiest'])