from customtkinter import *
from time import *


class ColorsWindow(CTk):
    def __init__(self):
        super().__init__()
        self.title("About")
        self.geometry("400x400")

        def get_rgb(rgb):
            return "#%02x%02x%02x" % rgb

        def color_TB_get():
            self._label_.configure(bg_color=get_rgb((int(self._TB_1.get("0.0", "end")),
                                                     int(self._TB_2.get("0.0", "end")),
                                                     int(self._TB_3.get("0.0", "end")))))

        self._label_ = CTkLabel(self, bg_color=get_rgb((0, 0, 0)), text="", width=180, height=150)
        self._label_1 = CTkLabel(self, text="R", width=20, height=20, font=("TimesNewRoman", 30))
        self._label_2 = CTkLabel(self, text="G", width=20, height=20, font=("TimesNewRoman", 30))
        self._label_3 = CTkLabel(self, text="B", width=20, height=20, font=("TimesNewRoman", 30))
        self._TB_1 = CTkTextbox(self, width=40, height=20)
        self._TB_2 = CTkTextbox(self, width=40, height=20)
        self._TB_3 = CTkTextbox(self, width=40, height=20)
        self._Button = CTkButton(self, width=15, height=40, command=color_TB_get, text="Получить цвет",
                                 font=("TimesNewRoman", 16))

        self._TB_1.insert("end", "0")
        self._TB_2.insert("end", "0")
        self._TB_3.insert("end", "0")

        self._label_.place(x=5,y =5)
        self._label_1.place(x=5,y =180)
        self._label_2.place(x=5,y =220)
        self._label_3.place(x=5,y =260)
        self._TB_1.place(x=40,y =180)
        self._TB_2.place(x=40,y =220)
        self._TB_3.place(x=40,y =260)
        self._Button.place(x=5,y=300)


if __name__ == "__main__":
    ColorsWindow().mainloop()
