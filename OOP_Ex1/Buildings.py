"""
OOP_ASSIGNMENT_1, Class: Building
ID_1: 207817529,ID_2: 206320954
In this class we create a building using Json format
we load from Json files and create the object building
"""
import json

from Elevator import Elevator


class Building(object):

    def __init__(self, data: dict, file_name=None) -> None:
        self._minFloor = data['_minFloor']
        self._maxFloor = data['_maxFloor']
        self._elevators = []
        for elev in data['_elevators']:
            elevators = Elevator(elev)
            self._elevators.append(elevators)
