#!/usr/bin/env python3

# Learning Python
#
# Task from Checkio.org - The Cheapest Flight
# Version extended - all flights in result

def cheapest_flight(costs: list, a: str, b: str) -> int:
    
    # Each connection gets unique ID
    for i in range(len(costs)):
        costs[i].append(2 ** i)
    
    # Looking for all connection between to cities
    def flight(costs: list, a: str, b: str, visited: list) -> list:   
        price = []
        for i in costs:
            if (i[0] in visited) or (i[1] in visited):
                continue
            if (i[0] == a and i[1] == b) or (i[0] == b and i[1] == a):
                price.append([i[2], i[0]+"<>"+i[1], i[3]])
            else:
                if i[0] == a:
                    temp = flight(costs, b, i[1], visited+[a])
                    x = a +"<>"+ i[1]
                elif i[1] == a:
                    temp = flight(costs, b, i[0], visited+[a])
                    x = a +"<>"+ i[0]
                elif i[0] == b:
                    temp = flight(costs, a, i[1], visited+[b])
                    x = b +"<>"+ i[1]
                elif i[1] == b:
                    temp = flight(costs, a, i[0], visited+[b])
                    x = b +"<>"+ i[0]
                else:
                    continue
                for j in temp:
                    if len(j[1]) > 0:
                        price.append([i[2]+j[0], j[1]+" + "+x, i[3]+j[2]])
                
        if len(price) > 0:
            price.sort()
            return price
        else:
            return [[0, ""]]
    price = flight(costs, a, b, [])

    temp = []
    result = []
    for i in price:
        if i[2] not in temp:
            temp.append(i[2])
            result.append(i)
     

    return [costs, result]

# Initial table with connections and costs
fsc = [["A", "C", 100], ["A", "B", 20], ["B", "C", 50], ["A", "D", 200], ["D", "C", 10],["G", "C", 30], ["A", "E", 22], ["E", "F", 82], ["F", "G", 35], ["F", "G", 90  ], ["D", "G", 15]]

print("Examples:")
result = cheapest_flight(fsc, "A", "D")

print("\nAvailable flights:")
for i in result[0]:
    print(i)

print("\nConnections:")
for i in result[1]:
    print(i)

print("\nCheapest connection: {} coins ;-)".format(result[1][0][0]))
