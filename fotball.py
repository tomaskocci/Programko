"""""Fotball"""
def prepare_count(words, index):
    """""Def for count"""
    counter={}
    for word in words:
        char= word[index]
        if char in counter.keys():
            counter[char] +=1
        else:
            counter[char] = 1
    return counter    

def true_or_false():
    firstCounter = prepare_count(["osel", "lok", "oko", "olusk", "nos", "kolo", "koks", "slon", "olovo"], -1)
    lastCounter = prepare_count(["osel", "lok", "oko", "olusk", "nos", "kolo", "koks", "slon", "olovo"], 0)
    #firstCounter = prepare_count(["ahoj","jo","ok"], -1)
    #lastCounter = prepare_count(["ahoj","jo","ok"], 0)
    inter = set(firstCounter.keys()).intersection(set(lastCounter.keys()))

    for i in inter:
        value = firstCounter[i]
        firstCounter[i] -= value
        value2 = lastCounter[i]
        lastCounter[i] -= value2
        if firstCounter[i] == 0:
            del firstCounter[i]
        if lastCounter[i] == 0:
            del lastCounter[i]

    if len(firstCounter.values()) == 1 and len(lastCounter.values()) == 1:
        return True
    else:
        return False

result = true_or_false()
print(result)






    
    