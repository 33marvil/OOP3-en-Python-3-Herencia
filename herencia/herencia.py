"""code goes here"""
class Animal: # super class
    """Animal class"""

    def __init__(self):
        pass

    def sight(self):
        return "I'm seeing..."

    def who_am_i(self):
        return "I'm an animal and"

class Sea: # super class
    """Marino class"""
    def __init__(self):
        pass

    def where_i_live(self):
        return " I live in the sea."

class Mammal(Animal):
    """Mammal class"""

    def __init__(self):
        pass

    def who_am_i(self):
        # Llamar a method who_am_i de la super class
        return super().who_am_i() + " I'm a Mammal."

class Reptile(Animal):
    """Reptile class"""

    def __init__(self):
        pass

    def who_am_i(self):
        # Llamar a method who_am_i de la super class
        return super().who_am_i() + " I'm a Reptile."

class Bird(Animal):
    """Bird class"""
    def __init__(self):
        pass

    def who_am_i(self):
        # Llamar a method who_am_i de la super class
        return super().who_am_i() + " I'm a Bird."

class Fish(Animal, Sea): # Herencia multiple Fish < Animal y < Sea
    """Fish class"""

    def __init__(self):
        pass

    def who_am_i(self):
        # Llamar a method who_am_i de la super class + who_am_i + where_i_live de super class Sea
        return super().who_am_i() + " I'm a Fish." + super().where_i_live()

class SeaTurtle(Reptile, Sea): # Herencia multiple  SeaTurtle < Reptile y < Sea
    """SeaTurtle class"""

    def __init__(self):
        pass

    def who_am_i(self):
        # Llamar a method who_am_i de la sub class Reptile + who_am_i + where_i_live de super class Sea
        return super().who_am_i() + " I'm a Turtle too." + super().where_i_live()

class Dog(Mammal): # Herencia multiple  Dog < Mammal < Animal
    """Dog class"""

    def who_am_i(self):
        # Llamar a method who_am_i de la sub class Mammal
        return super().who_am_i() + " I'm a Dog too."

class Macaw(Bird): # Herencia multiple  Macaw < Bird < Animal
    """Macaw class"""

    def who_am_i(self):
        # Llamar a method who_am_i de la sub class Bird
        return super().who_am_i() + " I'm a Macaw too."

class Dolphin(Mammal, Sea): # Herencia multiple  Dolphin < Mammal y < Sea
    """Dolphin class"""

    def who_am_i(self):
        # Llamar a method who_am_i de la sub class Mammal + who_am_i + where_i_live de super class Sea
        return super().who_am_i() + " I'm a Dolphin too." + super().where_i_live()

class Cat(Mammal): # Herencia multiple  Cat < Mammal < Animal
    """Cat class"""
    # Llamar a method who_am_i de la sub class Mammal
    def who_am_i(self):
        return super().who_am_i() + " I'm a Cat too."

class Whale(Mammal, Sea): # Herencia multiple  Cat < Mammal < Sea
    """Whale class"""

    def who_am_i(self):
        # Llamar a method who_am_i de la sub class Mammal + who_am_i + where_i_live de super class Sea
        return super().who_am_i() + " I'm a Whale." + super().where_i_live()

class Snake(Reptile): # Herencia multiple Snake < Reptile < Animal
    """Snake class"""

    def who_am_i(self):
        # Llamr a method who_am_i de la sub clase Reptile
        return super().who_am_i() + " I'm a Snake too."

#print(SeaTurtle.__mro__)
