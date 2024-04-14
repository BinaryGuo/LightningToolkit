import pygame,math,time,random,PIL,matplotlib.pyplot as plt;#from C import *

vd = {(0, 0): (10, 10, 92, 125), (1, 0): (108, 10, 190, 125), (2, 0): (206, 10, 288, 125), (3, 0): (304, 10, 386, 125), (4, 0): (402, 10, 484, 125), (5, 0): (500, 10, 582, 125), (6, 0): (598, 10, 680, 125), (7, 0): (696, 10, 778, 125), (8, 0): (794, 10, 876, 125), (9, 0): (892, 10, 974, 125), (10, 0): (990, 10, 1072, 125), (11, 0): (1088, 10, 1170, 125), (12, 0): (1186, 10, 1268, 125), (0, 1): (10, 139, 92, 254), (1, 1): (108, 139, 190, 254), (2, 1): (206, 139, 288, 254), (3, 1): (304, 139, 386, 254), (4, 1): (402, 139, 484, 254), (5, 1): (500, 139, 582, 254), (6, 1): (598, 139, 680, 254), (7, 1): (696, 139, 778, 254), (8, 1): (794, 139, 876, 254), (9, 1): (892, 139, 974, 254), (10, 1): (990, 139, 1072, 254), (11, 1): (1088, 139, 1170, 254), (12, 1): (1186, 139, 1268, 254), (0, 2): (10, 268, 92, 383), (1, 2): (108, 268, 190, 383), (2, 2): (206, 268, 288, 383), (3, 2): (304, 268, 386, 383), (4, 2): (402, 268, 484, 383), (5, 2): (500, 268, 582, 383), (6, 2): (598, 268, 680, 383), (7, 2): (696, 268, 778, 383), (8, 2): (794, 268, 876, 383), (9, 2): (892, 268, 974, 383), (10, 2): (990, 268, 1072, 383), (11, 2): (1088, 268, 1170, 383), (12, 2): (1186, 268, 1268, 383), (0, 3): (10, 397, 92, 512), (1, 3): (108, 397, 190, 512), (2, 3): (206, 397, 288, 512), (3, 3): (304, 397, 386, 512), (4, 3): (402, 397, 484, 512), (5, 3): (500, 397, 582, 512), (6, 3): (598, 397, 680, 512), (7, 3): (696, 397, 778, 512), (8, 3): (794, 397, 876, 512), (9, 3): (892, 397, 974, 512), (10, 3): (990, 397, 1072, 512), (11, 3): (1088, 397, 1170, 512), (12, 3): (1186, 397, 1268, 512),(0, 4): (10, 526, 92, 641),(1, 4): (108, 526, 190, 641)}
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
day_ending = ['st','nd','rd'] + 17* ['th'] + ['st','nd','rd'] + 8* ['th']
database1 = [['xyl','1038'],['SU','kill name'],['yzb','2835'],['wyj','3158'],['yjy','5849']]
database2 = {'SU':{'address':'second floor right room','password':'kill name'},'xyl':{'address':'second floor right room','password':'1038'},'yzb':{'address':'second floor left room','password':'2835'},'wyj':{'address':'second floor left,right room','password':'3158'},'yjy':{'address':'first floor left room','password':'5849'}}
chancer = 1
ca = 0
chance = 3
chancers = 10
use = 0
Lversions = ['A','B']
Lin1 = '2023年:'
Lin1_1 = '11月1日,我创建了Lightning A Beta。(10日后为stable)'
Lin1_2 = '11月5日,Lightning B Alpha 出现了。(45日后为Beta,52日后为Stable)'
Lin1_3 = '11月19日,Lightning C Alpha 出现了。'
Lin1_4 = '停更了好长时间,终于————(12月20日)Lightning B Beta 出现了。'
Lin1_5 = '中间整了好多东西,例如G-language/chess_local/chess_server/chess_client/file_editer等,除G-language外,全部并入了Lightning Tools'
Lin1_6 = 'G-language 并入 Lightning Tools,至此Lightning体系完善。'
jt = {'English':{'A' : '''
1-format_date   2-dice   3-timer_foward   4-timer_back   5-calculator
please choose program: ''',
      'B' : '''
1-format_date   2-dice   3-timer_foward   4-timer_back   5-calculator   6-text_box   7-joker1   8-number_game   9-account_info   10-Lightning_history
11-log_off   12-Lightning_info   13-joker2   14-fibonacci   15-taxas1   16-judge_rating   17-judge_type   18-release_note   19-chess1
please choose program: '''}}

def release_note():
    print('''
add:6-text_box   7-joker1   8-number_game   9-account_info   10-Lightning_history   11-log_off   12-Lightning_info   13-joker2   14-fibonacci   15-taxas1   16-judge_rating   17-judge_type   18-release_note   19-chess1
success:calculator.multistep''')

def Lightning_info():
    print('Version B, UnDebug:False')

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

def format_date() :
    year = input('enter year: ')
    month = input('enter month: ')
    day = input('enter day: ')
    month_int = int(month)
    day_int = int(day)
    Month = months[month_int -1]
    Day = day + day_ending[day_int -1]
    print(Month + ' ' + Day + ' , ' + year)

def dice() :
    ttti = input('please enter mode(every random input:1, all random one input:2): ')
    tti = input('please enter random times: ')
    ttt = int(ttti)
    tt = int(tti)
    if ttt == 1 :
        for i in range(tt) :
            ti1 = input("Please enter the number of faces on the dice: ")
            t1 = int(ti1)
            dice1 = math.ceil(random.random()*t1)
            print(dice1)
    else :
        tttti = input('please enter displar mode(list:1, pile up:2): ')
        ti2 = input("please enter times(number): ")
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

def timer_foward() :
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

def timer_back() :
    time1 = input('please enter seconds(s): ')
    time3 = int(time1)
    while time3 != 0 :
        time.sleep(1)
        time3 -= 1
        print("%d second(s)"%time3)

def calculator() :
    inm = input('please enter formula: ')
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

def heart3(a_people_card):
    return "heart_3" in a_people_card

def counter(a_people_card):
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

def joker1() :
    all_cards = card()
    all_player_cards, cover_cards = deal(all_cards)
    for player in all_player_cards:
        this_player_cards = all_player_cards[player]
        value_dict = counter(this_player_cards)
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
        value_dict = counter(this_player_cards)
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

def text_box() :
    t1 = input('please enter the text: ')
    t1_l = len(t1)
    box = t1_l + 10
    print('+' + (box - 2) * '-' + '+')
    print('|' + (box - 2) * ' ' + '|')
    print('|' + 4 * ' ' + t1 + 4 * ' ' + '|')
    print('|' + (box - 2) * ' ' + '|')
    print('+' + (box - 2) * '-' + '+')

def number_game():
    saves = 0
    saveb = 100
    bet = input('please enter difficulty: ')
    print('''It'gametime!!! the rules:
1_You need guess a number in my head between 1 and 100.
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
    print(Lin1_5)

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

def has_pair(hand):
    values = [card[1] for card in hand]
    value_counts = {value: values.count(value) for value in values}
    return 2 in value_counts.values()

def has_two_pair(hand):
    values = [card[1] for card in hand]
    value_counts = {value: values.count(value) for value in values}
    return list(value_counts.values()).count(2) == 2

def has_three_of_a_kind(hand):
    values = [card[1] for card in hand]
    value_counts = {value: values.count(value) for value in values}
    return 3 in value_counts.values()

def has_straight(hand):
    values = [["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"].index(card[1]) for card in hand]
    values.sort()
    return len(set(values)) == 5 and (max(values) - min(values) == 4)

def has_flush(hand):
    suits = [card[0] for card in hand]
    return len(set(suits)) == 1

def has_full_house(hand):
    return has_pair(hand) and has_three_of_a_kind(hand)

def has_four_of_a_kind(hand):
    values = [card[1] for card in hand]
    value_counts = {value: values.count(value) for value in values}
    return 4 in value_counts.values()

def has_straight_flush(hand):
    return has_straight(hand) and has_flush(hand)

def taxas1():
    save = {}
    suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck = [(suit, rank) for suit in suits for rank in ranks] * 2
    random.shuffle(deck)
    num_players = int(input("Enter the number of players: "))
    while num_players > len(deck) // 3:
        deck += [(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(deck)
    players = [f"Player{i+1}" for i in range(num_players)]
    cover_cards = [deck.pop() for _ in range(5)]
    for player in players:
        player_cards = [deck.pop() for _ in range(2)]
        print(f"{player}'s cards are {player_cards}")
        player_cards.extend(cover_cards)
        save[player] = player_cards
    print(f'Cover cards: {cover_cards}')
    for player, hand in save.items():
        print(f"{player}'s hand is {hand}")
        best_score = 0
        if has_pair(hand):
            best_score = max(best_score, 1)
        if has_two_pair(hand):
            best_score = max(best_score, 2)
        if has_three_of_a_kind(hand):
            best_score = max(best_score, 3)
        if has_straight(hand):
            best_score = max(best_score, 4)
        if has_flush(hand):
            best_score = max(best_score, 5)
        if has_full_house(hand):
            best_score = max(best_score, 6)
        if has_four_of_a_kind(hand):
            best_score = max(best_score, 7)
        if has_straight_flush(hand):
            best_score = max(best_score, 8)
        print(f"{player}'s best score is {best_score}")
def chess1():
    # Initialising pygame module
    pygame.init()

    # Setting Width and height of the Chess Game screen
    WIDTH = 1000
    HEIGHT = 800

    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption('Two-Player Chess Game')

    font = pygame.font.Font('freesansbold.ttf', 20)
    medium_font = pygame.font.Font('freesansbold.ttf', 40)
    big_font = pygame.font.Font('freesansbold.ttf', 50)

    timer = pygame.time.Clock()
    fps = 60

    # game variables and images
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

    # 0 - whites turn no selection: 
    # 1-whites turn piece selected: 
    # 2- black turn no selection, 
    # 3 - black turn piece selected
    turn_step = 0
    selection = 100
    valid_moves = []

    # load in game piece images (queen, king, rook, bishop, knight, pawn) x 2
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

    white_images = [white_pawn, white_queen, white_king,
                    white_knight, white_rook, white_bishop]
    small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small,
                        white_rook_small, white_bishop_small]

    black_images = [black_pawn, black_queen, black_king,
                    black_knight, black_rook, black_bishop]
    small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small,
                        black_rook_small, black_bishop_small]

    piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

    # check variables/ flashing counter
    counter = 0
    winner = ''
    game_over = False


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
                screen.blit(white_images[index], (white_locations[i]
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
                screen.blit(black_images[index], (black_locations[i]
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


    # draw captured pieces on side of screen
    def draw_captured():
        for i in range(len(captured_pieces_white)):
            captured_piece = captured_pieces_white[i]
            index = piece_list.index(captured_piece)
            screen.blit(small_black_images[index], (825, 5 + 50 * i))
        for i in range(len(captured_pieces_black)):
            captured_piece = captured_pieces_black[i]
            index = piece_list.index(captured_piece)
            screen.blit(small_white_images[index], (925, 5 + 50 * i))


    # draw a flashing square around king if in check 将军
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


    # main game loop
    black_options = check_options(black_pieces, black_locations, 'black')
    white_options = check_options(white_pieces, white_locations, 'white')
    run = True
    while run:
        timer.tick(fps)
        if counter < 30:
            counter += 1
        else:
            counter = 0
        screen.fill('dark gray')
        draw_board() # 棋盘
        draw_pieces() # 活的子
        draw_captured() # 死的子
        draw_check() #将军
        if selection != 100:
            valid_moves = check_valid_moves()
            draw_valid(valid_moves)
        # event handling 事件处理器
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
                x_coord = event.pos[0] // 100
                y_coord = event.pos[1] // 100
                click_coords = (x_coord, y_coord) # coords指的是你按什么格子
                if turn_step <= 1:
                    if click_coords == (8, 8) or click_coords == (9, 8):
                        winner = 'black'
                    if click_coords in white_locations:
                        selection = white_locations.index(click_coords)
                        if turn_step == 0:
                            turn_step = 1
                    if click_coords in valid_moves and selection != 100:
                        white_locations[selection] = click_coords #走
                        #send message()
                        if click_coords in black_locations: #吃
                            black_piece = black_locations.index(click_coords)
                            captured_pieces_white.append(black_pieces[black_piece])
                            if black_pieces[black_piece] == 'king':
                                winner = 'white'
                            black_pieces.pop(black_piece)
                            black_locations.pop(black_piece)
                        black_options = check_options(black_pieces, black_locations, 'black')
                        white_options = check_options(white_pieces, white_locations, 'white')
                        turn_step = 2 #黑棋
                        selection = 100 #没有选中
                        valid_moves = []
            
                if turn_step > 1:
                    if click_coords == (8, 8) or click_coords == (9, 8):
                        winner = 'white'
                    if click_coords in black_locations:
                        selection = black_locations.index(click_coords)
                        if turn_step == 2:
                            turn_step = 3
                    if click_coords in valid_moves and selection != 100: 
                        black_locations[selection] = click_coords  #走起来了
                        if click_coords in white_locations:
                            white_piece = white_locations.index(click_coords)
                            captured_pieces_black.append(white_pieces[white_piece])
                            if white_pieces[white_piece] == 'king':
                                winner = 'black'
                            white_pieces.pop(white_piece)
                            white_locations.pop(white_piece)
                        black_options = check_options(black_pieces, black_locations, 'black')
                        white_options = check_options( white_pieces, white_locations, 'white')
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
acc = account()

if __name__ == "__main__" or __name__ == 'B.py' :
    print('_____                                           _____                   ______                                                                    ')
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

if __name__ == '__main__':
    while True:
        try:
            launch = input(f'{Lversions}   please choose version: ')
            ll = int(input('please shoose language(English:1): '))
            if ll == 1 :
                data = jt['English']
                for key in data:
                    value = data[key]
                    if ca == 0 and launch == key:
                        while True:
                            judge(value)
                            if ca == 1:
                                use = 1
                                ca = 0
                                break
            else :
                print('unavailble language')
            if use == 1 :
                print('thanks for use,goodbye!')
                break
            else:
                print('unavailble version')
        except:
            print(f'Sorry,the program went wrong. it will turn back automatically in 2 second.')
            time.sleep(2)