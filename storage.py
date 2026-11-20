import os
import json
from config import WIN, QUIT

def load_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    return {"players": {}}

def save_data(data, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def save_records(user_name, game_status, target, guessed_numbers, level, file_path, score):
    data = load_data(file_path)
    if user_name not in data['players']:
        data['players'][user_name] = {'total_games': 0, 'wins': 0, 'losses': 0, 'total_score':0, 'history':[]}
    player = data['players'][user_name]

    game = {"game_id": len(player['history']) + 1,
                        "secret_number": target,
                        "attempts": len(guessed_numbers),
                        "guessed_numbers": guessed_numbers,
                        "level": level,
                        "score": score,
                        "result": game_status}
    player['history'].append(game)

    player['total_games'] += 1
    player['total_score'] += (score)
    if game_status == WIN:
        player['wins'] += 1
    if game_status == 'lose' or game_status == QUIT :
        player['losses'] += 1

    save_data(data, file_path)

def get_player_data(user_name, file_path):
    data = load_data(file_path)
    if user_name in data['players'].keys():
        return data['players'][user_name]