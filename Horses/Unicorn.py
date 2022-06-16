from Horses.Horse import Horse

# Klasa opisująca jednorożca
class Unicorn (Horse):
    cornColor = ""

    def __init__(self):
        super().__init__()

    def __str__(self) -> str:
        message = super().__str__()
        message += " I'm also a unicorn with " + self.cornColor + "-coloured corn!"
        #message += ...
        #message = message + ...
        return message