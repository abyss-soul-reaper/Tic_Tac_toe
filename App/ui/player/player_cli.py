class PlayerCli:
    def player_name(self):
        name = input("Enter Your Name (Only Letters!): ")
        return {"name": name}
    
    def player_symbol(self):
        symbol = input(f"Choose Your Symbol (X OR O): ")
        return {"symbol": symbol}

    def change_board_size(self):
        size = input("Enter New Board Size (e.g., 3 for 3x3): ")
        return {"board_size": size}


