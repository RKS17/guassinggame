"""1. You are free to use anything we've studied till now.
2. The number of guesses should be limited, i.e (5 or 9).
3. Print the number of guesses left.
4. Print the number of guesses he took to win the game.
5. “Game Over” message should display if the number of guesses becomes equal to 0.
You are advised to participate in solving this problem. This task helps you to become a good problem solver and helps you accepting the challenge and acquiring new skills.

"""
n = 17
i = 0
c = 9
while i<9 :
    x = int(input("enter the guassing number:"))

    if x==n:
        print("you won the game",i+1)
        break
        #print("you won " + str(i+1) + " time")

    elif x<n:
        print("increase the number")
        print("you lost the game", i + 1)
        #print("you lost " + str(i+1) + " time")
    elif x>n:
        print("decrease tha number")
        print("you lost the game", i + 1)
       # print("you lost " + str(i+1) + " time")
    i = i + 1
    print(9 - i, "time left")

else:
    print("game over")
    print("thank u for playing")
 
    


