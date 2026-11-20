import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def win_rate(wins, total):
    return f"{int(wins / total * 100)}%" if total else "0%"