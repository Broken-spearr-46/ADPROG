# Justine Reinn Sanidad
# I101

# for Loop and while loop


# for loop
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# while loop
count = 1
while count <= 6:
    print(f"Count is :{count}")
    count += 2


# numeric
x = 0
while x < 10:
    print(x)
    x += 2

# Boolean
flag = True
while flag:
    print("Running")
    flag = False


# using in for iteration
for char in "Hello":
    print(char)

  
# using range() for iteration
for num in range(1,6):
    print(num)


## else in for loop and while loop
for i in range (3):
    print(i)
    
else:
    print("Loop completed successfully!")
##while loop    
x = 3
while x > 0:
    print(x)
    x -= 1
else:
    print("countdown finished")

#infinite loop
while True:
    print("This is an infinite loop!")

## controlling loop

for num in range(1, 10):
    if num == 5:
        break
    print(num)

for num in range(1, 6):
    if num == 3:
        print(num)
        continue
