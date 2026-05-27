import string
from time import time
from random import randint

users={"user1":{"password":"useradmin"}}
uscards={"user1":{"How do we translate the word 'Apple' to russian?":"a","When did people go to space":"1961"}}

def log(user,password):


    if user in users and users[user]["password"]==password:
        print(f"Success. Welcome back {user}!")

    else:
        raise ValueError("System Error, check your login or password")

def reg(user,password):

    if user in users:
        raise ValueError("System Error, User already exists do you want to log in?")

    if len(password) < 5:
        raise ValueError("System Error, password must be at least 5 characters long")

    if any(char in string.punctuation for char in password):
        raise ValueError("System Error, Unexpected symbols")

    users[user] = {"password": password}
    uscards[user] = {}
   

def addcard(user):
    print("Great! Use this method to add card: question-answer")
    adcard = input("Input your card:\n")

    if "-" in adcard:
        q,a=adcard.split("-")
        uscards[user][q] = a

    else:
        raise ValueError("System Error, Hey lil bro you used wrong method. Oopsie uwu")

def rep(user):
    e=str(input("0-start, 1-stop\n"))
    a=[]
    questions = list(uscards[user].keys())
    answers = list(uscards[user].values())
    if not questions:
        raise ValueError("System Error, No questions entered")

    while e=="0":

        i=randint(0,len(questions)-1)
        print(questions[i],"\nYou have 30 seconds left uwu,")
        t1 = time()

        answ=input("Input your answer:\n")

        if answ=="1":
            print(sum(a))
            e="1"

        elif not questions:
            break
        elif time()-t1 > 30:
            print("Stupid;[")
            print(round(time()-t1))

        elif answ == answers[i]:
            print("You are doing so well. If you get max score I will be happy :)")
            a.append(1)
            del questions[i]
            del answers[i]


        else:
            print("At least you tried... Try to remember/")
            a.append(0)
            questions.append(questions[i])
            answers.append(answers[i])

def main():
    u=None
    enter = input("If you want to log in - 0, if register - 1. Input:\n")

    if enter == "0":
        u, p = input("Input your username:\n"), input("Input your password:\n")
        log(u, p)

    elif enter == "1":
        u, p = input("Input your username:\n"), input("Input your password:\n")
        reg(u, p)
    else:
        raise ValueError("Unexpected command")



    c=u.capitalize()
    while True:
        try:
            motion = input(
                f"{c} would you like add more cards or js repeat? If u want to add more cards - 0, if repeat - 1\nInput:\n")

            if motion == "0":
                addcard(u)

            elif motion == "1":
                rep(u)

            else:
                raise ValueError("Unexpected command")
        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)

if __name__=="__main__":
    main()
