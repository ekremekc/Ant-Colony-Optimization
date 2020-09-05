# Ant-Colony-Optimization
This repository includes Travelling Salesman problem implementation of Ant Colony Optimization.

Implemented code can be executed by using **aco.py** file. This file uses distance **matrix from aco_distances.xlsx** and creates pheromone matrix. Then by using probability analysis, the next city is selected by using quite popular **roulette wheel** method based on the updated pheromone matrix for each city. At the end of the each iteration, best ant route is saved and displayed as a plot.

### Distance Matrix

|            | Muğla | Bursa | Ankara | Gaziantep | Diyarbakır | Hatay | Adıyaman | Kocaeli | İstanbul | Eskişehir |
|------------|-------|-------|--------|-----------|------------|-------|----------|---------|----------|-----------|
| Muğla      | 0     | 543   | 619    | 1058      | 1371       | 1037  | 1181     | 671     | 782      | 499       |
| Bursa      | 543   | 0     | 385    | 1026      | 1272       | 1033  | 1114     | 132     | 243      | 152       |
| Ankara     | 619   | 385   | 0      | 655       | 901        | 683   | 742      | 342     | 453      | 233       |
| Gaziantep  | 1058  | 1026  | 655    | 0         | 313        | 193   | 150      | 1000    | 1111     | 874       |
| Diyarbakır | 1371  | 1272  | 901    | 313       | 0          | 506   | 207      | 1246    | 1357     | 1121      |
| Hatay      | 1037  | 1033  | 683    | 193       | 506        | 0     | 316      | 1028    | 1139     | 881       |
| Adıyaman   | 1181  | 1114  | 742    | 150       | 207        | 316   | 0        | 1087    | 1198     | 962       |
| Kocaeli    | 671   | 132   | 342    | 1000      | 1246       | 1028  | 1087     | 0       | 111      | 214       |
| İstanbul   | 782   | 243   | 453    | 1111      | 1357       | 1139  | 1198     | 111     | 0        | 325       |
| Eskişehir  | 499   | 152   | 233    | 874       | 1121       | 881   | 962      | 214     | 325      | 0         |

![aco](https://user-images.githubusercontent.com/65715006/92313913-0637b300-efc9-11ea-81e4-67a50e9ee397.png)
<img src="https://user-images.githubusercontent.com/65715006/92313913-0637b300-efc9-11ea-81e4-67a50e9ee397.png" align="center" height="750" width="750"/>

## Building Animation

Implemented algorithm utilized and optimized the best tour among the 10 cities of Turkey. To build an animation turtle graphic package has been used. The GPS coordinates of each cities are pulled from **coordinates.xlsx** excel file by using **anim.py** Python script.

### GPS Coordinates of Relevant Cities
| Cities     | N       | E       |
|------------|---------|---------|
| Mugla      | 37.2154 | 28.3634 |
| Eskisehir  | 39.7667 | 30.5256 |
| Istanbul   | 41.0082 | 28.9784 |
| Bursa      | 40.1885 | 29.061  |
| Gaziantep  | 37.066  | 37.3781 |
| Hatay      | 36.4018 | 36.3498 |
| Ankara     | 39.9334 | 32.8597 |
| Diyarbakir | 37.925  | 40.211  |
| Kocaeli    | 40.7654 | 29.9408 |
| Adiyaman   | 37.7636 | 38.2773 |
