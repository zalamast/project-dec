"""Смотрите ниже"""
from customtkinter import *

class UnixTimeStamp(CTk):
    def __init__(self):
        super().__init__()
        self.title("Unix_timestamp")
        self.geometry("400x400")

        self._title_label = CTkLabel(self, text="Ваш текст:")
        self._text_label = CTkLabel(self, text="(C) Oreshnik team 2024")
        #self.field_user

        self._title_label.grid(row=0, column=0, pady=5)

        self._text_label.grid(row=2, column=0, padx=5, pady=5)


if __name__ == "__main__":
    UnixTimeStamp().mainloop()
#def perform_command() -> None:
 #   """Получение текущего таймштампа и вывод даты из пользовательского."""
#    timestamp: float = datetime.now().timestamp()
#    print(timestamp)
#    users_timestamp: str = input("Ваш таймштамп:")
#    users_date = float(users_timestamp)
#    users_date = datetime.fromtimestamp(users_date)
#    print("Текущая дата:" + str(users_date))
