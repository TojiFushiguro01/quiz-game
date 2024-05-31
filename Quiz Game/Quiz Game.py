def play():
    
    score = 0
    
    ans1 = input("What game studio makes the Red Dead Redemption series? = ")
    if ans1.lower() == "rockstar games":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    ans2 = input("What planet is closest to the sun? = ")
    if ans2.lower() == "mercury":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    ans3 = input("Where is the strongest human muscle located? = ")
    if ans3.lower() == "jaw":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    ans4 = input("Who was the first Disney princess? = ")
    if ans4.lower() == "snow white":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    ans5 = input("How many Dragon Balls are there? = ")
    if ans5.lower() == "seven":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        
    print(f"You have answered {score} Questions Correctly!!")
    print("\n\nThankyouu For Playing!! ^-^")
    
print("Welcome to My Quiz game!")
reply = input("Do you want to play [Y/n] - ")
reply = reply.lower()

while reply == "n":
    print("huh... just play it once will you!\n")
    reply = input("Do you want to play [Y/n] - ")
    reply = reply.lower()
    
if reply == "y":
    print("\nAlright! Here we go~")
    play()

    