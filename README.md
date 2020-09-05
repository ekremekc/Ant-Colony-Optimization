# Ant-Colony-Optimization
This repository includes Travelling Salesman problem implementation of Ant Colony Optimization.

Implemented code can be executed by using **aco.py** file. This file uses distance **matrix from aco_distances.xlsx** and creates pheromone matrix. Then by using probability analysis, the next city is selected by using quite popular **roulette wheel** method based on the updated pheromone matrix for each city. At the end of the each iteration, best ant route is saved and displayed as a plot.

![aco](https://user-images.githubusercontent.com/65715006/92313913-0637b300-efc9-11ea-81e4-67a50e9ee397.png)

## Building Animation

Implemented algorithm utilized and optimized the best tour among the 10 cities of Turkey. To build an animation turtle graphic package has been used. The GPS coordinates of each cities are pulled from **coordinates.xlsx** excel file by using **anim.py** Python script.
