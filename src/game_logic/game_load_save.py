# from game_contracts.game_logic_interface import GameLogicABC
from src.game_logic.game_config import available_functions


class GameLoadSave:
    def __init__(self):
        pass

    def build_new_game_state(self, requesting_player_id) -> dict[str, str]:
        """
        Build a new game state for the game.
        """
        # abstracted away until the game storage runner is implemented
        return {}

    def get_ongoing_game_choices(self, requesting_player_id) -> dict[str, str]:
        """
        Get the options for an ongoing game.
        """
        # abstracted away until the game storage runner is implemented
        return {}

    def check_game_in_progress(self, requesting_player_id) -> bool:
        """
        Check if a game is in the game registry already.
        """
        # abstracted away until the game storage runner is implemented
        # Will check dynamodb for existing game
        return False

    def load_ongoing_game_state(self) -> dict[str, str]:
        """
        Load the game state from the game storage.
        """
        # abstracted away until the game storage runner is implemented
        self.game_over = False
        return {}
