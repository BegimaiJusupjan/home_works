# with open('file.txt','r') as file:
#     content= file.read()
#     print(content)
# with open('file.txt','w')  as file:
#     file.write("Hello word")
# with open("file.txt",'a') as file:
#
#
# with open('file.txt','r') as file:
#     content=file.read()
#     print(content)
# with open('files.txt','x') as file:
#     file.write("this is a new file")


# with open('file.txt','w+') as file:
#     file.write("Hello, Aman.\nthis is a new line.")
#     file.seek(0)
#     content=file.read()
#     print(content)


with open('file.txt','w') as file:
    for i in range(5):
        number=int(input("number: "))
        file.write(f"{number}\n")
numbers=[]
with open('file.txt','r') as file:
    for line in file:
        numbers.append(int(line.strip()))
    print(sum(numbers))


