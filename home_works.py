

# def season():
#     season=int(input("enter san: "))
#     if season==5 or season==4 or season==3:
#         return "spring"
#     elif season==6 or season==7 or season==8:
#         return "summer"
#     elif season==9 or season==10 or season==11:
#         return "aurtum"
#     elif season==12 or season==1 or season==2:
#         return "winter"
#     else:
#         return "faulse"
# print(season(3))
# print(season(2))
# print(season(1))
# print(season(5))
# print(season(6))
# print(season(9))
def season(mounth):
    if mounth in [1,2,12]:
        return "winter"





def get_date(day,month,year):
    from datetime import date
    return date(day,month,year)
print(get_date(18,3,2023))


def funk(a,b,c):
