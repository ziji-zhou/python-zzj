#Day--4  综合小项目--剪刀石头布
import random, sys
print('我们来玩，剪刀，石头，布！三局两胜！')
win=0
python_win=0                  # 初始赋值要写在循环外！写到循环内，会使每次循环又回到初始值！
for game in range(1,4):
   python=random.randint(1,3)
   player=input('paper,scissors,rock 出！')
   if player=='paper':
        player=3
   elif player=='scissors':
        player=1 
   elif player=='rock':
        player=2   
   if python==player:
        win=win+0
        print('这局平局！') 
   elif (player==1 and python==3) or (player==2 and python==1) or (player==3 and python==2):
        win=win+1
        python_win=python_win+0
        print('这局你赢了！') 
   else:
        win=win+0
        python_win=python_win+1
        print('这局你输了！')
while True:                        #  True 的 t 要大写!!!
     if win>=2 and python_win<=1:
          print('恭喜，你赢了！'+'你:我='+str(win)+':'+str(python_win))
          break
     elif win<=1 and python_win>=2:
          print('抱歉，你输了！'+'你:我='+str(win)+':'+str(python_win))
          break
     else:
          print('平局！'+'你:我='+str(win)+':'+str(python_win))
          sys.exit()