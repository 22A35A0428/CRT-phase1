insurance=5000
class carshowroom:
    def toyota():
        print("welcome to toyota cars Enter ur choice")
        print("Glanza=0 & Hilux=1")
        b=int(input("please enter model :"))
        price1=100000
        price2=200000
        if b==0:
            print("final car price is Rs",price1+(.18*price1)+(.16*price1)+insurance)
        elif b==1:
            print("final car price is Rs",price2+(.18*price2)+(.16*price2)+insurance)
        else:
            print("Sorry wrong choice")
      
    def tata():
        print("welcome to tata cars")
        print("TATA tigor=0 &TATA punch=1")
        b=int(input("please enter ur model : "))
        price1=300000
        price2=400000
        if b==0:
            print("final car price is Rs",price1+(.18*price1)+(.16*price1)+insurance)
        elif b==1:
            print("final car price is Rs",price2+(.18*price2)+(.16*price2)+insurance)
        else:
            print("sorry wrong choice")

    def tesla():
        print("welcome to tesla cars")
        print("Mdel x=0 & Model Y")
        b=int(input("please enter ur model:"))
        price1=500000
        price2=600000
        if b==0:
            print("final car price is Rs",price1+(.18*price1)+(.16*price1)+insurance)
        elif b==1:
            print("final car price is Rs",price2+(.18*price2)+(.16*price2)+insurance)
        else:
            print("sorry wrong choice")
       
    list=['TOYOTA','TATA','TESLA']
    a=str(input("enter u r car name:"))
    a=a.upper()
    if a!=list[:]:
        print("sorry u enter wrong car name")
    for i in range (0,3):
        if a==list[i]:
            if i==0:
              toyota()
            elif i==1:
              tata()
            elif i==2:
             tesla()    
