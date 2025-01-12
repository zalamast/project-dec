import customtkinter as ctk
import tkinter

from utils import center


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

def convert():
    try:
        o = int(radio_var.get())  # Получаем выбор пользователя: 0 или 1
        if o == 1:
            # Перевод из 10 -> любая(2-36)
            number = int(number_input.get())
            target_base = int(base_input.get())
            result = dec_to_base(number, target_base)
            result_label.configure(text=f"Результат: {result} (в {target_base}-й системе)")
        elif o == 0:
            # Перевод из любой(2-36) -> 10
            number = number_input.get()
            source_base = int(base_input.get())
            result = from_base_to_decimal(number, source_base)
            result_label.configure(text=f"Результат: {result} (в десятичной системе)")
        else:
            result_label.configure(text="Неверный выбор программы. Введите 0 или 1.")
    except ValueError as e:
        result_label.configure(text=f"Ошибка: {e}")


def radiobutton_event():
    print("radiobutton toggled, current value:", radio_var.get())


def start_window():
    global radio_var, number_input, base_input, result_label
    root = ctk.CTk()
    radio_var = tkinter.IntVar(value=0)
    # Заголовок
    root.title("Конвертер СС")
    # Размещение элементов
    frame = ctk.CTkFrame(root)
    center(root, 600, 600)
    frame.pack(padx=20, pady=20)
    radiobutton_1 = ctk.CTkRadioButton(frame, text="10 -> Any", variable=radio_var, value=1)
    radiobutton_2 = ctk.CTkRadioButton(frame, text="Any -> 10", variable=radio_var, value=0)
    radiobutton_1.grid(row=0, column=0, padx=10, pady=5)
    radiobutton_2.grid(row=0, column=1, padx=10, pady=5)
    # Поле для выбора программы (0 или 1)
    # o_input_label = ctk.CTkLabel(frame, text="Выбери программу (1 = 10 -> любая(2-36); 0 = любая(2-36) -> 10):")
    # o_input_label.grid(row=0, column=0, padx=10, pady=5)
    #
    # o_input = ctk.CTkEntry(frame)
    # o_input.grid(row=0, column=1, padx=10, pady=5)
    # Поле для ввода числа
    number_input_label = ctk.CTkLabel(frame, text="Введите число:")
    number_input_label.grid(row=1, column=0, padx=10, pady=5)
    number_input = ctk.CTkEntry(frame)
    number_input.grid(row=1, column=1, padx=10, pady=5)
    # Поле для ввода основания СС
    base_input_label = ctk.CTkLabel(frame, text="Введите основание системы счисления (2-36):")
    base_input_label.grid(row=2, column=0, padx=10, pady=5)
    base_input = ctk.CTkEntry(frame)
    base_input.grid(row=2, column=1, padx=10, pady=5)
    # Кнопка для запуска конвертации
    convert_button = ctk.CTkButton(frame, text="Конвертировать", command=convert)
    convert_button.grid(row=3, column=0, columnspan=2, pady=10)
    # Метка для вывода результата
    result_label = ctk.CTkLabel(frame, text="Результат: ")
    result_label.grid(row=4, column=0, columnspan=2, pady=10)
    # Запуск окна
    root.mainloop()


if __name__ == '__main__':
    start_window()
