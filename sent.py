import random
def receive(test):
    num = len(test)
    my_list = ['positive','negative']
    response = []
    my_dict = {}
    for i in range(num):
        response.append(random.choice(my_list))
    my_dict['response'] = response
    return (my_dict)


test = [1,2]
print(receive(test))