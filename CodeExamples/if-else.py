#if-else statements are called duel alternative. Means two paths to choose from

a = 7
b = 9

if a == b:
    print("These are equl")
else:
    print("These are NOT equal")

#evaluating strings with if-else
message = "yes"

if message == "yes":
    print("You said yes.")
else:
    print ("nope!")

#see if you can vote... we are only checking if someone is 18 or older

age = int(input("Please give me your age: "))
if age >= 18:
    print("You can vote")
else:
    print("You can NOT vote")

#NESTED IFS WORK BY HAVING A SERIES OF IT STATEMENTS THAT MUST BE TRUE, AND THEN DRILLED
#DOWN TO THE CAULE YOU ARE LOOKING FOR
#compund conditions and elif statements can help relieve some of this
#lets create a qucik program that will say you get a discounted movie if you are 12 and younger of if 
#you are a senior citizen

#we use nested ifs to check for multiple conditions 

ticket_price = 10.00
discount = 0.10

age = int(input("Whats your age "))
rating = "G"

if(rating == "G"):
    if age <= 12:
        ticket_price = ticket_price - (ticket_price * discount)
        print("Child discount. your ticket price is", ticket_price)

else: 
    if (age >= 65):
        ticket_price = ticket_price - (ticket_price * discount)
        print("Senior citizen discount. Ticket price", ticket_price)

    else:
        print("Ticket full price", ticket_price)

#else-if.py
# MULTI-ALTERNATIVE MORE THAN 2 BRANCHES
#usually deals with ranges or deals with having multiple conditions to check
#to do this we use else-if statements. in python elif

#below is an example of using elif statements to change numerical grades into letter grades (thnk like a gradebook) 
#ie - A = 90-100, B = 80-89, C = 70-79 etc...

number_grade = 72
letter_grade = ""

if number_grade >= 90:
    letter_grade = "A"

#well n80 is greater than 70, why does my letter grade not change to a C
#short-circuit evaluation
#as soon as a condition is met, it exits the elif structure
elif number_grade >= 80:
    letter_grade = "B"

elif number_grade >= 79: 
    letter_grade = "C"

else: letter_grade = "F"

print("Your letter grade is ")
