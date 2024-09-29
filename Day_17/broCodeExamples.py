# POOP Examples ( Python Object Oriented Programming)

#Here we create a class
class Perro:
    def __init__(self,raza,nombre,genero,color):
        self.raza = raza
        self.nombre = nombre
        self.genero = genero
        self.color = color

    def start(self):
        print(f"you are walking the {self.raza} dog called {self.nombre}")

    def stop(self):
        print(f"You stopped walking the {self.raza} dog called {self.nombre}")

    def hungry(self):
        print(f"The dog called {self.nombre} is hungry and needs food")

    def describeDog(self):
        print(f"You are about to adopt a {self.raza} breed dog called {self.nombre} which is a {self.genero} dog and is color {self.color} ")
        


#Here im printing the objects
perro1 = Perro("Maltese","Wolfie","Male","White")
perro2 = Perro("Maltese","Fury","Female","Orange")



#Here i print the object attributes
print(perro1.raza)
print(perro1.nombre)
print(perro1.genero)

print(perro2.genero)
print(perro2.nombre)
print(perro2.genero)


#Here im using methods ( Functions that objects have inside them)
perro1.start()
perro1.stop()
perro1.hungry()

perro1.describeDog()
perro2.describeDog()