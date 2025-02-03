# questions = {
#     "Марина": "Держись, всё получится. Хочешь видео с котиками?"
# }

class Human:
    def __init__(self, name):
        self.name = name
    # ответ по умолчанию для всех одинаковый, можно
    # доверить его родительскому классу

    def answer_question(self, question: str):
        print("Очень интересный вопрос! Не знаю.")


class Student(Human):
    def ask_question(self, someone: Human, question: str):
        # напечатайте на экран вопрос в нужном формате
        print(someone.name + ", " + question)
        # запросите ответ на вопрос у someone
        someone.answer_question(question)
        print()  # этот print выводит разделительную пустую строку


class Curator(Human):
    def answer_question(self, question: str):
        if question == "мне грустненько, что делать?":
            print("Держись, всё получится. Хочешь видео с котиками?")
        else:
            super().answer_question(question)
        # здесь нужно проверить, пришёл куратору знакомый вопрос или нет
        # если да - ответить на него
        # если нет - вызвать метод answer_question() у родительского класса


class CodeReviewer(Human):
    def answer_question(self, question: str):
        if question == "что не так с моим проектом?":
            print("О, вопрос про проект, это я люблю.")
        else:
            super().answer_question(question)


class Mentor(Human):
    def answer_question(self, question: str):
        if question == "мне грустненько, что делать?":
            print("Отдохни и возвращайся с вопросами по теории.")
        elif question == "как устроиться работать питонистом?":
            print("Сейчас расскажу.")
        else:
            super().answer_question(question)


# следующий код менять не нужно, он работает, мы проверяли
student1 = Student('Тимофей')
curator = Curator('Марина')
mentor = Mentor('Ира')
reviewer = CodeReviewer('Евгений')
friend = Human('Виталя')

student1.ask_question(curator, 'мне грустненько, что делать?')
student1.ask_question(mentor, 'мне грустненько, что делать?')
student1.ask_question(reviewer, 'когда каникулы?')
student1.ask_question(reviewer, 'что не так с моим проектом?')
student1.ask_question(friend, 'как устроиться на работу питонистом?')
student1.ask_question(mentor, 'как устроиться работать питонистом?')
