
from utils import clear_terminal
from storage import save_records, get_player_data
from ui import (get_username, show_menu, show_player_profile, select_option,
                show_leaderboard, difficulty_menu, show_result, show_goodbye)
from gameplay import guess, calculate_score

from config import FILE_PATH, DIFFICULTIES, HISTORY_SIZE


def game(user_name, difficulties, file_path, history_size):
    while True:
        player_data = get_player_data(user_name, file_path)
        show_menu(user_name)
        choice = select_option(1,5)
        if choice == 1:
            d_option = difficulty_menu(difficulties)
            if d_option == (len(difficulties) + 1):
                continue
            else:
                level = list(difficulties.keys())[d_option-1]
                game_status, guessed_numbers, target = guess(difficulties.get(level))
                show_result(game_status, guessed_numbers, target)
                score = calculate_score(level, guessed_numbers, game_status, difficulties)
                save_records(user_name, game_status, target, guessed_numbers, level, file_path, score)
        elif choice == 2:
            show_leaderboard(file_path)
        elif choice == 3:
            show_player_profile(user_name, player_data, history_size)
        elif choice == 4:
            user_name = get_username()
        elif choice == 5:
            show_goodbye(user_name)


if __name__ == "__main__":
    user_name = get_username()
    game(user_name, DIFFICULTIES, FILE_PATH, HISTORY_SIZE)