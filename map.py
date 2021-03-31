from entity import *


class Map:
    """
    Класс генератора карты
    """

    def __init__(self, size):
        self._xsize, self._ysize = size

        self._map = []

    def __getitem__(self, key):
        return self._map[key]

    def __len__(self):
        return len(self._map)

    def get_size(self):
        return self._xsize, self._ysize

    def insert(self, obj, center):
        """
        Вставка обьекта на определенный участок карты по указанному центру
        """
        sizey = len(obj)
        sizex = len(obj[0])

        x1 = center[0] - sizex // 2
        y1 = center[1] - sizey // 2

        x2 = center[0] + sizex // 2
        y2 = center[1] + sizey // 2

        if sizex % 2 != 0: x2 += 1
        if sizey % 2 != 0: y2 += 1

        for objy, mapy in enumerate(range(y1, y2)):
            for objx, mapx in enumerate(range(x1, x2)):
                self._map[mapy][mapx] = obj[objy][objx]

    @staticmethod
    def create_room(size):
        """
        Возвращает список комнаты окруженной стенами
        """
        xsize, ysize = size
        room = [[Wall(sprite="#", xy=[x, 0]) for x in range(xsize)],
                [Wall(sprite="#", xy=[x, ysize - 1]) for x in range(xsize)]]

        for y in range(1, ysize - 1):
            room.insert(y, [Wall(sprite="#", xy=[0, y])]
                        + [Space(sprite=".", xy=[x, y]) for x in range(1, xsize - 1)]
                        + [Wall(sprite="#", xy=[xsize, y])])

        return room

    def generate(self, size):
        """
        Возвращает сгенерированную карты заданного размера
        """
        self._xsize, self._ysize = size

        clear_map = [[Space(sprite=".", xy=[x, y]) for x in range(self._xsize)] for y in range(self._ysize)]

        self._map = clear_map

        self.insert(self.create_room(size), [num // 2 for num in size])

    def refresh(self):
        """
        Устанавливает каждый Entity на свое место на карте
        """
        new_map = [[] for _ in range(self._ysize)]
        for line in self._map:
            for entity in line:
                x, y = entity.get_xy()
                new_map[y].insert(x, entity)
        self._map = new_map
