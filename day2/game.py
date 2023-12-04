#!/usr/bin/env python3

def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()
    

def parse_games(input):
    all_games = {}
    for line in input:
        game, contents = line.split(':')
        game_number = int(game.strip().split()[1])

        game_parts = []
        for part in contents.split(';'):
            part_data = {}
            pairs = part.split(',')
            for pair in pairs:
                number, color = pair.strip().split()
                part_data[color] = int(number)
            game_parts.append(part_data)

        all_games[game_number] = game_parts

    return all_games


MAX = {
    'red': 12,
    'blue': 14,
    'green': 13,
}

def main():
    input = read_input('input.txt')

    all_games = parse_games(input)

    valid_games = []
    for game_number, parts in all_games.items():
        for part in parts:
            if any(part.get(color, 0) > MAX[color] for color in MAX):
                break
        else:
            valid_games.append(game_number)

    total = sum(valid_games)

    print(total)



if __name__ == "__main__":
    main()
