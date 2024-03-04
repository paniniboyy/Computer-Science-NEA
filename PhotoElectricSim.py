import random
import numpy as np


class Metal():
    def __init__(self, x, y, width = 6, height = 4):
        self.x = x #x is used to declare where the metal will be on the x-axis/horizontal direction
        self.y = y #y is used to delclare where the metal will be on the y-axis/vertical direction
        self.width = width #width of metal is constant value, 6
        self.height = height #height of metal is constant value, 4

#Each subsequent class inherits from the class Metal, keeping the same height, width, x and y dimensions but having different names and work functions

class MetalCaesium(Metal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Caesium"
        self.WorkFunctionEV = 2.12

class MetalIron(Metal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Iron"
        self.WorkFunctionEV = 4.36

class MetalSodium(Metal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Sodium"
        self.WorkFunctionEV = 2.27

class MetalBarium(Metal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Barium"
        self.WorkFunctionEV = 2.51

class MetalSilver(Metal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Silver"
        self.WorkFunctionEV = 4.28

class MetalMagnesium(Metal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Magnesium"
        self.WorkFunctionEV = 3.46

class MetalCadmium(Metal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Cadmium"
        self.WorkFunctionEV = 3.92

class MetalAluminium(Metal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Aluminium"
        self.WorkFunctionEV = 3.74

class MetalNickel(Metal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Nickel"
        self.WorkFunctionEV = 4.84

class MetalCopper(Metal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Copper"
        self.WorkFunctionEV = 4.47

class MetalTungsten(Metal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Tungsten"
        self.WorkFunctionEV = 4.5

class MetalChromium(Metal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Chromium"
        self.WorkFunctionEV = 4.51
        
class MetalZinc(Metal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Zinc"
        self.WorkFunctionEV = 3.74

class MetalGold(Metal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Gold"
        self.WorkFunctionEV = 4.58
    
class MetalLead(Metal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Lead"
        self.WorkFunctionEV = 4.02

class Radiation():# This class represents a radiation source with its x and y coordinates, wavelength, and frequency.
    def __init__(self, x, y, wavelength, frequency):
        self.x = x #x coordinate of the radiation source
        self.y = y #y coordinate of the radiation source
        self.wavelength = wavelength #wavelength of radiation source given as a float value
        self.frequency = frequency #frequency of radiation source given as a float value

        




        
        

    