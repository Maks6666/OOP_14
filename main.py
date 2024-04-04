# Завдання для функторів. Створіть клас TextModifier,
# який може здійснювати різні операції над текстом:
# • Операція перетворення тексту у верхній регістр.
# • Операція перетворення тексту у нижній регістр.
# • Операція видалення пробілів у тексті.
# • Операція шифрування тексту за допомогою зсуву
# вліво на задану кількість символів

class TextModifier:
    def __init__(self, text):
        self.text = text

    def __call__(self, operation):
        if operation == "upper":
            return self.text.upper()
        elif operation == "lower":
            return self.text.lower()
        elif operation == "remove_spaces":
            return self.text.replace(" ", "")


text = "Hello, World!"
modifier = TextModifier(text)

result = modifier("upper")
print(result)


result = modifier("lower")
print(result)


result = modifier("remove_spaces")
print(result)








