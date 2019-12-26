class person:
    def __init__(self, name, age, add):
        self.name = name
        self.age  = age
        self.add  = add
    
    def hi(self):
        print('hi. I am {0}'.format(self.name))