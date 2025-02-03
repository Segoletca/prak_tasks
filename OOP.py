# Родительский класс.
class MeleeWeapon:

    # Конструктор родительского класса.
    def __init__(self, name):
        # Свойства родительского класса: название оружия и прочность.
        self.name = name
        self.strength = 100

    # Метод родительского класса — рубящий удар.
    def slashing_blow(self):
        # При рубящем ударе уменьшаем прочность меча на 10.
        self.strength -= 10
        return f"Нанесён рубящий удар оружием {self.name}."

    # Метод родительского класса — заточка оружия.
    def sharpen(self):
        # При заточке восстанавливаем стартовую прочность оружия.
        self.strength = 100
        return f'Оружие "{self.name}" заточено.'


class Axe(MeleeWeapon):

    def __init__(self, name, material):
        super().__init__(name)
        self.material = material

    # Объявляем собственный для класса Axe метод.
    def slashing_blow(self):
        # Описываем логику работы метода дочернего класса.
        print("СОКРУШИТЕЛЬНЫЙ УДАР!")
        # Возвращаем результат выполнения метода slashing_blow()
        # в родительском классе.
        return super().slashing_blow()


# brodex = Axe('Верный', 'железо')

# print(brodex.slashing_blow())

print("HDSF".lower().__doc__)
