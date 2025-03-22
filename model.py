# def custom_sum(a,b):
#     return a+b
#
# def custom_sub(a,b):
#     return a-b
# def result(a,b):
#     return a*b
# def date(day,month,year):
#     return(date)
# lang = {"ru": "Привет", "eng": "Hello", "kg": "Cалам"}
#
#
# def great(language_code):
#     if language_code in lang:
#         return lang[language_code]
#     else:
#         return "mistake"
user_data=[]
def add_user(username):
    user_data.append(username)
    return f" пользователь{username} добавлен"
def get_user():
    return user_data
def delete_user(username):
    if username in user_data:
        user_data.remove(username)
        return f"пользователь {username} удален"
    else:
        return "пользователь не найден"

