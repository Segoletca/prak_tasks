class Bird:

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def describe(self, full=False):
        """Описание птицы в формате строки."""
        return f"Размер птицы {self.name} — {self.size}."


class Parrot(Bird):

    def __init__(self, name, size, color):
        super().__init__(name, size)
        self.color = color

    def describe(self, full=False):
        """Описание птицы в формате строки."""
        if full:
            return f"""\tПопугай {self.name} — заметная птица,
        окрас её перьев — {self.color}, а размер — {self.size}.
        Интересный факт: попугаи чувствуют ритм, а вовсе не бездумно
        двигаются под музыку. Если сменить композицию,
        то и темп движений птицы изменится.
        """
        return super().describe()

    def repeat(self, phrase: str):
        return f"Попугай {self.name} говорит: " f"{phrase}"


class Penguin(Bird):

    def __init__(self, name, size, genus):
        super().__init__(name, size)
        self.name = self.name
        self.genus = genus

    def describe(self, full=False):
        """Описание птицы в формате строки."""
        if full:
            return f"""\tРазмер пингвина {self.name} из рода {self.genus} —
        {self.size}. Интересный факт: однажды группа геологов-разведчиков
        похитила пингвинье яйцо, и их принялась преследовать вся стая,
        не пытаясь, впрочем, при этом нападать. Посовещавшись,
        похитители вернули птицам яйцо, и те отстали.
        """
        return super().describe()

    def swimming(self):
        return f"{self.name} пингвин плавает со средней скоростью 11 км/ч."


kesha = Parrot("Кеша", "средний", "зеленый")
penguin = Penguin("Королевский", "большой", "Aptenodytes")

print(kesha.describe(True))
print()
print(penguin.describe(True))


print(kesha.repeat("Кеша хороший!"))
print(penguin.swimming())
