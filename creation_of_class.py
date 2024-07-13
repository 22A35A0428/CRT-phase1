class me:
    def l(self):
        print("on light")
    def f(self,speed):
        print("o fan speed",speed)
        self.s=speed
    def cpu(self):
        print("on cpu")
        print(self.s)
you=me()
you.l()
you.f(5)
you.cpu()

