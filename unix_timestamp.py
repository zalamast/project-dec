"""Смотрите ниже"""
import time
from customtkinter import *
from datetime import *


class UnixTimeStamp(CTk):
    def __init__(self):
        super().__init__()
        self.title("Unix_timestamp")
        self.geometry("450x400")

        def show_timestamp() -> None:
            """Получение текущего таймштампа и вывод даты из пользовательского."""
            users_timestamp: str = self.field_user.get("0.0","end")
            users_date = float(users_timestamp)
            users_date = datetime.fromtimestamp(users_date)
            self._text_date_from_timestamp.configure(text="Текущая дата:" + str(users_date))

        self._label_1 = CTkLabel(self, text="Unix Timestamp", font=("TimesNewRoman", 50) )
        self._title_label = CTkLabel(self, text="Текущий Unix timestamp:", font=("TimesNewRoman", 30) )
        self._text_timestamp = CTkLabel(self, text=f"{datetime.now().timestamp()}", font=("TimesNewRoman", 20))
        self.field_user = CTkTextbox(self, height=40, width=300)
        self._text_date_from_timestamp = CTkLabel(self, text="Ваша дата:", font=("TimesNewRoman", 23))
        self._button = CTkButton(self, text="ВЫВЕСТИ ВАШУ ДАТУ", command=show_timestamp, height=50, width=200,
                                 font=("TimesNewRoman", 30))

        self._label_1.pack()
        self._title_label.pack(pady=10)
        self._text_timestamp.pack()
        self.field_user.pack(pady=20)
        self._button.pack()
        self._text_date_from_timestamp.pack()


if __name__ == "__main__":
    UnixTimeStamp().mainloop()
