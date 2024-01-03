class Chef:
    def make_chicken(self):
        print("The chef makes a chicken")
    def make_salad(self):
        print("The chef makes a salad")
    def make_specialDish(self):
        print("The chef makes a special dish")

class ChineseChef(Chef): # ChineseChef class is inheriting Chef class
    def chineseExtra(self):
        print("Chinese chef makes an extra dish/")   
    def make_specialDish(self): # overriding make_specialDish function of Chef class
        print("It's my special dish")     

chineseChef1 = ChineseChef() # creating object
chineseChef1.chineseExtra()
chineseChef1.make_chicken() 