import random

def userId():
    for i in range (1,300):
        randNum = random.randint(1,300)
        Gmail = "201B"+ str(randNum) + "@juetguna.in"
        return(Gmail)

def toUserId():
    for i in range (1,300):
        rNum = random.randint(1,300)
        mail = "201B" + str(rNum) + "@jueguna.in"
        return(mail)

def toRecieved():
    for i in range(1,300):
	    y = random.randrange(40)
	    return(y)
    
def toSent():
    for i in range(1,300):
        y = random.randrange(40)
        return(y)

for i in range (1,300):
    lst = [userId(),toUserId(),toRecieved(),toSent()]
    print(lst)