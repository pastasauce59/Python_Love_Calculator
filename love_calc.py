print("Welcome to the Love Calculator")

name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

true = 0
love = 0

low_name1 = name1.lower()
low_name2 = name2.lower()

true += low_name1.count("t")
true += low_name1.count("r")
true += low_name1.count("u")
true += low_name1.count("e")

love += low_name1.count("l")
love += low_name1.count("o")
love += low_name1.count("v")
love += low_name1.count("e")

true += low_name2.count("t")
true += low_name2.count("r")
true += low_name2.count("u")
true += low_name2.count("e")

love += low_name2.count("l")
love += low_name2.count("o")
love += low_name2.count("v")
love += low_name2.count("e")

score = int(str(true) + str(love))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.") 