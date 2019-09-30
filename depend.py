def depend(test):
    final = []
    dependency = {}
    stack = set({})
    moduleSet = set(test["modules"])

    for item in test["dependencyPairs"]:
        if item["dependee"] in dependency:
            dependency[item["dependee"]] += [item["dependentOn"]]
        else:
            dependency[item["dependee"]] = [item["dependentOn"]]
        stack.add(item["dependee"])

    # add with no dependentOn
    for item in moduleSet.difference(stack):
        final += [item]
    for item in final:
        moduleSet.remove(item)

    #fff
    prevCount = len(moduleSet)
    currentCount = -1
    
    while currentCount!= prevCount:
        prevCount = len(moduleSet)
        nextF = []
        for item in moduleSet:
            dependsOn = dependency[item]
            if all(elem in final  for elem in dependsOn):
                nextF += [item]
        final += nextF 
        for item in nextF:
            moduleSet.remove(item)
        currentCount = len(moduleSet)
    
    return final




test = {
    "modules": ["m1","m27","m18","m31"],
    "dependencyPairs": [
                           {"dependee":"m1","dependentOn":"m18"},
                           {"dependee":"m27","dependentOn":"m18"},
                           {"dependee":"m31","dependentOn":"m1"},
                           {"dependee":"m31","dependentOn":"m27"}
                          ]
}

test2 = {
    "modules": ["m1","m27","m18","m31"],
    "dependencyPairs": [
                           {"dependee":"m1","dependentOn":"m27"},
                           {"dependee":"m27","dependentOn":"m18"},
                           {"dependee":"m18","dependentOn":"m1"}
                          ]
}

print("Your Output:" + str(depend(test)))
print("Expect Output:" + str(["m18","m1","m27","m31"]))

print()

print("Your Output:" + str(depend(test2)))
print("Expect Output:" + str(["m31"]))



############3
@app.route('/generateSequence', methods = ["POST"])
def depend():
    test = request.json
    final = []
    dependency = {}
    stack = set({})
    moduleSet = set(test["modules"])

    for item in test["dependencyPairs"]:
        if item["dependee"] in dependency:
            dependency[item["dependee"]] += [item["dependentOn"]]
        else:
            dependency[item["dependee"]] = [item["dependentOn"]]
        stack.add(item["dependee"])

    # add with no dependentOn
    for item in moduleSet.difference(stack):
        final += [item]
    for item in final:
        moduleSet.remove(item)

    #fff
    prevCount = len(moduleSet)
    currentCount = -1
    
    while currentCount!= prevCount:
        prevCount = len(moduleSet)
        nextF = []
        for item in moduleSet:
            dependsOn = dependency[item]
            if all(elem in final  for elem in dependsOn):
                nextF += [item]
        final += nextF 
        for item in nextF:
            moduleSet.remove(item)
        currentCount = len(moduleSet)
    
    return final