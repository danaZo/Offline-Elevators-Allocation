"""
OOP_ASSIGNMENT_1, Class: offline
ID_1: 207817529,ID_2: 206320954
In this class we read from Json file that holds info about every building and it's elevators
In addition, we read from csv file that holds all the calls for the elevators
At the end, we choose which elevators receives a given call and write it to a csv file.
"""


import os.path
import sys
import json
import csv


def read_json(file_name: str) -> dict:
    with open(file_name) as j_file:
        building_data = json.load(j_file)
    return building_data


def read_csv(file_name: str) -> list:
    calls_list = []
    with open(file_name, newline="") as calls_file:
        read_calls = csv.reader(calls_file)
        for call in read_calls:
            calls_list.append(call)
    return calls_list


def create_csv(file_name: str, calls_list: []) -> None:
    with open(file_name, 'w+', newline='') as new_calls_file:
        output = csv.writer(new_calls_file)
        output.writerows(calls_list)


Building = os.path.join('Ex1_Buildings', sys.argv[1])
Calls = os.path.join('Ex1_Calls', sys.argv[2])
Output = 'output.csv'

building = read_json(Building)
calls = read_csv(Calls)

elev_list = []  # this will be list of lists that holds the calls


def add_call_to_list(k: int, elev_id: int):
    elev_list[elev_id].append(calls[k][2])  # src floor
    elev_list[elev_id].append(calls[k][3])  # dest floor


def allocate(calls) -> None:
    """
    function allocate:
    in this function we will find the most suitable elevator for a given call.
    first o f all, we create for every elevator a list that will hold it's floors that it needs to go to.
    we run on the indexes of the calls - every index represents a call's number.
    @:param temp_total_time: temporary parameter, holds the time we calculate for every elevator,
    plus the time it will take for it to do the specific call we check.
    @:param fastest_elev: will be the elevator which it's time to make the current call will be the smallest.
    we run on the indexes of every elevator in the building, and sending it's values to a helper function
    that is calculating the total time it takes for the elevator to make all of it's calls,
    and the time it will take for it to make the current call with all of it's previous calls.
    then, if the total time of the current elevator is smaller than the value in the temporary parameter
    that keeps value of time, than the temporary value will receive the current elevator's total time.
    And so on until we finish check all the elevators in the building.
    Afterwards, we allocate the fastest elevator we found to the current call, and add this call to the
    elevator's floors list.
    after we finish doing this to all the calls, we create a new csv file with allocated elevators for
    every call.
    """
    for i in range(len(building['_elevators'])):
        curr_list = []
        elev_list.append(curr_list)
    for k in range(len(calls)):
        temp_total_time = 1000000000.0
        fastest_elev = -1
        for i in building['_elevators']:
            this_elev_id = i['_id']
            if elev_total_time(k, this_elev_id) < temp_total_time:
                temp_total_time = elev_total_time(k, this_elev_id)
                fastest_elev = this_elev_id
        calls[k][5] = fastest_elev
        add_call_to_list(k, fastest_elev)
    create_csv(Output, calls)


def elev_total_time(k: int, this_elev_id: int) -> float:
    """
    function elev_total_time:
    in this function we calculate the total time that it takes to an elevator to move through all of the floors
    it was allocated to, and the time it will take for it to complete a call that the function receives
    (the call we want to allocate an elevator to)
    :param k:is the call number
    :param this_elev_id: is the id number of the elevator
    :return:
    """
    speed_el = building['_elevators'][this_elev_id]['_speed']
    close_el = building['_elevators'][this_elev_id]['_closeTime']
    open_el = building['_elevators'][this_elev_id]['_openTime']
    start_el = building['_elevators'][this_elev_id]['_startTime']
    stop_el = building['_elevators'][this_elev_id]['_stopTime']
    curr_src_floor = float(calls[k][2])
    curr_dest_floor = float(calls[k][3])
    all_floors_speed = 0
    open_n_close = 0
    start_n_close = 0

    for index in range(len(elev_list[this_elev_id])):
        open_n_close = (open_el + close_el) * len(elev_list[this_elev_id])
        amount_of_floors = (len(elev_list[this_elev_id])-1)
        start_n_close = (start_el * amount_of_floors) + (stop_el * amount_of_floors)

        if index != 0:
            all_floors_speed = speed_el * abs(int(elev_list[this_elev_id][index]) - int(elev_list[this_elev_id][index-1]))
    total_list_time = all_floors_speed + open_n_close + start_n_close

    total_time_with_new_call = ((abs(curr_dest_floor - curr_src_floor) * speed_el) + close_el + open_el + start_el + stop_el) + total_list_time

    return total_time_with_new_call


if __name__ == '__main__':
    Calls_a = read_csv(Calls)
    allocate(Calls_a)
