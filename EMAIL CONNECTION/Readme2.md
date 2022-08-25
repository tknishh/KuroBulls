# Finding the relevancy between A and B:

![image](https://user-images.githubusercontent.com/74897823/186653297-e44535ce-b4b6-4ed0-b444-f39dfc0e5808.png)

* ```SR Ratio = recieved/sent```
* ```RS Ratio = sent/recieved```
* ```Sum = SR Ratio + RS Ratio```
* ```Relevancy Score = ((0.7*Recieved + 0.3*Sent)/Sum)```
* ```Norm_Rev = (xi - min(x) / (max(x) - min(x) )```
where x is the set of Relevancy Score

#### Results: 
![image](https://user-images.githubusercontent.com/74897823/186653448-92077409-82d9-4f55-933b-d6b1c4b41e7d.png)


# Finding Relevancy between users which are not in the same circle

![image](https://user-images.githubusercontent.com/74897823/186653579-619e0dd8-fb5d-4d28-a50f-9c9f55807a14.png)

* ```Let the number of nodes = i```
* ```Longest path from A to C: A-B-D-F-E-C```
* ```Total Length / Rev_Total = Rev_Ab + Rev_Bd + Rev_Df + Rev_Fe + Rev_Ec```
* ```Maximum Length = 1 * (i-1) ```
#### Formula to check if the email id spoofed or authentic:

* ``` If Rev_Total > 60% * (Maximum Length)``` then it is authentic
* ``` If Rev_Total <= 60% * (Maximum Length)``` then the email is spoofed.

To support the formula and how the percantages are taken we did hypothesis testing on the relevancy score.
