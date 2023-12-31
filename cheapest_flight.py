#!/usr/bin/env python3

"""Learning Python

Task from Checkio.org - The Cheapest Flight
Version extended - all flights in result
"""

def cheapest_flight(costs: list, a: str, b: str) -> int:
    """Find flights between two points"""

    # Each connection gets unique ID
    for i, cost in enumerate(costs):
        cost.append(2**i)

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
fsc = [["A", "C", 100], ["A", "B", 20], ["B", "C", 50], ["A", "D", 200],
       ["D", "C", 10],["G", "C", 30], ["A", "E", 22], ["E", "F", 82],
       ["F", "G", 35], ["F", "G", 90  ], ["D", "G", 15]]

print("Examples:")
flights = cheapest_flight(fsc, "A", "D")

print("\nAvailable flights:")
for _ in flights[0]:
    print(_)

print("\nConnections:")
for _ in flights[1]:
    print(_)

print(f"\nCheapest connection: {flights[1][0][0]} coins ;-)")
