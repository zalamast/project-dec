from customtkinter import *
from time import *
from tkinter.colorchooser import askcolor

class ColorsWindow(CTk):
    def __init__(self):
        super().__init__()
        self.title("ColorPeaker")
        self.geometry("200x260")

        def get_rgb(rgb):
            return "#%02x%02x%02x" % rgb

        def change_color():
            colors = askcolor(title="Tkinter Color Chooser")
            self._TB_1.delete("0.0", "end")
            self._TB_1.insert("end", colors[1])
            self._label_.configure(bg_color=colors[1])

        self._label_ = CTkLabel(self, bg_color=get_rgb((0, 0, 0)), text="", width=180, height=150)
        self._TB_1 = CTkTextbox(self, width=180, height=20)
        self._Button = CTkButton(self, width=15, height=40, command=change_color, text="Открыть colorpeaker",
                                 font=("TimesNewRoman", 16))

        self._label_.place(x=5,y =5)
        self._TB_1.place(x=5,y =170)
        self._Button.place(x=5,y=210)


if __name__ == "__main__":
    ColorsWindow().mainloop()
