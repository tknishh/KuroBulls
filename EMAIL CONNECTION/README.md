# PROBLEM 
Spoofing an email is pretending to be a legitimate sender, such as an online retailer or website owner. The victim's email address is used by cybercriminals to attempt to access their personal data. They can get the victim's name, address, credit card information, social security number, passwords, and other personal information.

## Let's take an example of a real-life situation to understand the problem better.

Let’s say the head of the finance department sends frequent mails to his employee for making some transactions. An email spoofing attack can easily happen here. The attacker can target the head of the department and can send a spoofed mail to any of the employee asking to make transactions to any of his personal account. 

An attack here can be very dangerous for the organization and thus we present a solution for the same.

# USING EMAIL CONNECTION TO DETECT A SPOOFING ATTACK

1. Using the concept of email connections we came out with a solution to detect spoofing attacks that happen intra-organization.

2. If two users are sending emails to each other they are being marked with a relevancy score which checks how much relevant or legitimate emails a user can send to another user.

3. We are using the concept of longest path to determine the relevancy of impersonating a person intra-organization and performing a spoofing attack.

### Working of the longest path concept:
![image](https://user-images.githubusercontent.com/74897823/186481985-2bf10a0f-dae5-4c53-af42-ac486975be3e.png)

Assuming we have this graph, the longest path from the starting node "A" to the ending node "C" will be  ```A --> B --> D --> E --> F --> C```.

We have marked the length between the nodes with the relevancy score.

If there are i nodes then the maximum length from any starting to ending node will be ``` 1 x(i-1) ``` 

The total length from A to C will be the simmation of all the relevancy scores between A and C through longest path traversal.

Now, if ```Rev_total > 0.6``` then email is ```not spoofed```.
if ```Rev_total <= 0.6``` then the email will be marked as ```potential spoofed email```.

To check the how the 0.6 probablity comes here check the hypothessis testing excel file.

### What we need
A cypher query that searches the longest path and returns the summation of the relevancy score between them.
