import random

top_range = input("Please maximum range number \n")

if (top_range.isdigit()):
    top_range= int(top_range)
    if (top_range<=0):
        print("Please enter a number greater than zero next time")
        quit()
else:
    print ("That's not a number  \nPlease enter a number next time")
    quit()

random_number= random.randint(0,top_range)
guesses = 0

while True:
    guesses += 1
    answer = input("Please enter a guess of the number chosen by the computer: ")

    if (answer.isdigit()):
        answer = int(answer)
        if (answer == random_number):
            print('You got it')
            break
        elif(answer<random_number) :
            print('try again, your guess was lower than the random number chosen by the computer')
        elif(answer>random_number):
            print('try again, your guess was higher than the random number chosen by the computer')

    else:
        print("Please enter a number")
        continue
print("you got the right answer in",guesses,"guesses")
