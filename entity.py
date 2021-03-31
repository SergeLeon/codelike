class Entity:
    """
    Родительский класс для каждого обьекта на карте
    """

    def __init__(self, xy, sprite="?", description="...", act_description="..."):
        self._sprite = sprite
        self._x, self._y = xy
        self._description = description
        self._act_description = act_description

    def get_xy(self):
        return self._x, self._y

    def set_xy(self, xy):
        self._x, self._y = xy

    def get_sprite(self):
        return self._sprite

    def set_sprite(self, sprite):
        self._sprite = sprite

    def get_descript(self):
        return self._description

    def get_act_descript(self):
        return self._act_description

    def action(self, user):
        """
        Взаимодействие с user
        """
        pass


class Creature(Entity):
    """
    Класс всех живых существ
    """

    def __init__(self, xy, sprite, health, attack):
        super().__init__(xy, sprite)
        self._hp = health
        self._att = attack

    def get_att(self):
        return self._att

    def get_hp(self):
        return self._hp

    def interact(self, entity: Entity):
        """
        Вызов взаимодействия с entity
        """
        entity.action(self)


class Player(Creature):
    """
    Класс игрока
    """

    def __init__(self, xy, sprite, health, mana, attack):
        super().__init__(xy, sprite, health, attack)
        self._mp = mana

    def action(self, user):
        """
        обьект player уменьшает self.hp на значение att обькта user
        """
        self._hp -= user.get_att()


class Wall(Entity):
    """
    Класс стены без взаимодействия
    """

    def action(self, user):
        pass


class Space(Entity):
    """
    Класс пустого пространства в котором можно передвигатся
    """

    def action(self, user):
        """
        Поменятся местами с user
        """
        xy1 = self.get_xy()
        xy2 = user.get_xy()
        user.set_xy(xy1)
        self.set_xy(xy2)
