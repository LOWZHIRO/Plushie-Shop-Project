class Plushie:
    def __init__(self, name, price, shop):
        self.name = name
        self.price = price
        self.shop = shop

    def updateShop(self, shop):
        self.shop = shop

    def buyFromShop(self):
        if self.shop == 0: # if there is no items available
            # raise not item exception
            pass
        self.shop -= 1

class PlushShop:

    def __init__(self):
        self.amount = 0
        self.Plushies = []

    def addPlushies(self, plushie):
        self.Plushies.append(plushie)

    def showPlushies(self):
        print("_________\nPlushies in shop\n_________")
        for plushie in self.Plushies:
            if plushie.shop == 0:
                self.Plushies.remove(plushie)
        for plushie in self.Plushies:
            print(plushie.name + ": " "$", plushie.price) 
        print("__________\n")

    def addCash(self, money):
        self.amount = self.amount + money

    def buyPlushie(self, plushie):
        if self.amount < plushie.price:
            print("Not enough cash...") 
        else:
            self.amount -= plushie.price
            plushie.buyFromShop()
            print(f"{plushie.name} has been purchased!")
            print(f"You have {self.amount} cash left.")

    def containsPlushies(self, wanted):
        ret = False
        for plushie in self.Plushies:
            if plushie.name == wanted:
                ret = True
                break
        return ret
    def getPlushie(self, wanted):
        ret = None
        for plushie in self.Plushies:
            if plushie.name == wanted:
                ret = plushie
                break
        return ret

    def insertAmountForPlushie(self, plushie):
        price = plushie.price
        while self.amount < price:
                self.amount = self.amount + float(input("It is $" + str(price - self.amount) + ", how much would you like to pay? "))
    def checkRefund(self):
        if self.amount > 0:
            print(str(self.amount) + " refunded.")
            self.amount = 0
            print("Thank you for buying our plushies ٩(ˊᗜˋ*)و ♡ !\n")


def plush():
    shop = PlushShop()
    Plushie1 = Plushie("Lil Bunny", 15, 6)
    Plushie2 = Plushie("Lovely-Lula Cub", 20, 4)
    Plushie3 = Plushie("Fuwafuwa",  32, 3)
    Plushie4 = Plushie("Sir Foxelite",  35,2)
    Plushie5 = Plushie("Meowrry",28, 3)
    shop.addPlushies(Plushie1)
    shop.addPlushies(Plushie2)
    shop.addPlushies(Plushie3)
    shop.addPlushies(Plushie4)
    shop.addPlushies(Plushie5)

    print("_______Welcome to our world of Plushies!_______\n")

    continueToBuy = True
    while continueToBuy == True:
        shop.showPlushies()
        selected = input("select plushie: ")
        if shop.containsPlushies(selected):
            plushie = shop.getPlushie(selected)

            shop.insertAmountForPlushie(plushie)
            shop.buyPlushie(plushie)

            a = input("buy something else? (y/n): ")
            if a == "n":
                continueToBuy = False
                shop.checkRefund()
            else:
                continue

        else:
            print("Plushie not available. Select another Plushie.")
            continue

plush()