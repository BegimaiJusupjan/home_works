def func():
    print("python")
    print("jawa")
    print("git")
    print("#"* 10)
#f=func
#f()
# pr=print
# pr("My names Arsen")
# i=input
def area_circle():
    radius=float(input("Enter the radius"))
    s=3,14*radius**2
    print("Ayant",s)

def area_rectangle(width,height):
    if width<0 or height<0:
        print("it is imposible")
    else:

        area=width*height
        print("ayant",area)
#area_rectangle(10,11)
def info():
    info="Arsen"
    print("Your name is ",info)
#info()
def info(name):
    print(f"your name is {name}")
#info("Arsen")
#info("Adil")
name=input("Enter name:")
info(name)
