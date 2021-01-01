import random
randNum = random.randint(1,15)
num =None
Guesses =0
while randNum!=num:
     num = int(input("Enter a Number \n"))
     Guesses += 1
     if num==randNum:
         print("You Guessed it Right")
     else:
        if num<randNum:
            print("Try Larger")
        else:
            print("Try Smaller")
print(f"Your Guess Was Correct in {Guesses} Guesses")
with open("C:\\Programs\\Python Programs\\HiScore.txt","r") as f:
    hiscore =int(f.read())
if hiscore>Guesses:
    with open("C:\\Programs\\Python Programs\\HiScore.txt","w") as f:
        f.write(str(Guesses))
