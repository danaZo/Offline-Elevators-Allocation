"""
OOP_ASSIGNMENT_1, Class: Elevator
ID_1: 207817529,ID_2: 206320954
In this class we create an elevator using the information we receive from the Json file of the building
"""

class Elevator:

    def __init__(self, data: dict) -> None:
        self._id = data['_id']
        self._speed = data['_speed']
        self._minFloor = data['_minFloor']
        self._maxFloor = data['_maxFloor']
        self._openTime = data['_openTime']
        self._closeTime = data['_closeTime']
        self._startTime = data['_startTime']
        self._stopTime = data['_stopTime']

