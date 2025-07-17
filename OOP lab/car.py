class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self. fuelRate = min(fuelRate, 100)
        self.velocity = min(velocity, 200)


    def run(self, velocity, distance):
        self.velocity = min(velocity, 200)
        self.distance = distance



    def stop(self, remaining_distance):
        self.velocity = 0
        if remaining_distance > 0:
            print(f"remaning distance {remaining_distance} km")
        else:
            print("You have arrived")


