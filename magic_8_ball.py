import random
def magic_8_ball():
    input("What is your question for the magic 8 ball?\n")
    result = random.randint(1, 20)
    if result == 1:
        answer = "It is certain"
    elif result == 2:
        answer = "Reply hazy, try again"
    elif result == 3:
        answer = "Don't count on it"
    elif result == 4:
        answer = "It is decidedly so"
    elif result == 5:
        answer = "Ask again later"
    elif result == 6:
        answer = "My reply is no"
    elif result == 7:
        answer  = "Without a doubt"
    elif result == 8:
        answer = "Better not tell you now"
    elif result == 9:
        answer = "My sources say no"
    elif result == 10:
        answer = "Yes, definitely"
    elif result == 11:
        answer = "Cannot predict now"
    elif result == 12:
        answer = "Outlook not so good"
    elif result == 13:
        answer = "You may rely on it"
    elif result == 14:
        answer = "Concentrate and ask again"
    elif result == 15:
        answer = "Very doubtful"
    elif result == 16:
        answer = "As I see it, yes"
    elif result == 17:
        answer = "Most likely"
    elif result == 18:
        answer = "Outlook good"
    elif result == 19:
        answer = "Yes"
    elif result == 20:
        answer = "Signs point to yes"
    else:
        answer = "Error"
    print(answer)

magic_8_ball()

def try_again():
    while True:
        response = input("Would you like to try again? (yes/no)\n").lower()
        if response == "yes":
            magic_8_ball()
        elif response == "no":
            print("Ok, goodbye.")
            break
        else:
            print("Invalid response, please type yes or no.")

try_again()



