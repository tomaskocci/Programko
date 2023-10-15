def alg(a, b, c):
    slovnik = {}  
    all_collections = [a, b, c] 

    for collection in all_collections:
        for num in collection:
            key = num[0]
            value = num[1]

            if key in slovnik:
                slovnik[key].append(value)  
            else:
                slovnik[key] = [value]  

    
    
    return slovnik
a = [(1, 2), (4, 3), (5, 1)]
b = [(1, 3), (2, 4), (5, 2)]
c = [(2, 5), (4, 1), (10, 1)]

result = alg(a, b, c)
print(result)
