import requests
import os
import re
#获取数字
def req():
    r = requests.get('https://python666.cn/cls/number/guess/')
    print(r.text)
    return r.text
#确保文件路径可用
def getfile(add):
    if os.path.exists(add) == False:
        fi = open(add, 'w+')
#获取玩家记录
def getrecord(name1,data):
    global k
    k = -1
    length = len(data)
    userinfo = []
    if length:
        for i in range (length):
            name = (data[i].split())[0]
            if name1 == name:
                userinfo = data[i].split()
                k = i
                break
    if not userinfo:
         userinfo = [name1, '0', '0', '0']
    print('%s, you already have played %s times, minimum %s rounds, average %s rounds, start to play' %(userinfo[0],userinfo[1],userinfo[2],userinfo[3]))
    return userinfo

#玩游戏
def game(n):
    t = 0
    judge = 1
    while judge:
        num1 = input('guess a number')
        m = re.match(r'\d+$', num1)
        if m :
            num1 = int(num1)
            if num1 > n:
                print('too big, guess another one')
            elif num1 < n:
                print('too small, guess another one')
            else:
                print("You're right" )
                judge = 0
        else:
            print('it is not a number, guess another one')
        t += 1
    return t

#写入玩家记录
def writerecord(add, data, result):
    if k >= 0:
        data[k] = result + '\n'
    else:
        data.append(result + '\n')
    with open(add,'w+') as fi:
        fi.writelines(data)
try:
    conti = 'y'
    while conti == 'y':
        add = 'record1.txt'
        getfile(add)
        with open(add) as fi:
            data = fi.readlines()
        print(data)
        name1 = input('enter your name')
        player = getrecord(name1, data)
        n = int(req())
        times = game(n)
        total_rounds = int(player[1])
        min_times = int(player[2])
        avg_times = float(player[3])
        if min_times == 0 or times < min_times:
            min_times = times

        total_times = avg_times * total_rounds + times
        total_rounds +=1
        avg_times = total_times / total_rounds
        print('%s, you already have played %d times, minimum %d rounds, average %.2f rounds' %(name1,total_rounds,min_times,avg_times))
        result = '%s %d %d %.2f'%(player[0], total_rounds, min_times, avg_times)
        writerecord(add, data, result)
        conti = input('是否继续游戏?(输入y继续，其他退出)')
    print('退出游戏，欢迎下次再来！')
except:
    print('error')























