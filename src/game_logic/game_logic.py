# from game_contracts.game_logic_interface import GameLogicABC
from src.game_logic.game_config import available_functions


class SampleGameLogic:
    def __init__(self, requesting_client):
        self.game_over = False
        self.requesting_client = requesting_client

    def setup_game_state(self) -> dict[str, str]:
        if not self.check_game_in_progress():
            self.game_state = self.build_new_game_state()
        else:
            self.game_state = self.load_ongoing_game_state()
        return self.report_current_game_state()

    def check_game_in_progress(self) -> bool:
        """
        Check if a game is in the game registry already.
        """
        # abstracted away until the game storage runner is implemented
        # Will check dynamodb for existing game
        return False

    def build_new_game_state(self) -> dict[str, str]:
        """
        Build a new game state for the game.
        """
        # abstracted away until the game storage runner is implemented
        return {}

    def load_ongoing_game_state(self) -> dict[str, str]:
        """
        Load the game state from the game storage.
        """
        # abstracted away until the game storage runner is implemented
        self.game_over = False
        return {}

    def report_current_game_state(self) -> dict[str, str]:
        return self.game_state

    def update_game_state(self): ...

    def is_game_over(self) -> bool:
        return self.game_over

    def get_current_player(self) -> int: ...

    def get_available_actions(self, player_id: int) -> list[dict[str, str]]: ...

    def apply_action(self, input_player: str) -> None: ...

    def post_turn_cleanup(self, player_id: int) -> None: ...

    def handle_input(self, input_data):

        input_player = input_data.get("player_id")
        action = input_data.get("action")

        if action in available_functions:
            self.apply_action(action, input_player)
            return available_functions[action]()
        else:
            print(f"Action '{action}' is not available.")
            return available_functions["do_nothing"]()
