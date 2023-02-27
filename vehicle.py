class Vehicle:
    def __init__(self, doors, color, height, width, capacity, company):
        self.doors = doors
        self.color = color
        self.height = height
        self.width = width
        self.capacity = capacity
        self.company = company

class Car(Vehicle):
    def __init__(self, doors, color, height, width, capacity, company, horsepower):
        super().__init__(doors, color, height, width, capacity, company)
        self.horsepower = horsepower

    def __repr__(self):
        return f"""<{self.__class__.__name__} company:{self.company},
                    doors:{self.doors},
                    color:{self.color},
                    height:{self.height},
                    width:{self.width},
                    capacity:{self.capacity}
                    horsepower:{self.horsepower}>
                    """ 

    def revving(self):
        return f'The {self.color} {self.company} rev sounds insane with {self.horsepower}!'

class Truck(Vehicle):
    def __init__(self, doors, color, height, width, capacity, company, cargo_capacity):
        super().__init__(doors, color, height, width, capacity, company)
        self.cargo_capacity = cargo_capacity

    def __repr__(self):
        return f"""<{self.__class__.__name__} company:{self.company},
                    doors:{self.doors},
                    color:{self.color},
                    height:{self.height},
                    width:{self.width},
                    capacity:{self.capacity}
                    cargo_capacity:{self.cargo_capacity}>
                    """ 
 
    def haul(self):
        return f'The {self.color} Truck is hauling {self.cargo_capacity} of cargo!'

class Helicopter(Vehicle):
    def __init__(self, doors, color, height, width, capacity, company, rotor_blades):
        super().__init__(doors, color, height, width, capacity, company)
        self.rotor_blades = rotor_blades

    def __repr__(self):
        return f"""<{self.__class__.__name__} company:{self.company},
                    doors:{self.doors},
                    color:{self.color},
                    height:{self.height},
                    width:{self.width},
                    capacity:{self.capacity}
                    rotor_blades:{self.rotor_blades}>
                    """ 

    def hover(self):
        return f'The {self.color} {self.company} helicopter is hovering using it\'s {self.rotor_blades} rotor blades!'

class Fighter_jet(Vehicle):
    def __init__(self, doors, color, height, width, capacity, company, model, stealh, lbs_thrust, supercruise):
        super().__init__(doors, color, height, width, capacity, company)
        self.model = model
        self.stealth = stealh
        self.lbs_thrust = lbs_thrust
        self.supercruise = supercruise

    def __repr__(self):
        return f"""<{self.__class__.__name__} company:{self.company},
                    doors:{self.doors},
                    color:{self.color},
                    height:{self.height},
                    width:{self.width},
                    capacity:{self.capacity}
                    model:{self.model}
                    stealth:{self.stealth}
                    lbs_thrust:{self.lbs_thrust}
                    supercruise:{self.supercruise}>
                    """     

    def flying(self):
        return f'The {self.company} {self.model} is flying supersonic!'

if __name__ == '__main__':
    # Each instance.
    print('Each Object:')
    print(Car(4, 'Blue', 6, 7, 2, 'Lamborghini', '768Hp'))
    print(Truck(2, 'Black', 12, 10, 2, 'Peterbuilt', '320^FT'))
    print(Helicopter(2, 'White', 22, 16, 6, 'Bell', 6))
    print(Fighter_jet(1, 'Gray', 14, 35, 1, 'Lockheed-Martin','F-35', True, 43000, False ))
    print('Methods:')
    # Each instance's Method
    print(Car(4, 'Blue', 6, 7, 2, 'Lamborghini', '768Hp').revving())
    print(Truck(2, 'Black', 12, 10, 2, 'Peterbuilt', '320^FT').haul())
    print(Helicopter(2, 'White', 22, 16, 6, 'Bell', 6).hover())
    print(Fighter_jet(1, 'Gray', 14, 35, 1, 'Lockheed-Martin', 'F-35', True, 43000, False).flying())