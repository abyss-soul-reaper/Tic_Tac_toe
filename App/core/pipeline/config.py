from App.core.base.menu_enum import GameAction
from App.ui.player.player_schema import *



class FeatureResolver:
    """
    Resolves a feature name (str or Enum) into a Feature/SpecialFeature enum
    and its configuration from FEATURE_CONFIG.
    """

    @staticmethod
    def resolve(feature):
        if isinstance(feature, GameAction):
            enum_feature = feature
        elif isinstance(feature, str):
            try:
                enum_feature = GameAction[feature]
            except KeyError:
                raise ValueError(f"Unknown feature: {feature}")
        else:
            raise TypeError("Invalid feature type")

        config = CONFIG.get(enum_feature)
        if config is None:
            raise ValueError(f"No config found for feature: {enum_feature}")

        return enum_feature, config


CONFIG = {
    GameAction.START_GAME: {
        "requires_input": False,
        "use_pipeline": False,
    },
    GameAction.SET_PLAYER_NAME: {
        "requires_input": True,
        "use_pipeline": True,
    },
    GameAction.SET_PLAYER_SYMBOL: {
        "requires_input": True,
        "use_pipeline": True,
    },
    GameAction.CHANGE_BOARD_SIZE: {
        "requires_input": True,
        "use_pipeline": True,
    },
    GameAction.START_MATCH: {
        "requires_input": False,
        "use_pipeline": False,
    },
    GameAction.NAV_BACK: {
        "requires_input": False,
        "use_pipeline": False,
    },
}