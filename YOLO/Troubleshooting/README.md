
# QT Freezing

- When the webcam and detection were implemented in a single node and the service on/off function was also used together, the system got stuck and the webcam stopped working.
- I tried to solve this problem using **MultiThreadedExecutor**, but it made the situation worse.  
  Because webcam streaming and YOLO inference are both CPU-intensive tasks, running multiple callbacks in parallel caused resource contention and blocked the communication between nodes.
- To solve this issue, I separated the system into three nodes: **webcam**, **YOLO detection**, and **result processing**.  
  After separating the nodes, the pipeline worked properly without freezing.

![result](../images/QT_freeze.png)


# Data imbalance
- data supplement
<img width="809" height="238" alt="image" src="https://github.com/user-attachments/assets/6a9efce0-dd7b-46af-8ef6-7fa904143d38" />

# Misclassification
- fist and five can be classified well, but the other classes have a quite high misclassification rate by taking as neighboring finger number  like 3,5 if it is 4
<img width="2400" height="1200" alt="results" src="https://github.com/user-attachments/assets/b8c80624-f823-4d27-bfa5-c6d6b68b0509" />
<img width="3000" height="2250" alt="confusion_matrix_normalized" src="https://github.com/user-attachments/assets/9284f599-8a7c-42ee-b10d-923dea2d746e" />
