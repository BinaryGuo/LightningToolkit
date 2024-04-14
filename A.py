import math,time,random

months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
day_ending = ['st','nd','rd'] + 17* ['th'] + ['st','nd','rd'] + 8* ['th']
database = [['xyl','1038'],['SU','20121129'],['yzb','2835'],['wyj','3458'],['yjy','5849'],['gjm','5482']]
chancer = 1
chance = 3
chancers = 10 

def logo() :
    print('_____                                           _____                   ______                                                                   ')
    print('|   |                                           |   |                   |    |                                                                    ')
    print('|   |                                           |   |                   |    |                                                                    ')
    print('|   |                                           |   |                   |    |                                                                    ')
    print('|   |                                           |   |                   |    |                                                                    ')
    print('|   |                                           |   |                   |    |                                                                    ')
    print('|   |                _____                      |   |                   |    |                         _____                                      ')
    print('|   |                |   |                      |   |                   |    |                         |   |                                      ')
    print('|   |                |___|                      |   |                   |    |                         |___|                                      ')
    print('|   |                _____  __________________  |   |____________  _____|    |_____  ________________  _____  _______________  ___________________')
    print('|   |                |   |  |                |  |               |  |              |  |              |  |   |  |             |  |                 |')
    print('|   |                |   |  |   __________   |  |   ________    |  |____      ____|  |   ________   |  |   |  |   _______   |  |   __________    |')
    print('|   |                |   |  |   |        |   |  |   |       |   |       |    |       |   |      |   |  |   |  |   |     |   |  |   |        |    |')
    print('|   |                |   |  |   |        |   |  |   |       |   |       |    |       |   |      |   |  |   |  |   |     |   |  |   |        |    |')
    print('|   |                |   |  |   |        |   |  |   |       |   |       |    |       |   |      |   |  |   |  |   |     |   |  |   |        |    |')
    print('|   |                |   |  |   |        |   |  |   |       |   |       |    |       |   |      |   |  |   |  |   |     |   |  |   |        |    |')
    print('|   |                |   |  |   |        |   |  |   |       |   |       |    |       |   |      |   |  |   |  |   |     |   |  |   |        |    |')
    print('|   |______________  |   |  |   |________|   |  |   |       |   |       |    |       |   |      |   |  |   |  |   |     |   |  |   |________|    |')
    print('|                 |  |   |  |                |  |   |       |   |       |    |       |   |      |   |  |   |  |   |     |   |  |                 |')
    print('|_________________|  |___|  |_____________   |  |___|       |___|       |____|       |___|      |___|  |___|  |___|     |___|  |_____________    |')
    print('                                         |   |                                                                                               |   |')
    print('                                         |   |                                                                                               |   |')
    print('                                         |   |                                                                                               |   |')
    print('                                         |   |                                                                                               |   |')
    print('                                         |   |                                                                                               |   |')
    print('                                         |   |                                                                                               |   |')
    print('                                         |   |                                                                                               |   |')
    print('                            _____________|   |                                                                                 ______________|   |')
    print('                            |                |                                                                                 |                 |')
    print('                            |________________|                                                                                 |_________________|')

def account() :
    def timer1(interval) :
        time1 = interval
        while time1 != 0 :
            time.sleep(1)
            time1 -= 1
            print("your account has been locked, it will unlock in %d seconds!"%time1)
    global chance,chancer,chancers
    while True :
        name = input('please enter your account name: ')
        password = input('please enter your account password: ')
        if [name,password] in database :
            print('welcome, ',name)
            break
        else :
            chance -= 1
            print("sorry, your account doesn't exist. now you have %d chance!"%chance)
            if chance == 0 :
                chance = 3
                timer1(chancers)
                chancers += 10


def judge2(interval) :
    r1 = input('go back?(yes:1, no:2)')
    r1_i = int(r1)
    if r1_i == 1 :
        pass
    else :
        interval()

def A_0_0_1() :
    def judge() :
        program = input('''
1_date  2_dice   3_timer(foward)   4_timer(back)   5_calculator
please choose program:''')
        program1 = int(program)
        if program1 == 1 :
            date()
        elif program1 == 2 :
            dice()
        elif program1 == 3 :
            timer2()
        elif program1 == 4 :
            timer3()
        elif program1 == 5 :
            calculator()
        else :
            print('No program named %d'%program1)
            time.sleep(2)

    def date() :
        year = input('enter year: ')
        month = input('enter month: ')
        day = input('enter day: ')
        month_int = int(month)
        day_int = int(day)
        Month = months[month_int -1]
        Day = day + day_ending[day_int -1]
        print(Month + ' ' + Day + ' , ' + year)
        judge2(date)

    def dice() :
        ttti = input('please enter mode(every random input:1, all random once input:2): ')
        tti = input('please enter random times(number): ')
        ttt = int(ttti)
        tt = int(tti)
        if ttt == 1 :
            for i in range(tt) :
                ti1 = input("please enter times(number): ")
                t1 = int(ti1)
                dice1 = math.ceil(random.random()*t1)
                print(dice1)
        else :
            tttti = input('please enter displar mode(list:1, pile up:2): ')
            ti2 = input("please enter times(number): ")
            tttt = int(tttti)
            t2 = int(ti2)
            if tttt == 1:
                ls = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 19:0, 20:0, 21:0, 22:0, 23:0, 24:0, 25:0, 26:0, 27:0, 28:0, 29:0, 30:0, 31:0, 32:0, 33:0, 34:0, 35:0, 36:0, 37:0, 38:0, 39:0, 40:0, 41:0, 42:0, 43:0, 44:0, 45:0, 46:0, 47:0, 48:0, 49:0, 50:0}
                for i in range(tt) :
                    dice2 = math.ceil(random.random()*t2)
                    ls[dice2] += 1
                print(ls)
            else :    
                for i in range(tt) :
                    dice2 = math.ceil(random.random()*t2)
                    print(dice2)
        judge2(dice)

    def timer2() :
        time2 = input('please enter second(s)(limitless:l): ')
        if 'l' in time2 :
            time2_1 = input('please enter the stop inquiry interval(numbers) :')
            time2_2 = 0
            time2_3 = int(time2_1)
            while True :
                for i in range(time2_3) :
                    print("%d second(s)"%time2_2)
                    time2_2 += 1
                    time.sleep(1)
                time2_4 = input("stop?(stop:1, don't stop:2): ")
                time2_5 = int(time2_4)
                if time2_5 == 1 :
                    break
        else : 
            time2_6 = int(time2)
            time2_7 = 0
            while time2_7 != time2_6 :
                print("%d second(s)"%time2_7)
                time2_7 += 1
                time.sleep(1)
        judge2(timer2)

    def timer3() :
        time1 = input('please enter seconds(s): ')
        time3 = int(time1)
        while time3 != 0 :
            time.sleep(1)
            time3 -= 1
            print("%d second(s)"%time3)
        judge2(timer3)

    def calculat1() :
        c2_1 = input('please enter operator: ')
        c2_2 = input('please enter number1: ')
        c2_3 = input('please enter number2: ')
        c2_2_i = int(c2_2)
        c2_3_i = int(c2_3)
        if '+' in c2_1 :
            c2_4 = c2_2_i + c2_3_i
        elif '-' in c2_1 :
            c2_4 = c2_2_i - c2_3_i
        elif '/' in c2_1 :
            c2_4 = c2_2_i / c2_3_i
        elif '**' in c2_1 :
            c2_4 = c2_2_i ** c2_3_i
        elif '%' in c2_1 :
            c2_4 = c2_2_i % c2_3_i
        else :
            c2_4 = c2_2_i * c2_3_i
        print(c2_2,c2_1,c2_3,'=',c2_4)

    def calculat2() :
        print('Sorry, Lightning A does not have this feature')

    def calculator() :
        c1 = input('please enter the mode(Multistep:1, single step:2): ')
        c1_i = int(c1)
        if c1_i == 1 :
            calculat2()
        else : 
            calculat1()
        judge2(calculator)

    while True :
        judge()

if __name__ == "__main__" :
    logo()
    account()
    A_0_0_1()