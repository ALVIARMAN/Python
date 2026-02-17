"""
    If you understand this clearly you will not have any problem in Class and Objects.

    To drive this car:
    Start Engine -> Accelerate -> Breaking -> Stop Engine

    @ALL Rights Reserved to MD. ALVI ARMAN
"""

class Car:
    _wheel = 4  #protected class variable
    def __init__(self,brand,types,maxspeed,wheel):
        #private instance variable
        self.__brand = brand
        self.__types = types
        self.__maxspeed = maxspeed
        Car._wheel = wheel
        self._isStart = False
        self._isAccelerate = False
        self._speed = 0

    def start_engine(self):
        self._isStart = True
        return f"Engine start's... 🚗"


    def accelerate(self,times):
        #to accelerate you need to start the engine first
        if self._isStart:
            self._speed = 0
            while times > 0:
                self._isAccelerate = True
                if self._speed < self.__maxspeed:
                    self._speed += 50
                elif self._speed >= self.__maxspeed:
                    return f"This car approach it's maximum speed {self._speed}"
                times -= 1
            return f"You drive this {self.__brand} car at the speed of {self._speed} km/h..."
        else:
            self._speed = 0
            return f"Please turn on the engine first "

    def breaking(self,times):
        #to break you need to accelerate first
        if self._isStart:
            if self._isAccelerate:
                while times > 0:
                    self._speed -= 50
                    if self._speed < 0:
                        self._speed = 0
                    times -= 1
            else:
                return f"Please accelerate first..."
        else:
            self._speed = 0
            return f"Turn on the engine man"
        return f"Your {self.__brand} car present speed is at {self._speed} km/h..."

    def stop_engine(self):
        if self._isStart:
            if not self._speed == 0:
                return f"Please reduce the speed to zero to turn off..."
            else:
                self._isStart = False
                return (f"You turn off the engine ... \n"
                        f"Congratulates you have successfully learn how to drive this {self.__brand} car.")
        else:
            return f"You don't even start the engine..."

    def get_details(self):
        return (f"This {self.__brand} car is a {self.__types} type. "
                f"It has {self.__maxspeed} maximum speed and "
                f"it has {self._wheel} wheel's.")

car1 = Car("BMW","Diesel",350,4)
print(car1.get_details())
print(car1.start_engine())
print(car1.accelerate(7)) #times of acceleration(gear)
print(car1.breaking(6)) #times of breaking(power)
print(car1.stop_engine())
