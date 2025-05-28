def costCalculator(items):
    cost = 0
    items_sorted = sorted(items)
    result = []
    temp = items
    separations = []
    pile = []
    pile.append(items)
    #Division
    i=0
    while i < len(items):
        print("i:",i)
        current, extra = division(items_sorted[i], pile.pop())
        print("Current: ", current)
        print("Extra: ", extra)
        cost += min(len(current), len(extra))
        if extra != []:
            pile.append(extra)
        j=0
        while j < len(current) and current[j] == items_sorted[i]:
            i=i+1
            j=j+1
        result = current[:j]
        if extra == []:
            cost += min(len(result), len(current[j:]))
        print("Cost: ", cost)
        if j == len(current):
            separations.append(current)
        else:
            separations.append(result)
            pile.append(current[j:])
        result = []
        print("Separations: ", separations)
        print("Pile: ", pile)
    # Concatenation
    concatenation = separations[0]
    for i in range(len(separations)-1):
        concatenation = concatenation + separations[i+1]
        cost += len(concatenation)
    print("Cost: ", cost)
    
            
def division(number, items):
    i=items.index(number)
    return items[i:], items[:i]
    
items = [4,5,3,1,2]
print(costCalculator(items))
