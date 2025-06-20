# from game_contracts.game_logic_interface import GameLogicABC
from src.game_logic.game_config import available_functions
from src.game_logic.game_load_save import GameLoadSave


class SampleGameLogic:
    def __init__(self):
        self.game_over = False
        self.game_state = {}
        self.game_load_save = GameLoadSave()

    def is_game_over(self) -> bool:
        return self.game_over

    def initialize_game_state(self, requesting_player_id, new_game) -> dict[str, str]:
        if new_game:
            self.game_state = self.game_load_save.build_new_game_state(
                requesting_player_id
            )
        else:
            return self.game_load_save.get_ongoing_game_choices(requesting_player_id)
        return self.report_current_game_state()

    def report_current_game_state(self) -> dict[str, str]:
        return self.game_state

    def update_game_state(self): ...

    def get_current_player(self) -> int: ...

    def get_available_actions(self, player_id: int) -> list[dict[str, str]]: ...

    def apply_action(self, action, player_id: str) -> None: ...

    def post_turn_cleanup(self, player_id: int) -> None: ...

    def handle_input(self, input_data):

        player_id = input_data.get("player_id")
        action = input_data.get("action")

        if action in available_functions:
            self.apply_action(action, player_id)
            return available_functions[action]()
        else:
            print(f"Action '{action}' is not available.")
            return available_functions["do_nothing"]()
