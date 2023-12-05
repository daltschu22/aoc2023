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
        color_max = {'blue': 0, 'red': 0, 'green': 0}
        for part in contents.split(';'):
            part_data = {}
            pairs = part.split(',')
            for pair in pairs:
                number, color = pair.strip().split()
                if int(number) > color_max[color]:
                    color_max[color] = int(number)

            # print(color_max)
            all_games[game_number] = color_max


    return all_games


MAX = {
    'red': 12,
    'blue': 14,
    'green': 13,
}

def main():
    input = read_input('input.txt')

    all_games = parse_games(input)

    total_pow = 0
    for game in all_games:
        # print(all_games[game])
        pow = all_games[game]['red'] * all_games[game]['blue'] * all_games[game]['green']
        
        total_pow += pow
            

    print(total_pow)
# 


if __name__ == "__main__":
    main()
