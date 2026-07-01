age = int(input("What is your age? ")) 

if age < 6 or age > 65: #for this condition to be true, at least one of the inequalities has to be true. If both of them are false, the whole condition will be false.
    print("You go free")
else:
    print("You have to pay $20")

#We are combining multiple conditions using logical operators
# or is one of them
#there is also and. 

if age > 6 and age < 65: #for this condition to be true both inequalities have to be true. If one of them is false, the whole condition will be false.
    print("You have to pay $20")
else:
    print("You go free")


weight = float(input("weight?"))
height = float(input("height?"))
bmi = weight/height**2

#block comment below is a BMI chart. It shows the different categories of BMI and their corresponding ranges.
'''
UnderweightBelow 18.5
Healthy Weight18.5 – 24.9
verweight25.0 – 29.9
Obesity30.0 or greater
''' 

if bmi < 18.5:
    print("You are underweight with a BMI of: ", bmi)
elif bmi >= 18.5 and bmi < 25:
    print("You are healthy with a BMI of: ", bmi)
elif bmi >= 25 and bmi < 30:
    print("You are overweight with a BMI of: ", bmi)
else:
    print("You are obese with a BMI of: ", bmi)

