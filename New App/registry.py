class Registry:
    def __init__(self, enums):
        self.enums = enums

    def check_map(self):
        MAP = {
            self.enums.WIN: "Congratulations! You win!",
            self.enums.DRAW: "It's a draw!"
        }
        return MAP