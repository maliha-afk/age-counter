age= int(input("please enter your age: ")) 

grade=int(input("please enter your grade: "))

alphabet="qwertyuioplkjhgfdsazxcvbnmMNBVCXZASDFGHJKLPOIUYTREWQ"

specialsign= "!@#$%^&*()}{][+=-_/?.>,<':;~`|"

num=1234567890

if age <= 12 and age > 3 and grade <= 5:
    print(f"age {age} is below (or same) 12 and grade {grade} is below (or same) 5 .So you are a child")


elif age>=13 and age <= 19 and grade >= 6:
    print(f"age {age} is greater than (or same) 13 and grade {grade} is below (or same) 10 .So you are a teen")


elif age <= 3 and grade == 0:
    print(f"age {age} is below (or same) 3 and grade is {grade} .So basically you are a baby")


elif age >= 20 and age <= 30 :
     print(f"age {age} is greater than (or same) 20 .So basically you are an adult")


elif age >= 30 and age <=60 and grade ==0:
    print(f"age {age} is greater than (or same) 30 and grade is {grade} .So basically you are a middle aged adult")


elif age>60 and grade ==0:
    print(f"age {age} is greater than (or same) 60 and grade is {grade} .So basically you are an old person")


elif age == alphabet or age== num or age == specialsign:
    print("!ERROR!ERROR!")

