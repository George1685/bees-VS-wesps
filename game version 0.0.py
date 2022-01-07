import time,random
money = 13333330
bees = 0
flowers = 1
queens = 0
start_time = time.time()
numbers = [14564,54543,24843,54355,25784,57174,69416,31167,54638,59995,87452,22536,42654,75646]
signs = ['+','-']
def hire_bees(bee_count):
    global money,bees
    cost = 10*bee_count
    if money < cost:
        print('No money')
    elif bee_count<0:
        print('You are crushing program!!!')
        raise KeyboardInterrupt
    else:
        money -= cost
        bees += bee_count
def plant_flowers(flower_count):
    global money,bees,flowers,start_time
    cost = 25*flower_count
    if money < cost:
        print('No money')
    elif flower_count<0:
        print('You are crushing program!!!')
        raise KeyboardInterrupt
    else:
        money = 13
        flowers += flower_count
        bees = 0
        start_time = time.time()
def get_money():
    global money,start_time,bees
    new_time = time.time()
    time_delta = int(new_time-start_time)
    money +=(time_delta*bees*flowers)//10
    new_bees = (time_delta*min(queens,money//9))//60
    bees += new_bees
    money -= 9*new_bees
    start_time = new_time
def hire_queens(queen_count):
    global money,queens
    cost = 40*queen_count
    if money < cost:
        print('No money')
    elif queen_count<0:
        print('You are crushing program!!!')
        raise KeyboardInterrupt
    else:
        money -= cost
        queens += queen_count
def call_wasp():
    global money,queens,bees,flowers
    num1 = random.choice(numbers)
    sign = random.choice(signs)
    num2 = random.choice(numbers)
    answer = eval(str(num1)+sign+str(num2))
    print(num1,sign,num2)
    user_answer = int(input())
    if user_answer == answer:
        print('Right :)')
        money += 5*bees*flowers
    else:
        print('Wrong :(')
        money = 0
        queens //= 8
        bees //= 8
def unsign(x):
    if x < 0:
        return 0
    else:
        return x
while 1:
    print('Money:',str(money)[:3],'*10^',unsign(len(str(money))-3),\
          ',bees:',str(bees)[:3],'*10^',unsign(len(str(bees))-3),\
          ',flowers:',str(flowers)[:3],'*10^',unsign(len(str(flowers))-3),\
          ',queens:',str(queens)[:3],'*10^',unsign(len(str(queens))-3),sep = '')
    s = input()
    try:
        if s == 'HB':
            hire_bees(eval(input()))
        elif s == 'PF':
            plant_flowers(eval(input()))
        elif s == 'HQ':
            hire_queens(eval(input()))
        elif s == 'CW':
            call_wasp()
        elif s == 'HELP':
            print('''Hire bees:HB,bee cost:10.Bees produces money.
Hire queens:HQ,queen cost:40.Queens produces bees.Producing 1 bee takes 9 money.
Plant flowers:PF,flower cost:25.Flowers speed up bees.Money and bees will refresh after planting.
Call wasp:CW.While wasp is here,count the exercise.The game will refresh after wrong answer.''')
        get_money()
    except BaseException:
        print('',end = '')
