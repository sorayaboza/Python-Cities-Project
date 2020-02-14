def range(distance):
    largest = distance[0]
    largest2 = None
    lowest2 = None
    lowest = list1[0]
    for item in distance[1:]:
        if item > largest:
            largest2 = largest
            largest = item
        elif largest2 == None or largest2 < item:
            largest2 = item
        if item < lowest:
            lowest2 = lowest
            lowest = item
        elif lowest2 == None or lowest2 > item:
            lowest2 = item
    print(largest)
    print(largest2)
    print(lowest2)
    print(lowest)


################

sorted(list_name, key=lambda item: item[0])