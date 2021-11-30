from utils import get_character()
import random

class Superhero():
    def __init__(self,request):
        self.name=request["name"]
        self.aliases=request["biography"]["aliases"][0]         # if no alias will return "-"
        self.occupation=request["work"]["occupation"]
        self.intelligence=request["powerstats"]["intelligence"]
        self.strength=request["powerstats"]["strength"]
        self.speed=request["powerstats"]["speed"]
        self.profilepic=request["image"]["url"]
        self.eyecolour=request["appearance"]["eye-color"]
        self.height=request["appearance"]["height"][0] #returns height in feet.

    def getName(self):
        return self.getName()

    def getName(self):
        return self.getName()

#EXAMPLE CALL TO CREATE A RANDOM HERO CHARACTER - BUT IMPORT RANDOM
player2=Superhero(get_character(str(random.randint(1, 731))))