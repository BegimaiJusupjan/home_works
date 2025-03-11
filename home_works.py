n="Ali"
m=25
print(f"Hello {n},you are {m}")
a=7
b=4
summ=a+b
print(f"summa {a}and {b}={a+b}")
m=[3,5,8,10,15]
while True:
    n=int(input("n: "))
    if n in m:
        print(f"number {n} founded")
        break

n=input().split(",")
for i in n:
    if int(i)%2==0:
        print(i)
        break
n=input("n:")
while True:
    if n=="1234":
        print("allowed")
        break
    else:
        print("not allowed")


