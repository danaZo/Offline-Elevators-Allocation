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

elev_list = [] # this will be list of lists that holds the calls


def add_call_to_list(k: int, elev_id: int):
    elev_list[elev_id].append(calls[k][2])  # src floor
    elev_list[elev_id].append(calls[k][3])  # dest floor


def allocate(calls) -> None:

    for i in range(len(building['_elevators'])):
        currList = []
        elev_list.append(currList)
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


# param k is the call number
# param this_elev_id is the id number of the elevator


def elev_total_time(k: int, this_elev_id: int) -> float:
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
        amountOfFloors = (len(elev_list[this_elev_id])-1)
        start_n_close = (start_el * amountOfFloors) + (stop_el * amountOfFloors)

        if index != 0:
            all_floors_speed = speed_el * abs(int(elev_list[this_elev_id][index]) - int(elev_list[this_elev_id][index-1]))
    total_list_time = all_floors_speed + open_n_close + start_n_close

    total_time_with_new_call = ((abs(curr_dest_floor - curr_src_floor) * speed_el) + close_el + open_el + start_el + stop_el) + total_list_time

    return total_time_with_new_call


if __name__ == '__main__':
   Calls_a = read_csv(Calls)
   allocate(Calls_a)
   #add_call_to_list(calls[0], 0)
   #print(elev_list)



