from console import Console
from entity import Player
from interface import Interface
from map import Map


class Game:
    def __init__(self, map_size, hero_pos):
        self.interface = Interface(Interface.get_shell_size())
        self.cons = Console(locals())

        self.map = Map(map_size)
        self.map.generate(map_size)

        self.hero = Player(xy=hero_pos, sprite="@", health=20, mana=20, attack=1)
        self.map[hero_pos[1]][hero_pos[0]] = self.hero

    def main_loop(self):
        while True:
            page = 0
            # очистка окна командной строки
            self.interface.cmd_clear()

            self.map.refresh()

            # отрисовка в cmd
            winx, winy = Interface.get_shell_size()

            self.interface.set_size((winx, winy - 3))
            self.interface.cmd_render(self.interface.get_view_zone(self.map, self.hero.get_xy()))

            print(self.hero.get_hp(), self.hero.get_xy())

            # действия игрока
            hero_x, hero_y = self.hero.get_xy()
            hero = self.hero

            left = self.map[hero_y][hero_x - 1]
            right = self.map[hero_y][hero_x + 1]
            up = self.map[hero_y - 1][hero_x]
            down = self.map[hero_y + 1][hero_x]

            user_input = self.cons.multiline_input()

            self.cons.set_locals(locals())
            self.cons.run_code(user_input)


def main():
    game = Game((15, 15), (7, 7))

    game.main_loop()


if __name__ == "__main__":
    main()
