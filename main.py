# Створіть клас температурного датчика, де обмежується
# температура в межах прийнятних для датчика значень, за
# допомогою property().

class Temperature:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    def current_temperature(self):
        if 50 > self._temperature > -50:
            print(f"Current temperature is: {self._temperature}")
        elif self._temperature > 50:
            print(f"Temperature '{self._temperature}' is to high.")
        elif self._temperature < -50:
            print(f"Temperature '{self._temperature}' is to low.")

temperature = Temperature(23)
temperature.current_temperature()





