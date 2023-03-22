class Car_builder:

    car_options = {
         'EV': 1000,
         'tires': 500,
         'paint': 100,
         'wheels': 150,
         'sun-roof': 400,
         'spare-tire': 50,
         'leather-seats': 200
    }

    def __init__(self):
        self.total = 0
        self.options = []

    def __repr__(self):
        if self.options != None:
                return 'The <Car > has no options at the moment!'        
        else:
            print('The(se) are the option(s)')
            for option in self.options:
                return f'{option}'
            
         

    def add_options(self, item):
        self.options.append(item)
        self.total += self.car_options[item]

    def print_receipt(self, tax, service):
        tax = (tax/100) * self.total
        service = (service/100) * self.total
        total = self.total + tax + service

        for option in self.options:
            print(f'{option:15} ${self.car_options[option]}')
        print('-' * 21)    
        print(f'{"Total:":15} ${int(total)}')


car1 = Car_builder()



if __name__ == '__main__':
    print(car1)
    car1.print_receipt(7, 20)