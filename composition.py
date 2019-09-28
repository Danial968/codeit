def compo(dict):
    compo = dict['composition']
    ban = dict['patterns']

    long_ban = []
    count = 0
    for ch in ban:
        long_ban.append(ch)
        long_ban.append(ch[1] + ch[0])

    for banned in long_ban:

        if banned in compo:
            count+=1
            compo = compo.replace(banned,'')
    
    result = {"testId":dict['setId'],"result":count}
    print(result)
my_str = 'abcdef'

# print(my_str.translate({ord('ab')}:None))
compo({"setId": '1', "compositionLength":5, "composition": "abcdeab", 'noOfCase':3, "patterns":['ac','ab','de']})