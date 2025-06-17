from game_contracts.game_logic_interface import GameLogicABC
from src.game_logic.game_config import available_functions


class SampleGameLogic:
    def __init__(self):
        super().__init__()

    def setup_game_state(self, game_state: dict) -> None: ...

    def build_new_game_state(self) -> dict: ...

    def is_game_over(self) -> bool: ...

    def get_current_player(self) -> int: ...

    def get_available_actions(self, player_id: int) -> list[dict[str, str]]: ...

    def apply_action(self, input_player: str) -> None: ...

    def report_game_state(self) -> dict[str, str]: ...

    def post_turn_cleanup(self, player_id: int) -> None: ...

    def update_game_state(self):

        new_game_state = self.report_game_state()

        game_state_diff = {
            x: y for x, y in new_game_state.items() if self.game_state.get(x) != y
        }

        # Placeholder for actual logic to push game state to client
        # This should be replaced with the actual implementation
        print("Pushing game state to client:", game_state_diff)

        self.game_state = new_game_state

    def handle_out_of_turn(self, input_data):
        pass
        self.update_game_state()

    def handle_input(self, input_data):

        input_player = input_data.get("player_id")
        action = input_data.get("action")

        if action in available_functions:
            self.apply_action(action, input_player)
            return available_functions[action]()
        else:
            print(f"Action '{action}' is not available.")
            return available_functions["do_nothing"]()
