import json

class Game:

    def __init__(self, num_turns, width, height, start_x, start_y, hero, monsters):
        self.num_turns = num_turns
        self.width = width
        self.height = height
        self.start_x = start_x
        self.start_y = start_y
        self.hero = hero
        self.monsters = monsters
class Hero:

    def __init__(self, base_speed, base_power, base_range, level_speed_coeff, level_power_coeff, level_range_coeff):
        self.base_speed = base_speed
        self.base_power = base_power
        self.base_range = base_range
        self.level_speed_coeff = level_speed_coeff
        self.level_power_coeff = level_power_coeff
        self.level_range_coeff = level_range_coeff

class Monster:

    def __init__(self, x, y, hp, exp, gold):
        self.x = x
        self.y = y
        self.hp = hp
        self.exp = exp
        self.gold = gold

def create_game(filename):

    with open(filename) as f:
        d = json.load(f)
        num_turns = d["num_turns"]
        width = d["width"]
        height = d["height"]
        start_x = d["start_x"]
        start_y = d["start_y"]

        hero_json = d["hero"]
        base_speed = hero_json["base_speed"]
        base_power = hero_json["base_power"]
        base_range = hero_json["base_range"]
        level_speed_coeff = hero_json["level_speed_coeff"]
        level_power_coeff = hero_json["level_power_coeff"]
        level_range_coeff = hero_json["level_range_coeff"]
        hero = Hero(base_speed, base_power, base_range, level_speed_coeff, level_power_coeff, level_range_coeff)
        monsters_json = d["monsters"]
        monsters = []

        for monster_json in monsters_json:
            x = monster_json["x"]
            y = monster_json["y"]
            hp = monster_json["hp"]
            exp = monster_json["exp"]
            gold = monster_json["gold"]
            monster = Monster(x, y, hp, exp, gold)
            monsters.append(monster)

        game = Game(num_turns, width, height, start_x, start_y, hero, monsters)

        return game

game = create_game("001.json")
