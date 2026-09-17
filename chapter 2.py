#Day--1  if, elif, else 
my_lover=input('请输入她的名字')
birthday=float(input('请输入她的生日'))        # birthday=input('请输入她的生日')
if len(my_lover)==4 and my_lover=='zcyn':
    print('不忘初心')
elif birthday==6.8:      #.elif birthday=='6.8':(注意，input默认我输入的为字符串,赋值等于也要是字符串)
    print('不断努力')
else:
    print('继续沉淀')


#Day--2  while循环 ,break, continue
while True:
    my_lover=input('Who do you love? ')
    if my_lover!='zcyn':
        print('Think carefully!')
        continue
    print('Are you together?')
    answer=input('请输入 yes or no ')    
    if answer=='no':
        print('坚定，努力，相信自己！！！')      
        break                        # 每个条件要退出循环，都要加上break,否则会一直循环下去
    elif answer=='yes':
        print('Forever!!!')
        break


#Day--3  for循环，range函数, random模块, sys模块 
import random, sys
for i in range(100,0,-1):
    print(520)
while True:                  # while True:可无限循环取，range :循环有限次取
    I=random.randint(1,100)
    Love=random.randint(1,100)
    You=random.randint(1,100)
    if I+Love+You==5+2+0:
        print('zcyn!!!')
        sys.exit()
        

    


