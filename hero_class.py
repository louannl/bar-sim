from utils import get_character,set_user_character
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


#EXAMPLE CALL TO CREATE USER CHARACTER
player1=Superhero(get_character(set_user_character()))

#EXAMPLE CALL TO CREATE A RANDOM HERO CHARACTER
player2=Superhero(get_character(str(random.randint(1, 731))))
print(player1.name)