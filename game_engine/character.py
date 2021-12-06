class Character:
    def __init__(self, request) -> None:
        self.name = request["name"]
        # if no alias will return "-"
        self.aliases = request["biography"]["aliases"][0]
        self.occupation = request["work"]["occupation"]
        self.intelligence = request["powerstats"]["intelligence"]
        self.strength = request["powerstats"]["strength"]
        self.speed = request["powerstats"]["speed"]
        self.profilepic = request["image"]["url"]
        self.eyecolour = request["appearance"]["eye-color"]
        self.height = request["appearance"]["height"][0]

    def getName(self) -> str:
        return self.name
