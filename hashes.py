"""Hashes"""
from customtkinter import *
from hashlib import *


class Hashes(CTk):
    """Окно с хешами"""
    def __init__(self):
        """Ну это ИНИТ, что тут говорить"""
        super().__init__()
        self.title("HASHES")
        self.geometry("663x400")

        def perform_command() -> None:
            """Тут всё указывает на то,что делает эта несчастная функция"""
            self._TB_1.delete("0.0", "end")
            self._TB_2.delete("0.0", "end")
            text: str = self._TB_.get("0.0", "end")
            text_md5 = md5(text.encode()).hexdigest()
            self._TB_1.insert("end", f"{text_md5}")
            text_sha256 = sha256(text.encode()).hexdigest()
            self._TB_2.insert("end", f"{text_sha256}")

        self._label_ = CTkLabel(self, text="Ваш текст", font=("TimesNewROman", 25))
        self._label_1 = CTkLabel(self, text="SHA256", font=("TimesNewROman", 25))
        self._label_2 = CTkLabel(self, text="MD5", font=("TimesNewROman", 25))
        self._TB_ = CTkTextbox(self)
        self._TB_1 = CTkTextbox(self)
        self._TB_2 = CTkTextbox(self)
        self.button = CTkButton(self, text="СДЕЛАТЬ", command=perform_command, width=643, height=140,
                                font=("TimesNewROman", 100))

        self._label_.place(x=50,y=10)
        self._label_2.place(x=530,y=10)
        self._label_1.place(x=290,y=10)
        self._TB_.place(x=10,y=40)
        self._TB_1.place(x=230,y=40)
        self._TB_2.place(x=450, y=40)
        self.button.place(x=10, y=250)


if __name__ == "__main__":
    Hashes().mainloop()
