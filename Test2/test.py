class Test1:
    def __init__(self):
        self.c= None

    def a(self):
        try:
            print('a')
            raise Exception
        except:
           print('exception1111')
           raise Exception
        self.c = 'c'

        return self.c

    def b(self,m):
        print(m)
        print(self.c)

if  __name__=='__main__' :
    t=Test1()
    t.a()
    t.b(22)