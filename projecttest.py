import math

cities = open('cities.txt', 'r')  # This opens the cities.txt file.
cities.readline()

x = input('Will you take your holiday during Summer or Winter? ')
y = input('Would you like to go somewhere warm or cold? ')

Y = {}

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

    def lat2rad(LatDeg):
        lat2dec = int(LatDeg) + (int(LatMin) / 60)  # geographical degrees to DMS
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

    if x == 'Winter':
        if y == 'Warm':
            if LatDir == 'N' and 35 >= LatDeg:
                K = {city: distance}
                Y.update(K)
                if LatDir == 'S' and 35 >= LatDeg:  # Between 35 S and 35 N.
                    L = {city: distance}
                    Y.update(L)
            if LatDir == 'S' and 35 <= LatDeg:  # Between 35 S and 66 S.
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
