from interface.cli import Cli
from pipeline.registry import Registry
from pipeline.dispatcher import Dispatcher



class GameLoop:
    def __init__(self):
        self.cli = Cli()
        self.registry = Registry(self)
        self.dispatcher = Dispatcher(self.registry)


    


    

    # def set_players(self):
    #     players = []
    #     for _ in range(2):
    #         name = self.cli.player_name()
    #         symbol = self.cli.player_symbol()
    #         players.append(Player(name, symbol))
    #         clear_screen()
    #     return players
        
    # def play_game(self):
    #     players = self.set_players()
    #     self.game_state = GameState(players, Board())

    #     player = self.game_state.current_player
    #     board = self.game_state.board
    #     while True:
    #         self.cli.play_turn(player, board)
    #         status = check(board, self.enums)
    #         self.cli.status_message(player, status)
    #         self.game_state.switch_player()
    #         player = self.game_state.current_player


    # def start_game(self):
    #     actions = get_menu_actions(self.current_menu)
    #     action = self.cli.select_action(actions)
    #     clear_screen()
    #     menu = self.registry.main_menu_actions()
    #     if action in menu.keys():
    #         menu.get(action)()

    # def restart_game(self):
    #     clear_screen()
    #     self.game_state.Reset()
    #     self.cli.play_turn(self.game_state.current_player, self.game_state.board)
        
# if __name__ == "__main__":


