#Day---1  def语句，调用栈，局部和全局作用域对变量的影响（见书52～53）
def _5():
    print('I')
    _2()
    _0()

def _2():
    print('miss')
    _13()

def _13():
    print('you',end='')               # ,end=''指定参数末尾输出什么
    print('!')

def _0():
    if True:
      return print('Z','C','Y','N','',sep='!')     # ,sep=''指定在参数之间输出什么,但参数之间先要用逗号分开
                                                   # return 语句指定返回什么值

_5()

