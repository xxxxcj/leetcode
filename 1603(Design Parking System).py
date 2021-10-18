class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small
        self.big_now = 0
        self.medium_now = 0
        self.small_now = 0


    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big_now < self.big:
                self.big_now += 1
                return True
        elif carType == 2:
            if self.medium_now < self.medium:
                self.medium_now += 1
                return True
        elif carType == 3:
            if self.small_now < self.small:
                self.small_now += 1
                return True
        return False



# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)