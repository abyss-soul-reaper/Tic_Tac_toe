from pipeline.game_enum import GameEnum


class Resolver:
    """Resolves actions to their corresponding configurations and handlers."""
    def resolve(action):
        if isinstance(action, GameEnum):
            enum_action = action
        elif isinstance(action, str):
            try:
                enum_action = GameEnum[action]
            except KeyError:
                raise ValueError(f"Unknown feature: {action}")
        else:
            raise TypeError("Invalid feature type")

        config = ACTION_CONFIG.get(enum_action)
        if not config:
            raise ValueError(f"No config found for action: {enum_action}")

        return enum_action, config

ACTION_CONFIG = {
    GameEnum.START_GAME: {
        "requires_input": False,
        "requires_system": True,
        "requires_pipeline": False,
    },
    # GameEnum.SET_PLAYERS: {
    #     "requires_input": True,
    #     "requires_system": False,
    #     "requires_pipeline": True,
    # },

     
}
