#Day2  综合小项目---动态写‘Z , N’
import time
kong_1 = 48
x = 40

for a in range(1,4):
    print('*'*60)
    time.sleep(0.1)

while True:
    print(' '* kong_1+'*'*12)
    time.sleep(0.1)
    kong_1=kong_1-2
    if kong_1==0:
        break

for b in range(1,5):
    print('*'*60)
    time.sleep(0.1)

for c in range(1,5):
    print(' ')    

# 写 N ，（ 定义函数 + 利用布尔值，控制if语句）
s= True
t= False
v= False
ge_1 = 10
ge_2 = 0
kong_2 = 0
kong_3 = 40
def zhu_1():
    print('*' * ge_1,end='')

def zhu_2():
    print(' ' * kong_3 + '*' * ge_1)

for d in range(1,31):

    if s:
        zhu_1()
        print('*' * ge_2,end='')
        zhu_2()
        ge_2 = ge_2 + 2
        kong_3 = kong_3 - 2
        if ge_2 == 20:
            s = False
            t = True
    elif t:
        zhu_1()
        print(' ' * kong_2 + '*' * ge_2,end='')
        zhu_2()
        kong_2 = kong_2 + 2
        kong_3 = kong_3 - 2
        if kong_2 == 20:  
            t = False
            v = True
    elif v:
        zhu_1()
        print(' ' * kong_2 + '*' * ge_2,end='')
        zhu_2()
        ge_2 = ge_2 - 2
        kong_2 = kong_2 + 2

    time.sleep(0.1)    









