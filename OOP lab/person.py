class Person:
    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthrate = healthRate


    def sleep(self, hours):
        if hours == 7:
            self.mood = "happy"
        elif hours <= 7:
            self.mood = "tired"
        else:
            self.mood = "lazy"      


    def eat(self, meals):
        if meals == 3:
            self.healthrate = 100
        elif meals == 2:
            self.healthrate = 75
        elif meals == 1:
            self.healthrate = 50

    def buy(self, items):
        self.money -= items * 10
