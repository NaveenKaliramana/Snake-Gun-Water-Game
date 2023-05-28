#####           Snake Gun Water Game
import random
def main():
    ans = int(input("Enter a Number (0,1,2) : "))
    if ans == 0 or ans == 1 or ans == 2:
        if ans == cr:               ### Computer and You Choose Same, So Game Ends in Draw
            res = "Game Draw"
            print(res)
            with open("Result", "a") as f:
                f.write(f"\n{res}")
        elif cr == 0:               ### Computer Choose "Snake"
            if ans == 1:            # You Choose "Gun" and will kill Snake with Gun, So You Win
                print("You Won")
                with open("Result", "a") as f:
                    f.write(f"\n{res}")
            elif ans == 2:          # You Choose "Water" and Snake will Drink Water, So Computer Win
                print("You Lose")
                with open("Result", "a") as f:
                    f.write(f"\n{res}")
        elif cr == 1:               ### Computer Choose "Gun"
            if ans == 0:            # You Choose "Snake" and Gun will kill snake, So Computer Win
                res = "You Lose"
                print(res)
                with open("Result", "a") as f:
                    f.write(f"\n{res}")
            elif ans == 2:          # You Choose "Water" and Water will rust the Gun, So You Win
                res = "You Won"
                print(res)
                with open("Result", "a") as f:
                    f.write(f"\n{res}")
        elif cr == 2:               ### Computer Choose "Water"
            if ans == 0:            # You Choose "Snake" and Snake will drink Water, So You Win
                res = "You Won"
                print(res)
                with open("Result", "a") as f:
                    f.write(f"\n{res}")
            elif ans == 1:          # You Choose "Gun" and Water will rust the Gun, So Computer Win
                res = "You Lose"
                print(res)
                with open("Result", "a") as f:
                    f.write(f"\n{res}")      
    else:
        print("Enter Valid Number from (0 , 1 ,2)")
        main()

print("*****        Welcome to Snake Gun Water Game             *****")
cr = random.randint(0, 2)
#####       0 = snake , 1 = gun  , 2 = water
main()