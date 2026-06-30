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