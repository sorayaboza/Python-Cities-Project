import math

cities = open('cities.txt', 'r')  # This opens the cities.txt file.
cities.readline()

x = input('Will you take your holiday during Summer or Winter? ')
y = input('Would you like to go somewhere warm or cold? ')

Y = {}  # This is an empty dictionary.. for now.

# Here, I'm splitting each of the rows in the file, and giving them specific values.
for row_num, line in enumerate(cities):
    values = line.strip().split('\t')
    LatDeg = int(values[0].split('°')[0])
    LonDeg = int(values[1].split("°")[0])
    LatMin = int(values[0].split("°")[1][0:2])
    LonMin = values[1].split('°')[1][0:2]
    LatDir = values[0].split('°')[1][2:3]
    LonDir = values[1].split('°')[1][2:3]

    city = values[2]
    state = values[3]
    country = values[4]

    # My functions!

    def lat2rad(LatDeg):
        lat2dec = int(LatDeg) + (int(LatMin) / 60)  # Geographical degrees to DMS
        lat2 = lat2dec * (math.pi / 180)  # and degrees to radians.
        return lat2


    def lon2rad(LonDeg):
        lon2dec = int(LonDeg) + (int(LonMin) / 60)
        lon2 = lon2dec * (math.pi / 180)
        return lon2

    # This calculates the distance between point A and point B.
    def rad2dist():
        lat2 = lat2rad(LatDeg)
        lon2 = lon2rad(LonDeg)
        lat1 = 0.65217136388511
        lon1 = 2.1066124
        d = 12720 * math.asin(math.sqrt(
            abs(math.sin((lat2 - lat1) / 2) ** 2) + math.cos(lat1) * math.cos(lat2) * math.sin((lon2 - lon1) / 2) ** 2))
        return d

    distance = rad2dist()

    # My conditions!

    if x == 'Summer':  # If the input for x is 'Summer',
        if y == 'Cold':  # and the input for y is 'Cold',
            if LatDir == 'N' and LatDeg >= 66:  # the code will look for 'N' and LatDeg of values greater than 66 in the file.
                A = {city: distance} # Then it will pull the cities and distances from those conditions and put them in a dictionary,
                Y.update(A)  # and update the 'Y' dictionary based on those results.
            if LatDir == 'S' and LatDeg >= 35:  # Between 35 S and 66 S.
                B = {city: distance}
                Y.update(B)
                if LatDeg <= 66:
                    B1 = {city: distance}
                    Y.update(B1)
            if LatDir == 'S' and LatDeg <= 35:  # Below 66 S.
                C = {city: distance}
                Y.update(C)
        if y == 'Warm':
            if LatDir == 'N' and LatDeg >= 35:  # Between 35 N and 66 N.
                D = {city: distance}
                Y.update(D)
                if LatDeg <= 66:
                    D1 = {city: distance}
                    Y.update(D1)
            if LatDir == 'N' and LatDeg <= 35:
                if LatDir == 'S' and LatDeg <= 35:  # Between 35 S and 35 N.
                    F = {city: distance}
                    Y.update(F)
    if x == 'Winter':
        if y == 'Cold':
            if LatDir == 'N' and LatDeg >= 66:  # Above 66 N.
                G = {city: distance}
                Y.update(G)
            if LatDir == 'N' and LatDeg >= 35:  # Between 35 N and 66 N.
                H = {city: distance}
                Y.update(H)
                if LatDeg <= 66:
                    H1 = {city: distance}
                    Y.update(H1)
            if LatDir == 'S' and LatDeg <= 66:  # Below 66 S.
                distance = rad2dist()
                J = {city: distance}
                Y.update(J)
        if y == 'Warm':  # the second input is "Warm",
            if LatDir == 'N' and LatDeg <= 35:  # The Lat Direction is 'N' and it's degree is greater than 35,
                K = {city: distance}
                Y.update(K)
                if LatDir == 'S' and LatDeg <= 35:  # Between 35 S and 35 N.
                    L = {city: distance}
                    Y.update(L)
            if LatDir == 'S' and LatDeg >= 35:  # Between 35 S and 66 S.
                M = {city: distance}
                Y.update(M)
                if LatDeg <= 66:
                    N = {city: distance}
                    Y.update(N)

        # For the key and value in my dictionary, where they're sorted by the updated dictionary values (Y),
        # the keys are sorted from least to greatest using the lambda function.
        # item[1] is the dictionary.
        # [0:5] makes it so I only get 5 values.
for key, value in sorted(Y.items(), key=lambda item: item[1])[0:5]:
    print('%s is %.2f km away from Merced' % (key, value))

cities.close()

