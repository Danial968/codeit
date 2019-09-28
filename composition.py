def composition(test):

    patterns = test["patterns"]
    my_dic = {}
    for pattern in patterns:
        for ch in pattern:
            if ch not in my_dic:
                my_dic[ch] = 1
            else:
                my_dic[ch] += 1
    
    
test = {
  "setId" : "1",
  "compositionLength" : 5,
  "composition" : "abcde",
  "noOfCase" : 3,
  "patterns":[
    "ac",
    "ab",
    "de"
  ]
}

print(composition(test))