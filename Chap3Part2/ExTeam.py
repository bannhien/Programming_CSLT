import random
def Computer():
    return random.randint(1,3)
def Ketqua(human,computer):
    if human==computer:
        return "Draw!"
    elif (human==1 and computer==2) or (human==2 and computer==3) or (human==3 and computer==1):
        return "Human Win!"
    else:
        return "Computer Win!"
def Play():
    while True:
        human=int(input("Human: "))
        if human==0:
            break
        elif 0<human<=3:
            computer_choice=Computer()
            print("Computer:",computer_choice)
            result=Ketqua(human,computer_choice)
            print("Result:",result)
        else:
            print("Please enter the suitable number again!")
Play()