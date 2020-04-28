import requests
import re
import os

def G(n):
    global m1
    while True:
        num1 = str(input('guess a number'))
        #print(num1)
        m = re.match(r'\d+', num1)
        #print(type(num1))
        #print(m)
        if m != None:
            if num1 > n:
                print('too big, guess another one')

            elif num1 < n:
                print('too small, guess another one')
            else:
                print("You're right" )
                m1 +=1
                break
        else:
            print('it is not a number, guess another one')
        m1 += 1
        #print(m1)

def req():
    r = requests.get('https://python666.cn/cls/number/guess/')
    return r.text

try:
    while True:
        name1 = input('enter your name')
        add = 'record1.txt'
        bo = os.path.exists(add)
        if bo == True:
            with open(add) as fi:
                whole = fi.readlines()
            length = len(whole)
             # print(length)
            # print(whole)
            a = 0
            for i in range(length):
                #print(whole[i])
                find = re.match(name1, whole[i])
                #print(find)
                if find:
                    a = 1
                    data = whole[i].split(' ')
                    # print(data)
                    k = i
                    print(k)
                    print(a)
                    print('%s, you already have played %s times, minimum %s rounds, average %s rounds, start to play' %(data[0],data[1],data[2],data[3]))
                    break
                elif i == length-1 and a == 0:
                        print('%s, you already have played 0 times, minimum 0 rounds, average 0 rounds, start to play'%name1)
                        data = [name1, '0', '0', '0']
                        k = length

        else:
            fi = open("record1.txt", 'w+')
            print('%s, you already have played 0 times, minimum 0 rounds, average 0 rounds, start to play' % name1)
            data = [name1, '0', '0', '0']
            k = 0
            a = 0

        n = req()
        print(n)
        m1 = 0
        G(n)
        print(m1)
        #print(data)

        if m1 < int(data[2]) or int(data[2]) == 0:
            #print('3')
            data[2]= str(m1)
        data[1] = str(int(data[1])+1)
        #print(data[1])
        #print(float(data[3]))
        data[3] = str(float(data[3])+m1/int(data[1]))
        #print(data)
        print('%s, you already have played %s times, minimum %s rounds, average %s rounds' %(name1,data[1],data[2],data[3]))
        result = name1 + ' ' + data[1] + ' ' + data[2] +' ' +data[3]+ '\n'
        print(result)
        #print(a)
        #print(k)
        if a == 0:
            with open(add, 'a') as fi:
                fi.writelines(result)
        elif a == 1:
            whole[k] = result
            #print(whole)
            with open(add, 'w') as fi:
                fi.writelines(whole)

        conti = input('是否继续游戏?(输入y继续，其他退出)')
        if conti != 'y':
            break
    print('退出游戏，欢迎下次再来！')
except:
    print('error')



