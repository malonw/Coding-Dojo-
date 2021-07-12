import random
def randInt(min= 0 , max= 100 ):
    if min < max :
        num = random.random() * max
        return num
    elif max < 0 :
        print("Try again max is < 0")
        return False
    else :
        print("Try Again min is > Max!")
        return False
print(randInt(min=int(input("Input min #")), max= int(input("Input Max #"))))
#print(randInt()) 		    # should print a random integer between 0 to 100
#print(randInt(max=50)) 	    # should print a random integer between 0 to 50
#print(randInt(min=50)) 	    # should print a random integer between 50 to 100
#print(randInt(min=50, max=500))    # should print a random integer between 50 and 500
