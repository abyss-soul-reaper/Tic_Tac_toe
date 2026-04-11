def switch_player(game_state):
    game_state.curt_pl_idx = 1 - game_state.curt_pl_idx

def update_cell(board, player, cell_choice):
    if 1<= cell_choice <=board.size**2 and board.update_board(cell_choice, player.symbol):
        return True
