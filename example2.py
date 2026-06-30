weight1 = 50
weight2 = 70
weight3 = 90

average = (weight1+weight2+weight3)/3

print("Welcome to average calculator")

print("The average of these values is: ", average)

#literal strings are strings that are written directly in the code, like "Hello, World!" or 'Python is great!'. They are enclosed in either double quotes or single quotes.

firstName = "John"

print("Welcome", firstName) #instead of typing print("Welcome John"), I can use a variable to store the name and then print it. This way, if I want to change the name, I only have to change it in one place, instead of changing it in multiple places.

#string concatenation is the process of combining two or more strings together. In Python, you can concatenate strings using the + operator.

print("Welcome " + firstName) # I deliberately put a space after "Welcome" so that when it is concatenated with firstName, there is a space between the two words. If I didn't put a space, it would print "WelcomeJohn" without a space.

print("I love" + "Python" + "believe or not") #this will print "I lovePythonbelieve or not" because there is no space between the words. If I want spaces, I need to add them explicitly.

print("I love", "Python" , "believe or not")

print("I love " + "Python " + "believe or not")

#We are going to introduce str function. str() function is used to convert a number to a string. This is useful when you want to concatenate a string and a number.

#print("The average of these values is: " + average) #can't I use + operator to concatenate a string and a number? No, you can't. You can only concatenate strings with other strings. If you want to concatenate a string and a number, you need to convert the number to a string first using the str() function.

print("The average of these values is: " + str(average)) # This plus sign is not a math operation. It is a string concatenation operator. It is used to concatenate strings together. It is not used to add numbers together. If you want to add numbers together, you need to use the + operator with numbers, not strings.

####################################################################

#input function is used to get input from the user. It is a built-in function in Python. It takes a string as an argument, which is the prompt that will be displayed to the user. It returns the input from the user as a string.

firstName = input("What is your name? ") #firstName is a string.
print("Welcome to my program dear " + firstName)

myweight = input("What is your weight? ") #myweight is a string. 
print("Your weight is: " + myweight)

###ask for the height
###print the height on the screen
height = input("What is your height? ") #height is a string.
print("Your height is: " + height) #height is a string. 

byear = input("What is birth year? ") #age is a string.
print("Your age is: " + byear) #age is a string.

#We can convert a number to a string and a string to a number. 
#use str from number to string
#use int() or floa() from string to number 

myweight_float = float(myweight) #myweight_float is a float. 
height_float = float(height) #height_float is a float.

bmi = float(myweight)/float(height)**2 #bmi is a float. It is a decimal number. It is a real number. It is a number that can have a decimal point.

bmi  = myweight_float / height_float**2 #John John/Mary? John**2

#tell John by using his name what his BMI is.
print("Dear ", firstName, ", your BMI is: ", bmi) #bmi is a float. 

print("Dear " + firstName + ", your BMI is: " + str(bmi)) #bmi is a float. We need to convert it to a string to concatenate it with other strings.

#age = 2026-byear #don't forget that byear is a string. We need to convert it to an integer to do the subtraction.

byear_int = int(byear) #byear_int is an integer. We need to convert it to an integer to do the subtraction.

print("Your age is: ", 2026-byear_int) #byear_int is an integer. We can do the subtraction now.

####################################################################

myweight = float(myweight) #at the end of the day myweight becomes a float. It is no longer a string. We can do mathematical operations with it now.
height = float(height) #at the end of the day height becomes a float. It is no longer a string. We can do mathematical operations with it now.
byear = int(byear) #at the end of the day byear becomes an integer. It is no longer a string. We can do mathematical operations with it now.

print("your age is " , 2026-byear) #this will work because there is comma
print("your age is " + str(2026-byear)) # plus means there is concatenation, so we need to convert the number to a string first.
