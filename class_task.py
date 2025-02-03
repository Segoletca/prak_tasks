import time


# Объявите класс Quest с методами и свойствами.
class Quest:

    def __init__(self, name=None, description=None, goal=None):
        self.name = name
        self.description = description
        self.goal = goal

        self.time_start: float = None
        self.time_end: float = None

    def __str__(self):
        message = f"Цель квеста {self.name} - {self.goal}"

        if self.time_start:
            if self.time_end:
                return message + " Квест завершён."
            return message + " Квест выполняется."

        return message

    def accept_quest(self) -> str:
        """Получить квест."""
        if self.time_end:
            return "С этим испытанием вы уже справились."

        self.time_start = time.time()
        return f'Начало "{self.name}" положено.'

    def pass_quest(self) -> str:
        """Завершить квест."""
        if not self.time_start:
            return "Нельзя завершить то, что не имеет начала!"
        self.time_end = time.time()
        self.completion_time = self.time_end - self.time_start
        return (
            f'Квест "{self.name}" окончен. '
            f"Время выполнения квеста: {self.completion_time:.0f} сек."
        )


# В этих переменных содержатся значения, которые нужно передать
# в качестве аргументов в экземпляр класса Quest.
quest_name = "Сбор пиксельники"
quest_goal = "Соберите 12 ягод пиксельники."
quest_description = """
В древнем лесу Кодоборье растёт ягода "пиксельника".
Она нужна для приготовления целебных снадобий.
Соберите 12 ягод пиксельники."""


# Создайте экземпляр класса Quest.
new_quest = Quest(quest_name, quest_description, quest_goal)


print(new_quest.pass_quest())
print(new_quest.accept_quest())

time.sleep(3)

print(new_quest.pass_quest())
print(new_quest.accept_quest())

print(new_quest)
