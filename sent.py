def receive(test):
    num = len(test)
    my_list = ['positive','negative']
    response = []
    for i in range(num):
        response.append(rand(my_list))
    my_dict['response'] = response
    return jsonify(my_dict)


test = [1,2]
receive[test]