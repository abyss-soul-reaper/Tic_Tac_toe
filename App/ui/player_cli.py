class PlayerInterface:
    def player_name(self):
        name = input("Enter Your Name (Only Letters!): ").strip().title()
        while not name.isalpha():
            name = input("Invalid name! Make Sure Your Name Is Alphabetic: ")
        return name
    
    def player_symbol(self):
         symbol = input(f"Choose Your Symbol (X OR O): ").strip().upper()
         while not (symbol.isalpha() and len(symbol) == 1 and symbol in self.SYMBOLS):
            symbol = input(f"Invalid! Please enter a SINGLE letter: ").strip().upper()
         return symbol

         