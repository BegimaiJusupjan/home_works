from home_wordef main():
    while True:
        print("1.begin")
        print("2.exit game")
        choice_=int(input("vyberi: "))
        if choice_==1:
            com_ch=computer_choice()
            us_ch=user_choice()
            if us_ch==-1:
                print("nepravilny vybor")
                continue
                res=check(com_ch,us_ch)
                print(res)
            elif choice_==2:
                break
            else:                                    git