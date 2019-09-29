def secret(tests):

    my_list = []

    for test in tests:
        n = test["n"]
        text = test["text"]
        new_text = ""
        for i in range(len(text)):
            if text[i].isalpha():
                new_text += text[i].upper()
        if len(new_text) < n:
            my_list.append(new_text)
            break

        current_list = ['']*len(new_text)
        count = 0
        rounds = 1

        for i in range(len(new_text)):
            current_list[count] = new_text[i]
            count += n
            if count > len(new_text):
                count = rounds
                rounds += 1
        
        my_list.append("".join(current_list))
    
    return my_list

test = [
    {
        "n": 3,
        "text": "This is a sample message."
    },
    {
        "n": 10,
        "text": "Too short"
    }
]
print(secret(test))