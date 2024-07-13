class you:
    def hh(self):
        print("turn")
    def jj(self,sp):
        print("go right",sp)
        self.oo=sp
    def kk(self):
        print("go  left")
        print(self.oo)

class me(you):
    def __init__(self,place):
        self.p=place
        print("welcome",place)
    def l(self):
        print("on light")
    def f(self,speed):
        print("o fan speed",speed)
        self.s=speed
    def cpu(self):
        print("on cpu")
        print(self.s)

class shopping(you):
 
    def dt(self,type):
        self.t=type
    def dp(self,price):
        self.pp=price
    def ds(self,size):
        self.s=size
    def dis(self):
        print(self.t,self.pp,self.s)
k=shopping()
k.dt(22)
k.dp(400)
k.ds(12)
k.dis()
k.hh()
k.jj("5mt")
k.kk()
k1=me("iiiii")
k1.l()
k1.f(5)
k1.cpu()
k1.hh()
k1.jj("6mt")
k1.kk()
