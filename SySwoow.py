"""
Программа для перевода из любой СС в любую другую (2-36)
"""
o = int(input("Выбери нужную программу: \n 1 = 10 -> любая(2-36);\n 0 = любая(2-36) -> 10 \n"))
if o == 1:
    def dec_to_base(number, base):
        """
        Перевод из 10чной в любую СС(2-36).
        """
        symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if number == 0:
            return "0"
        result = ""
        while number > 0:
            result = symbols[number % base] + result
            number //= base
        return result

    if __name__ == "__main__":
        print("Перевод из десятичной СС в любую(2-36)")
        number = int(input("Введи число в десятичной СС: "))
        target_base = int(input("Введи СС(2-36): "))

        try:
            result = dec_to_base(number, target_base)
            print(f"Число {number} в десятичной СС равно {result} в {target_base} системе СС.")
        except ValueError:
            print("Неправильный ввод. Повтори ещё раз")

elif o == 0:
    def from_base_to_decimal(number, base):
        """
        Перевод из любой(2-36) СС в десятичную.
        """
        symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        number = number.upper()
        decimal_value = 0

        for index, digit in enumerate(reversed(number)):
            if digit not in symbols[:base]:
                raise ValueError(f"Неверное число '{digit}' для {base} СС")
            decimal_value += symbols.index(digit) * (base ** index)

        return decimal_value


    if __name__ == "__main__":
        print("Из любой(2-36) в десятичную")
        number = input("Введи число: ")
        source_base = int(input("Введи его СС(2-36): "))

        try:
            result = from_base_to_decimal(number, source_base)
            print(f"Число {number} в {source_base} СС равно {result} в десятичной.")
        except ValueError as e:
            print(f"Неверный ввод: {e}")
