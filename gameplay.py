import random

from utils import clear_terminal
from ui import user_input
from config import HIGH, LOW, WIN, LOSE, QUIT, LOSE_SCORE, QUIT_SCORE, QUIT_INPUT


def check_guess(target, guessed):
    if guessed > target:
        return HIGH
    if guessed < target:
        return LOW 

    return WIN

def calculate_score(level, attempts, game_status, difficulties):
    game_level = difficulties[level]
    if game_status == LOSE:
        return LOSE_SCORE
    elif game_status == QUIT:
        return QUIT_SCORE
    elif game_status == WIN:
        _, _, max_tries, base_score = game_level 

        efficiency = 0.5 + 0.5 * (
            (max_tries - len(attempts)) / (max_tries - 1)
        )

        return round(base_score * efficiency)
    
    return 0

def guess(level):
    clear_terminal()
    bottom, top , limit, _ = level
    target = random.randint(bottom, top)
    used_numbers = []
    lower_numbers = []
    higher_numbers = []
    while len(used_numbers) < limit:
        print(f'Remaining chances: {limit - len(used_numbers)}')
        if len(used_numbers) > 0:
            print("Lower numbers:", ", ".join(map(str, lower_numbers)))
            print("Higher numbers:", ", ".join(map(str, higher_numbers)))
        print(f"If you want to quit, enter {QUIT_INPUT}.")
        guessed = user_input(bottom, top, used_numbers)
        clear_terminal()
        if guessed == QUIT:
            status = QUIT
            break
        used_numbers.append(guessed)
        status = check_guess(target, guessed)
        if status == WIN:
            break
        if status == LOW:
            bottom = guessed + 1
            print(f'your guessed number ({guessed}) is lower..')
            lower_numbers.append(guessed) 
        if status == HIGH:
            top = guessed - 1
            print(f'your guessed number ({guessed}) is higher..')
            higher_numbers.append(guessed)
    else:
        status = LOSE
    return status, used_numbers, target