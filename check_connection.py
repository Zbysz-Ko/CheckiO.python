#!/usr/bin/env python3

""" Learning Python
    Task from Checkio.org - Check Connection
"""


def check_connection(network, first, second):
    """ Check if First drone is connected to Second one
        through other drones in network """

    first, network = {first}, [i.split("-") for i in network]

    def make_friends(drone, net=network.copy(), change=False):
        """ Find all friends for First drone """
        for i in net.copy():
            if i[0] in drone or i[1] in drone:
                drone.update(set(i))
                net.remove(i)
                change=True
        return make_friends(drone, net) if change else drone

    return second in make_friends(first)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
