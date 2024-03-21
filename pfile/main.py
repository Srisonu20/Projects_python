# def func(x=1,y=2):
#     x=x+y
#     y +=1
#     print(x,y)
# func(x=0,y=2)

n = int(input())

if n % 2 != 0:
    print("Weird")

elif n % 2 == 0 and range(2, 6):
    print("Not Weird")

elif n % 2 == 0 and range(6, 21):
    print("Weird")

elif n % 2 == 0 and n > 20:
    print("Not Weird")

else:
    print("none")