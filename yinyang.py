def yinyang(test):
    number_of_elements = test["number_of_elements"]
    number_of_operations = test["number_of_operations"]
    elements = test["elements"]
    elements_list = [elements]
    probability = 0

    for i in range(number_of_operations):
        count_yin = 0
        count_yang = 0
        for element in elements_list:
            for n in range(len(element)):
                if element[n] == "Y" or element[-n-1] == "Y":
                    count_yang += 1
                else:
                    count_yin += 1
            probability += (count_yang/len(element))/(len(elements_list))
            # if count_yin > 0:
            #     elements_list.append([])
    return probability

test = {
    "number_of_elements" : 3,
    "number_of_operations" : 1,
    "elements" :  "yYY"
}

print(yinyang(test))