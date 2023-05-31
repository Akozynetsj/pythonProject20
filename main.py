#3
class ValueError(Exception):
    def __init__(self, temperature):
        self.temperature = temperature

class TemperatureConverter:
    def celsium_to_farengeit(self, celsium):
        if celsium < -273:
            raise ValueError(celsium)
        return celsium * 9/5 + 32

    def farengeit_to_celsium(self, farengeit):
        if farengeit < -460:
            raise ValueError(farengeit)
        return (farengeit - 32) * 5/9

converter = TemperatureConverter()

try:
    temp_1 = converter.celsium_to_farengeit(20)
    print(f"Температура у Фаренгейтах: {temp_1}")
except ValueError as a:
    print(f"Температура {a.temperature} нижче абсолютного нуля")

try:
    temp_2 = converter.farengeit_to_celsium(50)
    print(f"Температура у Цельсіях: {temp_2}")
except ValueError as b:
    print(f"Температура {b.temperature} нижче абсолютного нуля")#3
class ValueError(Exception):
    def __init__(self, temperature):
        self.temperature = temperature

class TemperatureConverter:
    def celsium_to_farengeit(self, celsium):
        if celsium < -273:
            raise ValueError(celsium)
        return celsium * 9/5 + 32

    def farengeit_to_celsium(self, farengeit):
        if farengeit < -460:
            raise ValueError(farengeit)
        return (farengeit - 32) * 5/9

converter = TemperatureConverter()

try:
    temp_1 = converter.celsium_to_farengeit(20)
    print(f"Температура у Фаренгейтах: {temp_1}")
except ValueError as a:
    print(f"Температура {a.temperature} нижче абсолютного нуля")

try:
    temp_2 = converter.farengeit_to_celsium(50)
    print(f"Температура у Цельсіях: {temp_2}")
except ValueError as b:
    print(f"Температура {b.temperature} нижче абсолютного нуля")