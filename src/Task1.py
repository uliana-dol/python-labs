class Helicopter:
    def __init__(self, passenger_capacity=0, name="Unknown", max_speed=0, year=0, model=""):
        self.__passenger_capacity = passenger_capacity
        self.__name = name
        self.__max_speed = max_speed
        self.__year = year
        self.__model = model

    @property
    def passenger_capacity(self):
        return self.__passenger_capacity

    @property
    def name(self):
        return self.__name

    @property
    def max_speed(self):
        return self.__max_speed

    def __str__(self):
        return f"Passenger capacity = {self.__passenger_capacity}; Name = {self.__name}; Max speed = {self.__max_speed}"

    def __repr__(self):
        return f"Helicopter ({self.__passenger_capacity}; {self.__name}; {self.__max_speed})"

    def __del__(self):
        print(f"Helicopter {self.__name} destroyed")

def main():
    hel1 = Helicopter(20, "NB", 3000, 2060, "Default Model")
    hel2 = Helicopter(15, "RM", 2000, 2070, "Default Model")
    hel3 = Helicopter(10, "V", 1500, 2034, "Default Model")

    print(hel1)
    print(hel2)
    print(hel3)


if __name__ == "__main__":
    main()
