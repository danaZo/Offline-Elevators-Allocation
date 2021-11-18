# __Readme__
#### Object oriented programming assignment 1.
#### Wrriten by Dikla Birman - 206329054 and Dana Zorohov - 207817529.
#### In this assigment we built an offline algorithm which allocates the most suitable elevator for a given call.

## literature review :
#### The hidden science of Elevators : https://www.popularmechanics.com/technology/infrastructure/a20986/the-hidden-science-of-elevators/
#### Elevator puzzle : https://www.i-programmer.info/programmer-puzzles/203-sharpen-your-coding-skills/4561-sharpen-your-coding-skills-elevator-puzzle.html?start=1
#### Elevator scheduling : http://www.columbia.edu/~cs2035/courses/ieor4405.S13/p14.pdf

## Offline algorithm for elevators:
#### we want to save all the sorce floors and destination floors of every given call in a list for every elevator, so we can calculate which is the optimal one for the current call.
#### we will make a list of elevators for every building(every building has it own numbers of elevators) , in every index of the list which represent elevator ID, we will build another list which holds all of this elevator stop floors ( src and dest of every call).
#### for every 'next call' we will go through the list of every elevator and calculate the total time that will take every elevator to complete all of its calls included the new one we got. then, we can compare between all of the elevators which is the fastest, and add the new call to this optimal chosen elevator list.
#### Part of the assigment is to read CSV and JSON files and work with them. we will build classes for the objects in these files. At the end of the assigment we want to export the results as a new CSV output file.
#### in our main function (named allocate) we will find the most suitable elevator for a given call. first of all, we create for every elevator a list that will hold it's floors that it needs to go to. we run on the indexes of the calls - every index represents a call's number. we run on the indexes of every elevator in the building, and sending it's values to a helper function that is calculating the total time it takes for the elevator to make all of it's calls, and the time it will take for it to make the current call with all of it's previous calls.then, if the total time of the current elevator is smaller than the value in the temporary parameter that keeps value of time, than the temporary value will receive the current elevator's total time. And so on until we finish check all the elevators in the building. Afterwards, we allocate the fastest elevator we found to the current call, and add this call to the elevator's floors list. after we finish doing this to all the calls, we create a new csv file with allocated elevators for every call.

#### in our helper function we calculate the total time that it takes to an elevator to move through all of the floors it was allocated to, and the time it will take for it to complete a call that the function receives (the call we want to allocate an elevator to). we will consider also star time, stop time, open doors time, close door time and the speed of every elevator.


## *_Here are our cases results_*:
![cases](https://user-images.githubusercontent.com/80482676/142428378-aaa09fe8-3601-46ad-9b98-a0cb74fe9013.jpeg)



## *_UML_* :

![UML](https://user-images.githubusercontent.com/80482676/142420336-f88a08cc-3774-49e3-a0a8-13f1d658b1f4.jpg)
