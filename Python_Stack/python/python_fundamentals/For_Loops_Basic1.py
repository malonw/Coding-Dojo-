# 1. Basic Print all integers from 0 to 150.
for x in range(150):
    print(x)
    
# 2. multiples of 5.
print("-----")
for y in range(5, 1000, 5):
    print(y)

print('-----')

# 3. Counting the Dojo way
for z in range(100):
    if (z % 5 == 0) :
        print("Coding")
    elif (z % 10 == 0 ) :
        print("Coding Dojo")
print('-----')       
# 4. Whoa Thast sucker's Huge
for x in range(500001) :
    if(x % 2 !=0) :
        y += x
print(y)

print('-----') 
# 5. Countdown by Fours
for z in range(2018, 0, -4) :
    print(z)    
print('-----') 
# 6. Flexible Counter
lowNum = 0
highNum = 50
multi= 5
for z in range(lowNum, highNum, multi) :
    if (z % multi ==0) :
        print(z)
    