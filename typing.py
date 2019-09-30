def typeit(test):
    cost = 0
    steps= []

    steps.append({"type":"INPUT","value":test[0]})
    cost+= len(test[0])

    for index in range(1, len(test)):
        copied = test[index-1]
        steps.append({"type":"COPY","value":copied})
        cost+= 1
        current = test[index]
        steps.append({"type":"TRANSFORM","value":current})
        for indexc, ch in enumerate(copied):
            if ch != current[indexc]:
                cost += 1

    return {"cost":cost, "steps":steps}


test = [ "laziest",
  "busiest",
  "easiest" ]

print("Your Output:" + str(typeit(test)))
print("Expect Output:" + str({
  "cost": 13,
  "steps": [ { "type": 'INPUT', "value": 'laziest' },
             { "type": 'COPY', "value": 'laziest' },
             { "type": 'TRANSFORM', "value": 'easiest' },
             { "type": 'COPY', "value": 'easiest' },
             { "type": 'TRANSFORM', "value": 'busiest' } ]
}))