# while loops = execute some code WHILE some condition remains true

#iteration = Loop---- iterate(verb) looping over something
# name = input("Enter your name: ")
# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name: ") # infinite loops are bad
# print(f"Hello {name}")

# age = int(input("Enter your age: "))
# while age < 0:
#     print("Age cant be negative: ")
#     age = int(input("Enter your age: "))

# print(f"You are {age} years old")

# food = input("Emter a food you like(q to quit): ")

# while not food == "q":
#     print(f"you likr {food}")
#     food = input("Emter a food you like(q to quit): ")

# print("bye")

# num = int(input("Enter a # 1 - 10: "))

# while num < 1 or num > 10:
#     print(f"{num} is not valid")
#     num = int(input("Enter a # 1 - 10: "))

# print(f"Your number is {num}")




# for loops = execute a block of code a fixed number of times
#             You can iterate over a range, string, sequence, etc

# for x in reversed(range(1, 11)):
#     print(x)

# print("HAPPY NEW YEAR")

# credit_card  = "1234-5678-9012-3456"

# for x in credit_card:
#     print(x)

# for x in range(1, 21):
#     if x == 13 or x == 15 or x == 20:
#         continue
#     else:
#         print(x)

# for x in range(1, 21):
#     if x == 13:
#         break
#     else:
#         print(x)

# horror_characters = ("Freddy kreuger", "Jason Voorhees", "Michael Myers", "Pennywise", "Chucky")

# for x in horror_characters:
#     # if x == "Jason Voorhees":
#     #  continue
#     if x == "Michael Myers":
#         x = "Dracula"
#     print(x)

movie = ("IT", "Scream", "Chucky", "The nun", "Friday the 13th")

for x in movie:
    if x == "The nun":
        break
    elif x == "IT":
        x = "The conjuring"
    print(x)