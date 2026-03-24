from App.ui.player.player_result import PlayerResult

class PlayerCli:
    SYMBOLS = ['X', 'O']

    def player_name(self):
        res = PlayerResult()

        name = input("Enter Your Name (Only Letters!): ")
        res.payload["name"] = name
        return res.success()
    
    def player_symbol(self):
        res = PlayerResult()
        
        symbol = input(f"Choose Your Symbol (X OR O): ").strip().upper()
        res.payload["symbol"] = symbol
        return res.success()

    def change_board_size(self):
        res = PlayerResult()

        try:
            size = int(input("Enter New Board Size (e.g., 3 for 3x3): "))
            res.payload["board_size"] = size
            return res.success()
        except ValueError:
            res.validatoin_error("Invalid input! Board size must be a number.")
            return res
