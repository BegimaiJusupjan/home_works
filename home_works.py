from random import choice

def computer_choice():
    return choice(["apple","orange","banana","mango","lemon","kiwi","lime"])

def user_choice():
    print("1.apple")
    print("2.orange")
    print("3.banana")
    print("4.mango")
    print("5.lemon")
    print("6.kiwi")
    print("7.lime")
    choice_=int(input("choose one of them:"))
    if choice_==1:
        return "apple"
    elif choice_==2:
        return "orange"
    elif choice_==3:
        return "banana"
    elif choice_==4:
        return "mango"
    elif choice_==5:
        return "lemon"
    elif choice_==6:
        return "kiwi"
    elif choice_==7:
        return "lime"
    else:
        return -1

def check(computer_choice,user_choice):
    if computer_choice==user_choice:
        return "you quessed it"
    else:
        return "you did not quess"

def main():
    while True:
        print("1.start")
        print("2.exit")
        choice_=int(input("choose: "))
        if choice_==1:
            while True:
                c_choice=computer_choice()
                u_choice=user_choice()
                if u_choice==-1:
                    print("wrong choice")
                    continue
        elif choice_==2:
            break
        else:
            print("wrong choice")
main()