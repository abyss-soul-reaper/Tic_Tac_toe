class GameCli:
    def __init__(self):
        pass

    def show_menu(self, actions_map, menu_name):
        print(f"\n=== {menu_name.replace('_', ' ').title()} ===")

        for idx, action in actions_map.items():
            print(f"{idx}. {action.value}")

        choice = input("Select an action: ")
        while not choice.isdigit() or int(choice) not in actions_map:
            choice = input("❌ Invalid choice. Try again: ")
        print(actions_map[int(choice)])
        return actions_map[int(choice)]



