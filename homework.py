training_names = {
    "SWM": "Swimming",
    "RUN": "Running",
    "WLK": "SportsWalking",
}


class InfoMessage:
    """Информационное сообщение о тренировке."""

    def __init__(
        self,
        workout_type,
        duration,
        distance,
        speed,
        calories,
    ):
        self.workout_type = workout_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        return (
            f"Тип тренировки: {training_names[self.workout_type]};\n"
            f"Длительность: {self.duration:.3f} ч.;\n"
            f"Дистанция: {self.distance:.3f} км;\n"
            f"Ср. скорость: {self.speed:.3f} км/ч;\n"
            f"Потрачено ккал: {self.calories:.3f}.\n"
        )


class Training:
    """Базовый класс тренировки.
    action: int,  # количество совершённых действий.
    duration: float,  # длительность тренеровки в часах.
    weight: float,  # вес спортсмена.
    """

    def __init__(
        self,
        action: int,  # Количество совершённых действий.
        duration: float,  # Длительность тренеровки в часах.
        weight: float,  # Вес спортсмена.
    ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight
        self.M_IN_KM = 1000
        self.LEN_STEP = None
        self.TYPE = "Training"

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        self.distance = self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения в час."""
        self.get_distance()
        self.speed = self.distance / self.duration

    def get_mean_speed_m_sec(self) -> float:
        self.speed_m_sec = self.speed / 3.6

    def get_duration_min(self) -> float:
        self.duration_min = self.duration * 60

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(
            self.TYPE,
            self.duration,
            self.distance,
            self.speed,
            self.calories,
        )


class LandTraining(Training):
    """Сухопутная тренеровка."""

    def __init__(self, action, duration, weight):
        super().__init__(action, duration, weight)
        self.LEN_STEP = 0.65

        super().get_mean_speed()
        super().get_distance()
        super().get_duration_min()


class Running(LandTraining):
    """Тренировка: бег."""
    def __init__(self, action, duration, weight):
        super().__init__(action, duration, weight)

        self.TYPE = "RUN"
        self.CALORIES_MEAN_SPEED_MULTIPLIER = 18
        self.CALORIES_MEAN_SPEED_SHIFT = 1.79

    def get_spent_calories(self):
        self.calories = (
            (18 * self.speed + 1.79) * self.weight / self.M_IN_KM * self.duration_min
        )

    # def get_spent_calories(self):
    #     self.calories = (
    #         (
    #             self.CALORIES_MEAN_SPEED_MULTIPLIER
    #             * self.speed
    #             * self.CALORIES_MEAN_SPEED_SHIFT
    #         )
    #         * self.weight
    #         / self.M_IN_KM
    #         * self.duration
    #     )


class SportsWalking(LandTraining):
    """Тренировка: спортивная ходьба."""

    def __init__(self, action, duration, weight, height):
        super().__init__(action, duration, weight)
        self.height: float = height

        super().get_mean_speed_m_sec()
        super().get_duration_min()

        self.TYPE = "WLK"
        self.COEFFICIENTS = (0.035, 0.029)

    def get_spent_calories(self):
        # self.calories = ((0.035 * self.weight + (self.speed_m_sec**2 / self.height) * 0.029 * self.weight) * self.duration_min)
        self.calories = (
            self.COEFFICIENTS[0] * self.weight
            + (self.speed_m_sec**2 / self.height) * self.COEFFICIENTS[1] * self.weight
        ) * self.duration_min


class Swimming(Training):
    """Тренировка: плавание."""

    def __init__(self, action, duration, weight, length_pool, count_pool):
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool
        self.LEN_STEP = 1.38
        self.TYPE = "SWM"

        super().get_distance()

    def get_mean_speed(self):
        self.speed = self.length_pool * self.count_pool / self.M_IN_KM / self.duration

    def get_spent_calories(self):
        self.get_mean_speed()

        self.calories = (self.speed + 1.1) * 2 * self.weight * self.duration


def read_package(workout_type: str, data: list[int]) -> Training | str:
    """Прочитать данные полученные от датчиков."""
    training = "Неизвестный тип тренеровки"
    if workout_type.upper() == "RUN":
        run = Running(*data)
        run.get_spent_calories()
        training = run

    if workout_type.upper() == "WLK":
        wlk = SportsWalking(*data)
        wlk.get_spent_calories()
        training = wlk

    if workout_type.upper() == "SWM":
        swm = Swimming(*data)
        swm.get_spent_calories()
        training = swm

    return training


# , workout_type: str
def main(training: Training | str) -> None:
    """Главная функция."""
    info: InfoMessage = training.show_training_info()
    print(info.get_message())


if __name__ == "__main__":
    packages = [
        ("SWM", [720, 1, 80, 25, 40]),
        ("RUN", [15000, 1, 75]),
        ("WLK", [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
