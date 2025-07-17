from person import Person

class Employee(Person):
    def __init__(self, name, money, mood, healthrate, id , car, email, salary, distanceToWork):
        super().__init__(name, money, mood, healthrate)
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork



    def work(self, hours):
        if hours == 8:
            self.mood = "happy"
        elif hours >= 8:
            self.mood = "tired"
        else:
            self.mood = "lazy"      



    def refuel(self, gasAmount = 100):
        self.car.fuelRate += gasAmount

    





        
    