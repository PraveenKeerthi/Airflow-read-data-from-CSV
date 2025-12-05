class Vehicle:
    def __init__(self, name='Maruti', color='blue'):
        self.name = name
        self.color = color
        self.__speed = 100

    # This is a magic method, so when we call print(Vehicle) it will print the string returned by this method
    def __str__(self):
        return f"{self.name} is {self.color}"
    
    def sound(self):
        return "Vroom"

    # Encapsulted variable is retrieved only by getter
    def get_speed(self):
        return self.__speed


# Inheritance
class car(Vehicle):

    def __init__(self,name,color,type='hatchback'):
        super().__init__(name,color)
        # we can also use like this -> Vehicle.__init__(self,name,color)
        self.type = type
    
    #polymorphism
    def sound(self):
        if(self.type == 'hatchback'):
            return "pssst"
        elif(self.type == 'sports'):
            return "Vrooooooooooooom vroooom..."
        else:
            return "Vroom"

if __name__ == "__main__":
    v = Vehicle()
    print("Main class attributes",v.name,v.color)
    print("Main class sound()",v.sound())
    print("Encapsulated attribute",v.get_speed())

    c = car("Bmw","red","sports")
    print("Inherited attributes",c.name,c.color)
    print("Inherited (polymorphism) method",c.sound())
