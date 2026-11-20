import msvcrt
import sys

from utils import clear_terminal, win_rate
from storage import load_data
from config import QUIT, QUIT_INPUT, WIN, LOSE

def get_username():
    while True:
        user_name = input("Please enter your name: ").strip()

        if user_name:
            clear_terminal()
            return user_name

        print("Name cannot be empty!")

def show_goodbye(user_name):
    clear_terminal()
    print(f'Goodbye {user_name}...')
    sys.exit()

def show_menu(user_name):
    clear_terminal()
    
    print(f'==== Welcome {user_name} ====')    
    print("1. Start the game")
    print("2. Leaderboard (records)")
    print(f"3. {user_name}'s profile")
    print("4. change player")
    print("5. Exit")

def wait_for_key(message="Press any key to return to the main menu...."):
    print()
    print(message)
    msvcrt.getch()

def show_player_profile(user_name, player_data, history_size):
    clear_terminal()
    if player_data:
            player_last_games = player_data['history'][-history_size:][::-1]
    print(f"==== {user_name}'s profile ====")
    if player_data:
        print(f"Total games: {player_data['total_games']}, " +
                f"Wins: {player_data['wins']}, "+
                f"Losses: {player_data['losses']}, "+
                f"Win rate: {win_rate(player_data['wins'], player_data['total_games'])}, "+
                f"Total score: {player_data['total_score']}, ")
        print(f"Last {len(player_last_games)} plays:")
        print(f"\t{'ID':<8}{'Target':<12}{'Attempts':<12}{'Level':<12}{'Result':<12}{'Score'}")
        for i,val in enumerate(player_last_games):
            print(f"\t{(i + 1):<8}"f"{val['secret_number']:<12}"f"{val['attempts']:<12}"f"{val['level']:<12}"f"{val['result']:<12}"f"{val['score']}")
    else:
        print("\tNothing in here!!")
    wait_for_key()

def select_option(bottom, top):
    while True:
        try:
            print()
            option = input(f"Select an option [{bottom}-{top}]: ")
            if bottom <= int(option) <= top:
                break
            else:
                print("Invalid input, please try again..")

        except ValueError:
            print("Invalid input, please try again..")
    return int(option)

def show_leaderboard(file_path):
    clear_terminal()
    print(f"==== Leaderboard ====")
    data = load_data(file_path)
    players = data['players']
    sorted_players = sorted(players.items(),key=lambda player: player[1]["total_score"],reverse=True)
    print(f"{'Rank':<8}{'Player':<12}{'Games':<12}{'Wins':<12}{'Win Rate':<12}{'Total score'}")
    for i,val in enumerate(sorted_players):
        info = val[1]
        print(f"{(i + 1):<8}"f"{val[0]:<12}"f"{info['total_games']:<12}"f"{info['wins']:<12}"+
              f"{win_rate(info['wins'],info['total_games']):<12}"f"{info['total_score']}")

    wait_for_key()

def difficulty_menu(difficulties):
    clear_terminal()
    print(f'==== New game ====')    
    for i,val in enumerate(difficulties):
        temp = difficulties.get(val)
        print(f"{i+1}. {val} (range: [{temp[0]}-{temp[1]}], opportunities: {temp[2]}, base score: {temp[3]})")
    print(f"{len(difficulties)+1}. Back to main menu")

    choice = select_option(1,len(difficulties)+1)
    return choice

def user_input(bottom, top, used_numbers):
    while True:
        try:
            option = input(f"Select a number between [{bottom}-{top}]: ")
            option = int(option)
            if bottom <= option <= top: 
                if not option in used_numbers:
                    break
                print(f'You have already tried the number {option}.')
            else:
                if option == QUIT_INPUT:
                    return QUIT
                print(f"Not in the range [{bottom}-{top}], please try again..")

        except ValueError:
            print("Just number, please try again..")
    return option

def show_result(status, guessed_numbers, target):
    clear_terminal()
    if status == WIN:
        print(f'Well done, {target} is correct. You made it after {len(guessed_numbers)} gusses.')
        print("Guessed numbers:", ", ".join(map(str, guessed_numbers)))
    elif status == LOSE:
        print("Oops.. Your chances have run out.")
        print(f"The correct number was {target}.")
    elif status == QUIT:
        print("You quit..")
        print(f"The correct number was {target}.")

    wait_for_key()