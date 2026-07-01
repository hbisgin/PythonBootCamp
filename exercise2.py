name = input("Your name please: ") #this is a string
test1 = input("What is your first test score? ") 

test1 = float(test1) #this is still correct

test2 = float(input("What is your second test score? "))

average = (test1 + test2)/2 #this is a float

print(name, ", your average test score is: ", average)
print(name + ", your average test score is: " + str(average)) #this is a string

