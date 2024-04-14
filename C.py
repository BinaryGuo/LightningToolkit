import time,random,pygame,socket,math,multiprocessing,matplotlib.pyplot as plt,traceback

months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
day_ending = ['st','nd','rd'] + 17* ['th'] + ['st','nd','rd'] + 8* ['th']
s1 = socket.socket()
s2 = socket.socket()
Lin1 = 'year2023:'
Lin1_1 = 'Nov. 1st,A Alpha。'
Lin1_2 = 'Nov. 11th,A Stable。'
Lin1_3 = 'Nov. 5th,B Alpha。'
Lin1_4 = 'Nov. 19th,C Alpha。'
Lin2 = 'year2024'
Lin2_1 = 'Jan. 1st,B Stable'
Lino1 = 'Thanks:\nVisual Studio Code\nSubversion'
Lino2 = 'My e-mail address:tp114514251@outlook.com'
database1 = [['xyl','1038'],['SU','kill name'],['yzb','2835'],['wyj','3158'],['yjy','5849']]
database2 = {'SU':{'address':'second floor right room','password':'kill name'},'xyl':{'address':'second floor right room','password':'1038'},'yzb':{'address':'second floor left room','password':'2835'},'wyj':{'address':'second floor left,right room','password':'3158'},'yjy':{'address':'first floor left room','password':'5849'}}
ca = 0
use = 0
jt = {
'English':{
    'A' : '''
1-date_formatting   2-dice   3-timer_foward   4-timer_back   5-calculator
please choose program: ''',
    'B' : '''
1-date_formatting   2-dice   3-timer_foward   4-timer_back   5-calculator   6-text_box   7-joker1   8-number_game   9-account_info   10-Lightning_history
11-log_off   12-Lightning_info   13-joker2   14-fibonacci   15-taxas1   16-judge_rating   17-judge_type   18-release_note   19-chess1
please choose program: ''',
    'C' : '''
1-date   2-dice   3-timer_foward   4-timer_back   5-calculator   6-text_box   7-joker1   8-number_game   9-account_info   10-Lightning_history
11-log_off   12-Lightning_info   13-joker2   14-fibonacci   15-taxas1   16-judge_rating   17-judge_type   18-release_note   19-chess1   20-chess2_server
21-chess2_client_black   22-chess2_client_white   23-G_language_editer1   24-LevoOS1_log_in   25-joker3   26-taxas2   27-life_game1   28-made_account   29-LevoOS1_new   30-form
please choose program: '''},
'Chinese':{
    'A' : '''
1-格式化日期   2-骰子   3-正向计时器   4-倒计时   5-计算器
请选择程序：''',
    'B' : '''
1-格式化日期   2-骰子   3-正向计时器   4-倒计时   5-计算器   6-字符包装   7-斗地主1代   8-数字游戏   9-账号信息   10-Lightning历史
11-登出   12-Lightning信息   13-斗地主2代   14-fibonacci数列   15-德州扑克1代   16-评级   17-判断类型   18-发行说明   19-国际象棋1代
请选择程序：''',
    'C' : '''
1-格式化日期   2-骰子   3-秒表   4-倒计时   5-计算器   6-字符包装   7-斗地主1代   8-数字游戏   9-账号信息   10-Lightning历史
11-登出   12-Lightning信息   13-斗地主2代   14-fibonacci数列   15-德州扑克1代   16-评级   17-判断类型   18-发行说明   19-国际象棋1代   20-国际象棋2代_服务端
21-国际象棋2代_白方客户端   22-国际象棋2代_黑方客户端   23-G语言编辑器一代   24-极想OS1代   25-斗地主3代   26-德州扑克2代   27-人生游戏   28-注册账号   29-人生游戏2   30-表格生成器'''}}
#1234567
database3 = ['114514-LEVOSK','173934-LEVOK1','435676-LEVOK2','920572-LEVOK3']
syss = {'gqx':{'disk':512,'language':'English','passwd':{'SU':'20121129','Adminstrator':'20121129'},'path':{'logs_Adminstrator_w-':{'export.txt':'''
Group:
Adminstrator:Adminstrator
user:Adminstrator
Suffix:
.txt:text editer;'''},'Adminstrator_Adminstrator_wr':{},'media_Adminstrator_r':{'Lightning':{}}}}}
pygame.init()
WIDTH = 1000
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Two-Player Chess Game')
font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf', 40)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 10
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

captured_pieces_white = []
captured_pieces_black = []

turn_step = 0
selection = 100
valid_moves = []

# load in game piece assist (queen, king, rook, bishop, knight, pawn) x 2
black_queen = pygame.image.load('./assist/black queen.png')
black_queen = pygame.transform.scale(black_queen, (80, 80))
black_queen_small = pygame.transform.scale(black_queen, (45, 45))
black_king = pygame.image.load('./assist/black king.png')
black_king = pygame.transform.scale(black_king, (80, 80))
black_king_small = pygame.transform.scale(black_king, (45, 45))
black_rook = pygame.image.load('./assist/black rook.png')
black_rook = pygame.transform.scale(black_rook, (80, 80))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))
black_bishop = pygame.image.load('./assist/black bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (80, 80))
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))
black_knight = pygame.image.load('./assist/black knight.png')
black_knight = pygame.transform.scale(black_knight, (80, 80))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))
black_pawn = pygame.image.load('./assist/black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (65, 65))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))
white_queen = pygame.image.load('./assist/white queen.png')
white_queen = pygame.transform.scale(white_queen, (80, 80))
white_queen_small = pygame.transform.scale(white_queen, (45, 45))
white_king = pygame.image.load('./assist/white king.png')
white_king = pygame.transform.scale(white_king, (80, 80))
white_king_small = pygame.transform.scale(white_king, (45, 45))
white_rook = pygame.image.load('./assist/white rook.png')
white_rook = pygame.transform.scale(white_rook, (80, 80))
white_rook_small = pygame.transform.scale(white_rook, (45, 45))
white_bishop = pygame.image.load('./assist/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (80, 80))
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))
white_knight = pygame.image.load('./assist/white knight.png')
white_knight = pygame.transform.scale(white_knight, (80, 80))
white_knight_small = pygame.transform.scale(white_knight, (45, 45))
white_pawn = pygame.image.load('./assist/white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (65, 65))
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))

white_assist = [white_pawn, white_queen, white_king,
                white_knight, white_rook, white_bishop]
small_white_assist = [white_pawn_small, white_queen_small, white_king_small, white_knight_small,
                      white_rook_small, white_bishop_small]

black_assist = [black_pawn, black_queen, black_king,
                black_knight, black_rook, black_bishop]
small_black_assist = [black_pawn_small, black_queen_small, black_king_small, black_knight_small,
                      black_rook_small, black_bishop_small]

piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']
var = {}
func = {}
e = '''
error in file <G_shell> :
'''
def process(script_l):
    script = '''def temp() :
'''
    for i in script_l: script += i + '''
'''
    script += '''tmp = temp()
print('return is:',tmp)'''
    exec(script)
counter = 0
winner = ''
game_over = False

def 格式化日期():
    year = input('输入年: ')
    month = input('输入月: ')
    day = input('输入日: ')
    month_int = int(month)
    day_int = int(day)
    Month = months[month_int -1]
    Day = day + day_ending[day_int -1]
    print(Month + ' ' + Day + ' , ' + year)

def 牌() :
    colors = ['红桃', '方片', '梅花', '黑桃']
    numbers = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
    all_cards = ['小王', '大王']
    for number in numbers:
        for color in colors:
            card = color+"_"+str(number)
            all_cards.append(card)
    return all_cards

def 发牌(all_cards):
    random.shuffle(all_cards)
    tp =  {
        "玩家 A":all_cards[:17],
        "玩家 B":all_cards[17:34],
        "玩家 C":all_cards[34:51],
    }, all_cards[51:]
    return tp

def 大小(card_str):                                                                                                                                                                                                                                    
    if card_str=="大王": return 17
    elif card_str == "小王" : return 16
    else:
        parts = card_str.split("_")
        number = parts[1]
        if number == "A" : return 14
        elif number == "K" :return 13
        elif number =="Q" : return 12
        elif number =="J" : return 11
        elif number =="2" : return 15
        else:
            return int(number)

def 红桃3(a_people_card): return "红桃_3" in a_people_card

def sort(ls,card):
    sortedls = []
    for i in card:
        if i in ls:
            sortedls.append(i)
    return sortedls

def joker3() :
    ca = 0
    if '1' == input('please enter display mode(list:1, dict:2): ') :
        all_player_cards, cover_cards = deal(card())
        player = all_player_cards['player A']
        sort(player)
        st = strloop(value_dict)
        stlarge = largeststra(st)
        while True:
            if ca == 0:
                print('your cards:')
                print(value_dict)
                print("bomb ", bomb(value_dict))
                print("triple", triple(value_dict))
                print("double", double(value_dict))
                print("heart 3",  heart3(player))
                print('straight', st)
                print('largest straight', largeststra(st))
                ca += 1
                push = input('discard')
            else:
                print(value_dict)
    else :
        all_player_cards, cover_cards = deal(card())
        player = all_player_cards['玩家 A']
        op = (all_player_cards['玩家 B'],all_player_cards[' C'])
        value_dict = conter(player)
        op = (conter(op[0]),conter(op[1]))
        st = strloop(value_dict)
        GPT = cw1(value_dict)
        while True:
            if ca == 0:
                print('your cards:')
                print(value_dict)
                print("bomb: " , bomb(value_dict))
                print("triple: " , triple(value_dict))
                print("double: " , double(value_dict))
                print("heart 3: " ,  heart3(player))
                print('straight: ' , st)
                print('largest straight: ' , largeststra(st))
                print('card score: ' , sd(GPT))
                print('rocket: ' , rocket(player))
                ca += 1
                push = input('discard: ')
                
            else:
                print(value_dict)

def double(dict) :
    all_double = []
    for key in dict: 
        if 2 == dict[key]:
            all_double.append(key)
    if len(all_double) == 0 :
        return False
    else :
        return all_double

def jstr(value_dict, head_tail) :
    save = 0
    for i in range(head_tail[0],head_tail[1]) :
        if value_dict[i] != 0 :
            save += 1
    if save >= 5 :
        return head_tail
    else :
        return False

def strloop(vd) :
    save = []
    for i in range(3,11) :
        for j in range(5,15-i+1) :
            if jstr(vd,(i,i+j)) != False :
                save.append(jstr(vd,(i,i+j)))
    if len(save) == 0:
        return False
    else :
        return save

def largeststra(all) :
    lar = None
    large = 4
    for head,tail in all :
        save = tail - head + 1
        if save > large :
            lar = (head,tail)
            large = save
    return lar

def G_language_editer1(lay = 1):
    try :
        global var,e,func
        indent = '>'
        indent *= lay
        indent +=  ' '
        std_s = input(indent)
        std_l = list(std_s)
        edd = 'print(e,std_s)'
        if ' = ' in std_s :
            cut = std_s[4:]
            try:
                var[(std_l[0])] = int(cut)
            except ValueError :
                var[(std_l[0])] = cut
        elif ' == ' in std_s :
            del std_l[1:5]
            try:
                if var[std_l[0]] == int(std_l[1:]):
                    print('True')
                else:
                    print('False')
            except ValueError :
                if var[std_l[0]] == std_l[1:]:
                    print('True')
                else:
                    print('False')
            except KeyError :
                eval(edd)
                print('        key_error : no such key of vars')
        elif 'checkvars' in std_s :
            if 'checkvars()' in std_s :
                checkvars_sth1 = input(': ')
                if checkvars_sth1 in var.keys() :
                    print(var[checkvars_sth1])
                else :
                    eval(edd)
                    print('        parameter_error: no such key of vars')
            else :
                print(var)
        elif ' func ' in std_s :
            try:
                del std_l[1:6]
                fkey = std_s[7:7 + int(std_l[0])]
                func[fkey] = []
                while True :
                    def_sth1 = input(': ')
                    if def_sth1:
                        func[fkey].append(def_sth1)
                    else:
                        break
            except ValueError :
                pass
        elif 'for ' in std_s :
            del std_l[:4]
            for_str = '''
for i in range(int(std_l[0])):
'''
            while True :
                for_sth1 = input(': ')
                if for_sth1:
                    for_str += for_sth1 + '''
'''
                else:
                    break
            print(for_str)
            exec(for_str)                    
        elif 'checkfuncs' in std_s :
            if 'checkfuncs()' in std_s :
                checkfuncs_sth1 = input(': ')
                if checkfuncs_sth1 in func.keys() :
                    print(func[checkfuncs_sth1])
                else :
                    eval(edd)
                    print('        parameter_error: no such key of functions')
            else :
                print(func)
        elif 'process()' in std_s :
            try:
                sth1 = input(': ')
                process(func[sth1])
            except KeyError :
                eval(edd)
                print('        parameter_error: no such key of functions')
        elif std_s:
            pass
        else:
            eval(edd)
            print('        syntax_error: syntax unavailble')
    except :
        print()
        print("Sorry, your operation (Maybe it's not wrong) caused Bottom layer Python error, please put the following error message on http://www.G-language.org/error/upload, thanks for upload!")
        print('The error message is:')
        print()
        traceback.print_exc()

def 骰子():
    ttti = input('请输入模式(每次掷骰子时进行输入:1, :2): ')
    tti = input('请输入掷骰子的次数: ')
    ttt = int(ttti)
    tt = int(tti)
    if ttt == 1 :
        for i in range(tt) :
            ti1 = input("请输入骰子的面数: ")
            t1 = int(ti1)
            dice1 = math.ceil(random.random()*t1)
            print(dice1)
    else :
        tttti = input('请输入显示模式(列表:1, 堆积:2): ')
        ti2 = input("请输入骰子的面数: ")
        tttt = int(tttti)
        t2 = int(ti2)
        if tttt == 1:
            ls = {}
            for i in range(t2) :
                ls[i] = 0
            for i in range(tt) :
                dice2 = math.ceil(random.random()*t2)
                ls[dice2] += 1
            print(ls)
        else :    
            for i in range(tt) :
                dice2 = math.ceil(random.random()*t2)
                print(dice2)
def Ligntning信息():
    print('版本:C, 未修复漏洞:所有')

def get_random(times = 5):return math.ceil(random.random() * times)
shuxing = {'魅力':get_random(),'智力':get_random(),'毅力':get_random(),'体能':get_random(),'快乐':get_random(),'性别':get_random(),'健康':get_random(),'家境':get_random()}
def life_game():
    if 5 not in shuxing.values():
        input('''
魅力
智力
毅力
体能
快乐
男
女
健康
请指定一项作为你的天赋(“男”,“女”变为相应性别,其他变为5)''')
    print(f'''你出生在一个普通的家庭里，你的人生开始了！
魅力:{shuxing["魅力"]}
智力:{shuxing["智力"]}
毅力:{shuxing["毅力"]}
体能:{shuxing["体能"]}
快乐:{shuxing["快乐"]}
性别:{shuxing["性别"]}
健康:{shuxing["健康"]}
家境:{shuxing["家境"]}''')
    
    zhuazhou = input('''首先，你来到了抓周仪式:
1_链 : 魅力 + 1
2_计算器 : 智力 + 1
3_成山的练习册 : 毅力 + 1
4_跑鞋 : 体能 + 1
5_玩具 : 快乐 + 1
6_手术刀 : 20岁时变性
7_水果 : 健康 + 1
序号: ''')

def chess2_server():
    print('GQX chess server launcher')
    print('loading settings...')
    s = socket.socket()
    s.bind(('localhost',50000))
    s.listen(2)
    print('load finish')
    print('wait for connection 1(total:2)...')
    c1,addr1 = s.accept()
    print('connection from:',addr1)
    c1.send("You are connecting GQX chess server!,please wait the another connect player.".encode("utf-8"))
    print('wait for connection 2(total:2)...')
    c2,addr2 = s.accept()
    print('connection from:',addr2)
    c1.send('two player connecting, game on!'.encode("utf-8"))
    c2.send('two player connecting, game on!'.encode("utf-8"))
    print('two player connecting, game on!')
    '''
    while True:
        c1_c = c1.recv(1024)
        c2_c = c2.recv(1024)
        if c2_c != c1_c:
            c2.send(f'the another player choose {c1_c}, do you agree?'.)
        else:
            c1.send(f'time set finish:')
            c2.send(f'')
    '''
    while True :
        print("It's time for White to play")
        recv1 = c1.recv(1024)
        print("recv1", recv1)
        c2.send(recv1)
        print("It's time for Black to play")
        recv2 = c2.recv(1024)
        print("recv2", recv2)
        c1.send(recv2)
        if recv1 == 'close' and recv2 == 'close' :
            c1.send('goodbye')
            c2.send('goodbye')
            c1.close()
            c2.close()
            print('game over, servicing shutdown')
            break

def account() :
    try:
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
            if [name,password] in database1 :
                print('welcome, ',name)
                break
            else :
                chance -= 1
                print("sorry, your account doesn't exist. now you have %d chance!"%chance)
                if chance == 0 :
                    chance = 3
                    timer1(chancers)
                    chancers += 10
        return name
    except:
        print(f'Sorry,the program went wrong. it will turn back automatically in 2 second.')
        time.sleep(2)
        account()

def judge(text) :
    try:
        useful_parts = [w.strip().split("-") for w in text.replace('\n', ' ').split(" ") if len(w.strip())>0]
        useful_parts = [w for w in useful_parts if len(w)==2]
        value_dict = {}
        for item in useful_parts: value_dict[item[0]] = item[1]
        program = input(text)
        a = eval((value_dict[program]))
        a()
    except:
        print(f'Sorry,the program went wrong. it will turn back automatically in 2 second.')
        time.sleep(2)

def log_off():
    global ca
    ca = 1

def 秒表() :
    time2 = input('请输入时间限制（秒）(无限制:l): ')
    if 'l' in time2 :
        time2_1 = input('请输入询问‘是否停止’间隔:')
        time2_2 = 0
        time2_3 = int(time2_1)
        while True :
            for i in range(time2_3) :
                print("%d 秒"%time2_2)
                time2_2 += 1
                time.sleep(1)
            time2_4 = input("停止？(停止:1, 不停止:2): ")
            time2_5 = int(time2_4)
            if time2_5 == 1 :
                break
    else : 
        time2_6 = int(time2)
        time2_7 = 0
        while time2_7 != time2_6 :
            print("%d 秒"%time2_7)
            time2_7 += 1
            time.sleep(1)

def 倒计时() :
    time1 = input('请输入时间（秒）: ')
    time3 = int(time1)
    while time3 != 0 :
        time.sleep(1)
        time3 -= 1
        print("%d 秒"%time3)

def 计算器() :
    inm = input('请输入算式: ')
    print(eval(inm))

def card() :
    colors = ['heart', 'diamond', 'spade', 'club']
    numbers = ['A', 'K', 'Q', 'J']
    numbers.extend(list(range(2, 11)))
    all_cards = ['JOKER', 'joker']
    for color in colors:
        for number in numbers:
            card = color+"_"+str(number)
            all_cards.append(card)
    random.shuffle(all_cards)
    return all_cards

def deal(all_cards):
    dict =  {
        "player A":all_cards[:17],
        "player B":all_cards[17:34],
        "player C":all_cards[34:51],
    }, all_cards[51:]
    return dict

def power(card_str):                                                                                                                                                                                                                                    
    if card_str=="JOKER": return 17
    elif card_str == "joker" : return 16
    else:
        parts = card_str.split("_")
        number = parts[1]
        if number == "A" : return 14
        elif number == "K" :return 13
        elif number =="Q" : return 12
        elif number =="J" : return 11
        elif number =="2" : return 15
        else:
            return int(number)

def heart3(a_people_card): return "heart_3" in a_people_card

def conter(a_people_card):
    number_list = list(range(3, 18))
    value_dict = {}
    for number in number_list: 
        value_dict[number] = 0
    for card_str in a_people_card:
        number = power(card_str)
        value_dict[number] += 1
    return value_dict

def bomb(a_peole_value_dict):
    all_bomb = []
    for key in a_peole_value_dict:
        if 4 == a_peole_value_dict[key]:
            all_bomb.append(key)
    if len(all_bomb) == 0 :
        return False
    else :
        return all_bomb

def triple(a_player_dict) :
    all_triple = []
    for key in a_player_dict :
        if 3 == a_player_dict[key] :
            all_triple.append(key)
    if len(all_triple) == 0 :
        return False
    else :
        return all_triple
def double(dict) :
    all_double = []
    for key in dict: 
        if 2 == dict[key]:
            all_double.append(key)
    if len(all_double) == 0 :
        return False
    else :
        return all_double

def 斗地主1代() :
    all_cards = card()
    all_player_cards, cover_cards = deal(all_cards)
    for player in all_player_cards:
        this_player_cards = all_player_cards[player]
        value_dict = conter(this_player_cards)
        print(player,':')
        print(value_dict)
        print("bomb ", bomb(value_dict))
        print("triple", triple(value_dict))
        print("double", double(value_dict))
        print("heart 3",  heart3(this_player_cards))
        print()
    print("cover", cover_cards)

def rocket(a_people_card) :return "joker" in a_people_card and "JOKER" in a_people_card

def cctc(card_str):
    if card_str == "JOKER":
        return (0, 4)
    elif card_str == "joker":
        return (1, 4)
    else:
        parts = card_str.split("_")
        color_mapping = {"spade": 1, "club": 2, "diamond":3, "heart":0}
        number_mapping = {"A":0, "K":12, "Q":11, "J":10}
        y = color_mapping[parts[0]]
        if parts[1] in number_mapping:
            x = number_mapping[parts[1]]
        else:
            x = int(parts[1])-1
        return (x, y)

def dimg(all_cards) :
    img_path = './assist/poker.png'
    img = PIL.Image.open(img_path)
    carda1, cover_cards = deal(all_cards)
    fig, axs = plt.subplots(4, 17)
    for i in range(len(carda1.keys())):
        player = list(carda1.keys())[i]
        player_card = carda1[player]
        player_card = sorted(player_card, key = lambda x:power(x))
        for j in range(len(player_card)):
            player_one_card = player_card[j]
            x_y = cctc(player_one_card)
            loc = vd[x_y]
            img_crop = img.crop(loc)
            axs[i, j].imshow(img_crop)
            axs[i, j].axis('off')
    for k in range(len(cover_cards)):
        x_y = cctc(cover_cards[k])
        loc = vd[x_y]
        img_crop = img.crop(loc)
        axs[3, k].imshow(img_crop)
        axs[3, k].axis('off')
    for k in range(3, 17, 1): axs[3, k].axis('off')
    plt.show()

def cw1(card_dict):
    hands = []
    for card, count in card_dict.items():
        if count == 1:
            hands.append({'type': 'single', 'cards': [str(card)]})
        elif count == 2:
            hands.append({'type': 'pair', 'cards': [str(card), str(card)]})
        elif count == 3:
            hands.append({'type': 'trio', 'cards': [str(card), str(card), str(card)]})
        elif count == 4:
            hands.append({'type': 'bomb', 'cards': [str(card), str(card), str(card), str(card)]})
    if card_dict[16] > 0 and card_dict[17] > 0:
        hands.append({'type': 'rocket', 'cards': ['16', '17']})
    return hands

def sh(hand):
    values = {'3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, 
        '9': 9, '10': 10, '11': 11, '12': 12, '13': 13, 
        '14': 14, '15': 15, '16': 16, '17': 17}
    hand_types = {'single': 1, 'pair': 2, 'trio': 3, 'bomb': 4, 'rocket': 5}
    hand_type = hand['type']
    cards = hand['cards']
    cards = [str(card) for card in cards]
    base_score = hand_types[hand_type]
    card_score = sum(values[card] for card in cards)
    final_score = base_score * card_score
    return final_score

def sd(deck):
    total_score = 0
    for hand in deck:
        total_score += sh(hand)
    return total_score - 200

def find_all_consecutive_sequences(cards):  
    # 移除大小王并转换牌面为数字  
    numbers = [int(card[-1]) if card[-1].isdigit() else 14 if card[-1] == 'A' else 15 for card in cards if card != 'JOKER']  
    if not numbers:  
        return []
    # 对数字排序  
    numbers.sort()  
    # 找出所有顺子  
    sequences = []  
    current_sequence = [numbers[0]]  
    for i in range(1, len(numbers)):  
        if numbers[i] == numbers[i - 1] + 1:  
            current_sequence.append(numbers[i])  
        else:  
            if len(current_sequence) >= 5:  # 顺子至少需要5张牌  
                sequences.append(current_sequence)  
            current_sequence = [numbers[i]]  
    if len(current_sequence) >= 5:  # 添加最后一个序列  
        sequences.append(current_sequence)
    return sequences  
  
def find_longest_consecutive_sequence(sequences):  
    if not sequences:  
        return None  
    longest_sequence = max(sequences, key=len)  
    return longest_sequence

def joker2() :
    all_cards = card()
    all_player_cards, cover_cards = deal(all_cards)
    for player in all_player_cards:
        this_player_cards = all_player_cards[player]
        value_dict = conter(this_player_cards)
        hand_numbers = [card.replace('spade_', '').replace('heart_', '') for card in this_player_cards]  
        gort = cw1(value_dict)
        all_sequences = find_all_consecutive_sequences(hand_numbers)
        print(player,':')
        print(value_dict)
        print("bomb " , bomb(value_dict))
        print("triple" , triple(value_dict))
        print("double" , double(value_dict))
        print("straight: " ,all_sequences)
        print('largest straight: ' , find_longest_consecutive_sequence(all_sequences))
        print("heart 3" ,  heart3(this_player_cards))
        print('score: ' , sd(gort))
        print('rocket: ' , rocket(this_player_cards))
        print()
    print("cover", cover_cards)
    dimg(all_cards)

def 字符包装() :
    t1 = input('请输入字符: ')
    t1_l = len(t1)
    box = t1_l + 10
    print('+' + (box - 2) * '-' + '+')
    print('|' + (box - 2) * ' ' + '|')
    print('|' + 4 * ' ' + t1 + 4 * ' ' + '|')
    print('|' + (box - 2) * ' ' + '|')
    print('+' + (box - 2) * '-' + '+')

def made_account() :
    global acc
    def passed():
        global database1
        print("Verified passed")
        database1.append([input("new account's name: "),input("new account's password:")])
    if acc == 'SU':
        passed()
    elif input("You're accessing the lockout feature, enter the superuser's password: ") == 'kill name':
        acc = 'SU'
        passed()

def 注册账号():
    global acc
    def passed():
        global database1
        print("验证通过")
        database1.append([input("新账号名: "),input("新账号密码:")])
    if acc == 'SU':
        passed()
    elif input("你正在访问锁定功能，请输入管理员密码: ") == 'kill name':
        acc = 'SU'
        passed()

def 数字游戏():
    saves = 0
    saveb = 100
    bet = input('请输入难度: ')
    print('''游戏时间!!! 规则:
1_你需要猜我想的一个1到100的数
2_if you guessed my number correctly, then you won.
3_if you guess my number %s times incorrectly, then you lose.'''%bet)
    beat = int(bet)
    q1 = math.ceil(random.random() * 100)
    for i in range(1,beat + 1) :
        a1 = input('please enter the number you guessed: ')
        a1_i = int(a1)
        if a1_i == q1 :
            print('Congratulations! you win!')
            return True
        else :
            if a1_i > q1 :
                saveb = a1_i
            elif a1_i < q1 :
                saves = a1_i
            print("you lost this round, don't be discouraged. the right number is between %d and %d"%(saves,saveb))
    print('you lost!')

def Lightning_history() :
    print(Lin1)
    print(Lin1_1)
    print(Lin1_2)
    print(Lin1_3)
    print(Lin1_4)
    print(Lin2)
    print(Lin2_1)
    print(Lino1)
    print(Lino2)

def Lightning

def account_info() :
    def go():
        print('Verified passed')
        people = input('Who do you want to inquire about(account name): ')
        if people in database2 :
            print('address:',database2[people]['address'],'password:',database2[people]['password'])
        else:
            print("Lightning database haven't this person.")
    if acc != 'SU' :
        if input("You're accessing the lockout feature, enter the superuser's password: ") == 'kill name' :
            acc = 'SU'
            go()
        else:
            print('Permission denied')
    else:
        go()

def judge_type():
    print(judge_(input("enter value: "))[0])
def judge_(value):
    try:
        tp = eval(value)
        tj = type(tp).__name__
        return (tj,tp)
    except:
        return ('str',value)

def f(n) :
    if n == 1 :
        return 1
    elif n == 2 :
        return 1
    else :
        return (f(n - 1) + f(n - 2))

def fibonacci() :
    sa = []
    for fkey in range(1,int(input('please enter upper limit: ')) + 1) :
        sa.append(f(fkey))
    print(sa)

def go(seq,flag,script):
    if flag in seq :exec(script)
    else:print('no such goal')

def search() :
    while True:
        se = input('please enter sequence(list,dict,tuple,int,finish:finish): ')
        if se == 'finish':
            print('finish')
            break
        fla = input('please enter goal: ')
        string_e = 'print(seq.index(flag) + 1)'
        tup = judge_(se)
        sec = tup[0]
        seq = tup[1]
        flag = judge_(fla)[1]
        if sec == 'list' or sec == 'tuple' :
            go(seq,flag,string_e)
        elif sec == 'int' :
            go(list(str(seq)),str(flag),string_e)
        elif sec == 'dict':
            print(seq[flag])
        else :
            print('TypeError')

def judge_rating():
    s = {}
    pr = {}
    down = input("Please enter lower limit's name: ")
    for i in range(1,eval(input('Please enter the number of rating levels: ')) + 1):
        a = input(f"please enter the name of level {i}: ")
        s[a] = eval(input("please enter this level's score: "))
    for key in range(1,eval(input('Please enter rating times: ')) + 1):
        number = eval(input('Please enter rating number: '))
        if number < list(s.values())[0]:
            save = down
        else:
            for level in s:
                if number > s[level]:
                    save = level
                    continue
                elif number == s[level]:
                    save = level
                    break
        pr[number] = save
    print(pr)


# draw main game board
def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'light gray', [
                             600 - (column * 200), row * 100, 100, 100])
        else:
            pygame.draw.rect(screen, 'light gray', [
                             700 - (column * 200), row * 100, 100, 100])
        pygame.draw.rect(screen, 'gray', [0, 800, WIDTH, 100])
        pygame.draw.rect(screen, 'gold', [0, 800, WIDTH, 100], 5)
        pygame.draw.rect(screen, 'gold', [800, 0, 200, HEIGHT], 5)
        status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                       'Black: Select a Piece to Move!', 'Black: Select a Destination!']
        screen.blit(big_font.render(
            status_text[turn_step], True, 'black'), (20, 820))
        for i in range(9):
            pygame.draw.line(screen, 'black', (0, 100 * i), (800, 100 * i), 2)
            pygame.draw.line(screen, 'black', (100 * i, 0), (100 * i, 800), 2)
        screen.blit(medium_font.render('FORFEIT', True, 'black'), (810, 830))

# draw pieces onto board
def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(
                white_pawn, (white_locations[i][0] * 100 + 22, white_locations[i][1] * 100 + 30))
        else:
            screen.blit(white_assist[index], (white_locations[i]
                        [0] * 100 + 10, white_locations[i][1] * 100 + 10))
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'red', [white_locations[i][0] * 100 + 1, white_locations[i][1] * 100 + 1,
                                                 100, 100], 2)

    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(
                black_pawn, (black_locations[i][0] * 100 + 22, black_locations[i][1] * 100 + 30))
        else:
            screen.blit(black_assist[index], (black_locations[i]
                        [0] * 100 + 10, black_locations[i][1] * 100 + 10))
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue', [black_locations[i][0] * 100 + 1, black_locations[i][1] * 100 + 1,
                                                  100, 100], 2)


# function to check all pieces valid options on board
def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range((len(pieces))):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        elif piece == 'king':
            moves_list = check_king(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list


# check king valid moves
def check_king(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    # 8 squares to check for kings, they can go one square any direction
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0),
               (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list


# check queen valid moves
def check_queen(position, color):
    moves_list = check_bishop(position, color)
    second_list = check_rook(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list


# check bishop moves
def check_bishop(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    for i in range(4):  # up-right, up-left, down-right, down-left
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append(
                    (position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list


# check rook moves
def check_rook(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    for i in range(4):  # down, up, right, left
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append(
                    (position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list


# check valid pawn moves
def check_pawn(position, color):
    moves_list = []
    if color == 'white':
        if (position[0], position[1] + 1) not in white_locations and \
                (position[0], position[1] + 1) not in black_locations and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        if (position[0], position[1] + 2) not in white_locations and \
                (position[0], position[1] + 2) not in black_locations and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        if (position[0] + 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] - 1, position[1] + 1))
    else:
        if (position[0], position[1] - 1) not in white_locations and \
                (position[0], position[1] - 1) not in black_locations and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] - 2) not in white_locations and \
                (position[0], position[1] - 2) not in black_locations and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list


# check valid knight moves
def check_knight(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    # 8 squares to check for knights, they can go two squares in one direction and one in another
    targets = [(1, 2), (1, -2), (2, 1), (2, -1),
               (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list

black_options = check_options(black_pieces, black_locations, 'black')
white_options = check_options(white_pieces, white_locations, 'white')
# check for valid moves for just selected piece
def check_valid_moves():
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options


# draw valid moves on screen
def draw_valid(moves):
    if turn_step < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(
            screen, color, (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50), 5)

def draw_captured():
    for i in range(len(captured_pieces_white)):
        captured_piece = captured_pieces_white[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_black_assist[index], (825, 5 + 50 * i))
    for i in range(len(captured_pieces_black)):
        captured_piece = captured_pieces_black[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_white_assist[index], (925, 5 + 50 * i))

def draw_check():
    if turn_step < 2:
        if 'king' in white_pieces:
            king_index = white_pieces.index('king')
            king_location = white_locations[king_index]
            for i in range(len(black_options)):
                if king_location in black_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark red', [white_locations[king_index][0] * 100 + 1,
                                                              white_locations[king_index][1] * 100 + 1, 100, 100], 5)
    else:
        if 'king' in black_pieces:
            king_index = black_pieces.index('king')
            king_location = black_locations[king_index]
            for i in range(len(white_options)):
                if king_location in white_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark blue', [black_locations[king_index][0] * 100 + 1,
                                                               black_locations[king_index][1] * 100 + 1, 100, 100], 5)


def draw_game_over():
    pygame.draw.rect(screen, 'black', [200, 200, 400, 70])
    screen.blit(font.render(
        f'{winner} won the game!', True, 'white'), (210, 210))
    screen.blit(font.render(f'Press ENTER to Restart!',
                True, 'white'), (210, 240))
def sstr(li):
    saver = ''
    for i in li:
        saver += i
    return saver


def LevoOS1_new() :
    global acc,syss
    database4 = {}
    languages = ['English']
    passwd_list = {}
    register = int(input("please enter your physical hard drive's capacity(GB): "))
    while True :
        Key = input('please enter your PassKey :')
        if Key == '114514-LEVOSK':
            if acc == 'SU' :
                print('Welcome,SU')
                break
            elif input('''you are using super-key,please enter super-user's password: ''') == '20121129':
                acc = 'SU'
                print('Welcome,SU')
                break
            else:
                print('Super-Key:permission denied!')
        elif Key in database3 :
            print('Verified passed')
            break
        else :
            print('Permission denied,Try again')
    while True :
        disk1 = input(f'''
first:
please choose your virtual disk that you want to install LevoOS:
{database4}
No virtual disk? Register one!(press 1): ''')
        if disk1 == '1' :
            while True :
                register1 = input("please enter the virtual disk's name: ")
                register2 = int(input("please enter the virtual disk's capacity(GB): "))
                if register2 <= register - 10 :
                    print('registering...')
                    database4[register1] = register2
                    print('Register successful!')
                    break
                else :
                    print('Disk full!')
        elif disk1 in database4 :
            disk2 = database4[disk1]
            print('virtual disk select successful!')
            break
        else:
            print('no such virtual disk!')
    passwd_list['SU'] = input(f'''
second:
please set superuser's pasword : ''')
    while True :
        language = input(f'''
third:
{languages}
please choose language:
''')
        if language in languages :
            print('language select successful!')
            break
        else:
            print('no such availble language!')
    passwd_list['Adminstrator'] = input('''
fourth:
please set user adminstrator's password:''')
    print('password set successful!')
    syss[input('''
last one:
    time.sleep(1)
please set new system's name:''')] = {'disk':disk2,'language':language,'passwd':passwd_list,'path':{'logs_Adminstrator_w-':{'export.txt':'''
Group:
Adminstrator:Adminstrator
user:Adminstrator
Suffix:
.txt:text editer;'''},'Adminstrator_Adminstrator_wr':{},'media_Adminstrator_rr':{}}}
    print('system create finish')

def LevoOS1_log_in():
    while True:
        sys_c = input(f'''
{list(syss.keys())}
please select system: ''')
        if sys_c in syss.keys() :
            print('system select successful!')
            break
        else:
            print('no such system!')
            print('system launching...')
    sys = syss[sys_c]
    disk = sys['disk']
    passwd = sys['passwd']
    path = sys['path']
    while True :
        time.sleep(1)
        if sys['language'] == 'English':
            while True :
                user = input(f'''
{passwd.keys()}
please choose user:''')
                if user in passwd.keys():
                    while True:
                        passwdin = input('password:')
                        if passwdin == passwd[user]:
                            print('welcome,%s'%user)
                            break
                        else:
                            print('password wrong!')
                    break
                else:
                    print('no such user!')
                    time.sleep(1)
            mode = input('please choose mode(CLI:1,GUI:2): ')
            if mode == '1':
                shell(sys_c,path)
            else:
                print("sorry,no feature!")
                guide()

def guide():
    pass

def log_off():
    global ca
    ca = 1

def pather_count(pather,available_path):
    for pathc in pather:
        available_path = available_path[pathc]
    availble_path = str(availble_path.keys())
    del availble_path[:8]
    out = availble_path.split('_')
    return available_path

def shell(sys_c,available_path,user = 'Adminstrator') :
    print(f'CLI interface from {sys_c}/{user}')
    path = '/'
    pather = []
    dir_data = pather_count(pather,available_path)
    while True :
        std_in = input(f'{user}@{sys_c}:{path}$ ')
        std_in_s = list(std_in)
        if 'cd' in std_in:
            del std_in_s[:3]
            if sstr(std_in_s) == '..' :
                pather.pop()
                dir_data = pather_count(pather,available_path)
            else:
                path += sstr(std_in_s)
                pather.append(sstr(std_in_s))
                dir_data = pather_count(pather,available_path)
        elif 'nano' in std_in:
            del std_in_s[:5]
            dir_data
        elif 'exit' in std_in:
            print('thanks for use LevoOS v1.0.0(dev) CLI, goodbye!')
            time.sleep(1)
            break
        elif 'ls' in std_in:
            del std_in_s[:2]
            if std_in_s:
                pass
            else:
                print(dir_data)
        elif 'mv' in std_in:
            del std_in_s[:3]
        elif 'mkdir' :
            del std_in_s[:6]
        elif 'mkusr' :
            del std_in_s[:6]
        elif 'chpms' :
            del std_in_s[:6]
        elif 'dlusr' :
            del std_in_s[:6]
        else:
            print(f'{std_in} is not an availble syntax of LevoCLI v1.0.0(dev)')

def chess2_black():
    run = True
    while run:
        timer.tick(fps)
        if counter < 30:
            counter += 1
        else:
            counter = 0
        screen.fill('dark gray')
        draw_board()
        draw_pieces()
        draw_captured()
        draw_check()
        if selection != 100:
            valid_moves = check_valid_moves()
            draw_valid(valid_moves)
        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
                x_coord = event.pos[0] // 100
                y_coord = event.pos[1] // 100
                click_coords = (x_coord, y_coord)
                if turn_step <= 1:
                    recv = eval(str(s1.recv(1024)))
                    if recv == 'win'.encode('utf-8'):
                        winner = 'black'
                    else:                
                        white_locations[recv[0]] = recv[1]
                        if recv[1] in black_locations:
                            black_piece = black_locations.index(click_coords)
                            captured_pieces_white.append(black_pieces[black_piece])
                            if black_pieces[black_piece] == 'king':
                                winner = 'white'
                            black_pieces.pop(black_piece)
                            black_locations.pop(black_piece)
                        black_options = check_options(black_pieces, black_locations, 'black')
                        white_options = check_options(white_pieces, white_locations, 'white')
                        turn_step = 2
                        selection = 100
                        valid_moves = []
                if turn_step > 1:#黑方
                    if click_coords == (8, 8):
                        winner = 'white'
                        s1.send('win'.encode('utf-8'))
                    else :
                        if click_coords in black_locations:
                            selection = black_locations.index(click_coords)
                            if turn_step == 2:
                                turn_step = 3
                        if click_coords in valid_moves and selection != 100:
                            black_locations[selection] = click_coords
                            s1.send(str((selection,click_coords)).encode('utf-8'))
                            if click_coords in white_locations:
                                white_piece = white_locations.index(click_coords)
                                captured_pieces_black.append(white_pieces[white_piece])
                                if white_pieces[white_piece] == 'king':
                                    winner = 'black'
                                white_pieces.pop(white_piece)
                                white_locations.pop(white_piece)
                            black_options = check_options(
                                black_pieces, black_locations, 'black')
                            white_options = check_options(
                                white_pieces, white_locations, 'white')
                            turn_step = 0
                            selection = 100
                            valid_moves = []
            if event.type == pygame.KEYDOWN and game_over:
                if event.key == pygame.K_RETURN:
                    game_over = False
                    winner = ''
                    white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                    'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                    white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                    black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                    'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                    black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                    (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                    captured_pieces_white = []
                    captured_pieces_black = []
                    turn_step = 0
                    selection = 100
                    valid_moves = []
                    black_options = check_options(
                        black_pieces, black_locations, 'black')
                    white_options = check_options(
                        white_pieces, white_locations, 'white')
        if winner != '':
            game_over = True
            draw_game_over()
        pygame.display.flip()
    pygame.quit()
def chess2_white():
    while run:
        timer.tick(fps)
        if counter < 30:
            counter += 1
        else:
            counter = 0
        if selection != 100:
            valid_moves = check_valid_moves()
            draw_valid(valid_moves)
        screen.fill('dark gray')
        draw_board()
        draw_pieces()
        draw_captured()
        draw_check()
        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
                x_coord = event.pos[0] // 100
                y_coord = event.pos[1] // 100
                click_coords = (x_coord, y_coord)
                if turn_step <= 1:#白方
                    if click_coords == (8, 8) or click_coords == (9, 8):
                        winner = 'black'
                        s2.send('win'.encode('utf-8'))
                    else :
                        if click_coords in white_locations:
                            selection = white_locations.index(click_coords)
                            if turn_step == 0:
                                turn_step = 1
                        if click_coords in valid_moves and selection != 100:
                            white_locations[selection] = click_coords
                            s2.send(str((selection,click_coords)).encode('utf-8'))
                            if click_coords in black_locations:
                                black_piece = black_locations.index(click_coords)
                                captured_pieces_white.append(black_pieces[black_piece])
                                if black_pieces[black_piece] == 'king':
                                    winner = 'white'
                                black_pieces.pop(black_piece)
                                black_locations.pop(black_piece)
                            black_options = check_options(black_pieces, black_locations, 'black')
                            white_options = check_options(white_pieces, white_locations, 'white')
                            turn_step = 2
                            selection = 100
                            valid_moves = []
                        draw_pieces()
                        draw_captured()
                        draw_check()
                if turn_step > 1:
                    recv = eval(str(s2.recv(1024)))
                    if recv == 'win'.encode('utf-8') :
                        winner = 'white'
                    else :
                        black_locations[recv[0]] = recv[1]
                        if recv[1] in white_locations:
                            white_piece = white_locations.index(click_coords)
                            captured_pieces_black.append(white_pieces[white_piece])
                            if white_pieces[white_piece] == 'king':
                                winner = 'black'
                            white_pieces.pop(white_piece)
                            white_locations.pop(white_piece)
                        black_options = check_options(black_pieces, black_locations, 'black')
                        white_options = check_options(white_pieces, white_locations, 'white')
                        turn_step = 0
                        selection = 100
                        valid_moves = []
            if event.type == pygame.KEYDOWN and game_over:
                if event.key == pygame.K_RETURN:
                    game_over = False
                    winner = ''
                    white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                    'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                    white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                    black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                    'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                    black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                    (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                    captured_pieces_white = []
                    captured_pieces_black = []
                    turn_step = 0
                    selection = 100
                    valid_moves = []
                    black_options = check_options(
                        black_pieces, black_locations, 'black')
                    white_options = check_options(
                        white_pieces, white_locations, 'white')
        if winner != '':
            game_over = True
            draw_game_over()
        pygame.display.flip()
    pygame.quit()

def identify(external):
    pass

def chess3():
    black_options = check_options(black_pieces, black_locations, 'black')
    white_options = check_options(white_pieces, white_locations, 'white')
    run = True
    ex = input('Please enter chess Notation(Such as 1_d4 d5): ')
    while run:
        timer.tick(fps)
        if counter < 30:
            counter += 1
        else:
            counter = 0
        screen.fill('dark gray')
        draw_board()
        draw_pieces()
        draw_captured()
        draw_check()
        if selection != 100:
            valid_moves = check_valid_moves()
            draw_valid(valid_moves)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
                x_coord = event.pos[0] // 100
                y_coord = event.pos[1] // 100
                click_coords = (x_coord, y_coord)
                if turn_step <= 1:
                    if click_coords in white_locations:
                        selection = white_locations.index(click_coords)
                        if turn_step == 0:
                            turn_step = 1
                    if click_coords in valid_moves and selection != 100:
                        white_locations[selection] = click_coords
                        if click_coords in black_locations:
                            black_piece = black_locations.index(click_coords)
                            captured_pieces_white.append(black_pieces[black_piece])
                            if black_pieces[black_piece] == 'king':
                                winner = 'white'
                            black_pieces.pop(black_piece)
                            black_locations.pop(black_piece)
                        black_options = check_options(
                            black_pieces, black_locations, 'black')
                        white_options = check_options(
                            white_pieces, white_locations, 'white')
                        turn_step = 2
                        selection = 100
                        valid_moves = []
                if turn_step > 1:
                    if click_coords in black_locations:
                        selection = black_locations.index(click_coords)
                        if turn_step == 2:
                            turn_step = 3
                    if click_coords in valid_moves and selection != 100:
                        black_locations[selection] = click_coords
                        if click_coords in white_locations:
                            white_piece = white_locations.index(click_coords)
                            captured_pieces_black.append(white_pieces[white_piece])
                            if white_pieces[white_piece] == 'king':
                                winner = 'black'
                            white_pieces.pop(white_piece)
                            white_locations.pop(white_piece)
                        black_options = check_options(
                            black_pieces, black_locations, 'black')
                        white_options = check_options(
                            white_pieces, white_locations, 'white')
                        turn_step = 0
                        selection = 100
                        valid_moves = []
            if event.type == pygame.KEYDOWN and game_over:
                if event.key == pygame.K_RETURN:
                    game_over = False
                    winner = ''
                    white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                    'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                    white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                    black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                    'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                    black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                    (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                    captured_pieces_white = []
                    captured_pieces_black = []
                    turn_step = 0
                    selection = 100
                    valid_moves = []
                    black_options = check_options(
                        black_pieces, black_locations, 'black')
                    white_options = check_options(
                        white_pieces, white_locations, 'white')
        if winner != '':
            game_over = True
            draw_game_over()
        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__' :
    import B
    ll = int(input('please shoose language(English:1,Chinese:2): '))
    while True:
        try:
            if ll == 1 :
                launch = input('versions list: A B C   please choose version: ')
                data = jt['English']
                for key in data:
                    value = data[key]
                    if ca == 0 and launch == key:
                        while True:
                            B.judge(value)
                            if ca == 1:
                                use = 1
                                ca = 0
                                break
            elif ll == 2 :
                launch = input('版本列表：A B C   请选择版本：')
                data = jt['Chinese']
                for key in data:
                    value = data[key]
                    if ca == 0 and launch == key:
                        while True:
                            B.judge(value)
                            if ca == 1:
                                use = 1
                                ca = 0
                                break
            else :
                print('unavailble language')
            if use == 1 :
                if ll == 1:
                    print('thanks for use,goodbye!')
                else:
                    print('谢谢使用，再见！')
                break
            else:
                if ll == 1:
                    print('unavailble version')
                else:
                    print('不存在的版本')
        except:
            if ll == 1:
                print(f'Sorry,the program went wrong. it will turn back automatically in 2 second.')
            else:
                print('抱歉，程序发生了错误。两秒后返回。')
            time.sleep(2)

def lifegame3():
    pass

def CLI2():
    print('Please')

def SCP_Foundation():
    persion = {'O5':[100,None,None,[]],
            'S-1':[100,None,None,[]],'S-2':[100,None,None,[]],
            'D-1':[100,None,None,[]],'D-2':[100,None,None,[]],'D-3':[100,None,None,[]],
            'SCP-096':[True,2500,600],'SCP-173':[True,4000,750],'SCP-079':[True,1,100]}
    Alpha = 90
    detonate = False

    def getrandom(times):
        return math.ceil(random.random() * times)

    def counter():
        while count != 0:
            time.sleep(1)
            count -= 1

    def Alpha_bomb():
        if Alpha == 90:
            print('C.A.S.S. : Alpha-Warhead detonation sequence been eneaged,The underground facility will be detonated in T Minus %d seconds.'%Alpha)
        else:
            print("C.A.S.S. : Detonation sequence resumed T-minus 60 seconds.")
        for i in range(Alpha):
            time.sleep(1)
            Alpha -= 1
            if detonate == False:
                print("C.A.S.S. : Detonation canceled,restarting systeams")
                return

    def load_map():
        pass

    def S():
        pass

    def D():
        pass
        
    def SCP_173():
        pass
        
    def SCP_079():
        pass
        
    def SCP_096():
        pass

    def O5():
        pass

    def MTF():
        pass

    def MTF_p():
        print("     ----------")
        print("     你是 MTF队员")
        print("     ----------")
        print("保护所有人员逃离Site-02")
        print("    杀死所有的SCP")

    def D_p():
        print("     ----------")
        print("     你是 D级人员")
        print("     ----------")
        print("和'MTF'一起逃离Site-02")

    def O5_p():
        print("     ----------")
        print("     你是 O5人员")
        print("     ----------")
        print("操控所有设备杀死所有的SCP")

    def S_p():
        print("    ---------")
        print("    你是 科学家")
        print("    ---------")
        print("和'MTF'一起逃离Site-02")

    def SCP_096_p():
        print("-----------")
        print("你是 SCP-096")
        print("-----------")
        print(" 杀死所有人")

    def SCP_079_p():
        print("conneting inet...")
        time.sleep(0.8)
        print("ping 192.168.0.1")
        time.sleep(0.5)
        for i in range(3):
            print("    64 Byte from 192.168.0.1")
            time.sleep(0.5)
        print("^C")
        print("--- 192.168.0.1 ping statistics ---") 
        print("3 packets transmitted, 3 packets received, 0.0% packet loss")
        time.sleep(0.75)
        print("rdp site-02@192.168.0.1 -i RDP_breaker")
        time.sleep(0.5)
        print("conneting...")
        time.sleep(1)
        print("password:")
        time.sleep(0.75)
        print("RDP Warning:Detected hack,RDP has been forcibly clo")
        print("RDP_breaker:Successfully hacked into the RDP network bridge of 'SCP-079'(You) and 'Site-02'(Objects to be hacked in)")
        time.sleep(1)
        print("RDP_breaker:Successfully hacked into the terminal network of 'Site-02' with RDP")
        print("RDP_breaker:turning to RDP's certificate and connect to 'Site-02'...")
        time.sleep(1)
        print("RDP(RDP_breaker):Successfully connect RDP into 'Site-02'")
        for i in range(20):
            print("")
        print("-----------")
        print("你是 SCP-079")
        print("-----------")
        print(" 杀死所有人")
        print("C.A.S.S.I.E. : Attention,all persionnel,the lightning containment will be lock down in T Minus 10 minute.All creatrue will be remove.please exit this area!")
        

    def SCP_173_p():
        print("-----------")
        print("你是 SCP-173")
        print("-----------")
        print(" 杀死所有人")

    def load(player):
        if player != 'O5':
            O51 = multiprocessing.Process(target = O5,args = ())
            O51.start()
        if player != 'D':
            D1 = multiprocessing.Process(target = D,args = ())
            D1.start()
        if player != 'S':
            S = multiprocessing.Process(target = S,args = ())
            S.start()
        if player != '79':
            SCP_079 = multiprocessing.Process(target = SCP_079,args = ())
            SCP_079.start()
        if player != '96':
            SCP_096 = multiprocessing.Process(target = SCP_096,args = ())
            SCP_096.start()
        if player != '173':
            SCP_173 = multiprocessing.Process(target = SCP_173,args = ())
            SCP_173.start()
        if player != 'MTF':
            MTF = multiprocessing.Process(target = MTF,args = ())

    def launcher():
        mode = input("Please enter mode(Internet:1,local:2):")
        if mode == 2:
            player = input("role list:\nMTF:MTF\nClass-D:D\nO5 personnel:O5\nscientist:S\nSCP-096:96\nSCP-079:79\nSCP-173:173\nPlease enter the role you want to play: ")

e = True
sheetl = [[None,]]
sheet = ''

def add_column():
    global sheetl
    for i in sheetl:
        for j in range(input('add ? column:')):i.append(None)

def add_line():
    global sheetl
    for i in range(int(input('add ? line:'))):
        sheetl.append([])

def assignment():
    global sheetl
    sheetl[input('line:') - 1][input('column:') - 1] = input('value:')

def exit():
    global e
    print(sheet)
    e = False

while e:
    for i in sheetl:
        for j in sheetl:sheet += ('|' + str(j))
        sheet += '|\n'
    exec(input(f'''{sheet}
exit   add_column   add_line   assignment   colume_assignment
operation:'''))