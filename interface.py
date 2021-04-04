import os
from ctypes import windll, create_string_buffer
from struct import unpack


class Interface:
    """
    Класс пользовательского интерфейса
    """

    def __init__(self, size):
        self._sizex, self._sizey = size
        self.render_buffer = [[]]

    def set_size(self, size):
        self._sizex, self._sizey = size

    def get_size(self):
        return self._sizex, self._sizey


    @staticmethod
    def get_shell_size():
        """
        Возвращает размер командной строки в символах
        """
        h = windll.kernel32.GetStdHandle(-12)
        csbi = create_string_buffer(22)
        res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)

        if res:
            (bufx, bufy, curx, cury, wattr,
             left, top, right, bottom, maxx, maxy) = unpack("hhhhHhhhhhh", csbi.raw)
            sizex = right - left + 1
            sizey = bottom - top + 1
        else:
            sizex, sizey = 80, 25
        return [sizex, sizey]

    @staticmethod
    def cmd_render(smf):
        """
        Отрисовка спрайтов 2-x мерного списка в командную строку
        При ошибке отрисовывает " "
        """
        for y in smf:
            for x in y:
                if isinstance(x, str):
                    print(x)
                else:
                    try:
                        print(x.get_sprite(), end="")
                    except:
                        print(" ", end="")
            print("")


    @staticmethod
    def cmd_clear():
        """
        Очистка cmd/shell окна
        """
        os.system('cls||clear')

    @staticmethod
    def inspect(entity):
        return entity.about()

    def render(self):
        pass

    def get_view_zone(self, gmap, center):
        """
        Возвращает фрагмент карты заданного размера с выбранным центром
        """

        x1 = center[0] - self._sizex // 2
        y1 = center[1] - self._sizey // 2

        x2 = center[0] + self._sizex // 2
        y2 = center[1] + self._sizey // 2

        zone = []
        for y in range(y1, y2):
            zone_buf = []
            for x in range(x1, x2):
                if x >= 0 and y >= 0:
                    try:
                        zone_buf.append(gmap[y][x])
                    except:
                        zone_buf.append(None)
                else:
                    zone_buf.append(None)
            zone.append(zone_buf)

        return zone
