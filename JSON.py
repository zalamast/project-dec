from json import *
from customtkinter import *
from pyperclip import *

class TextAnalysisWindow(CTk):
    def __init__(self):
        super().__init__()
        self.title("Text Analysis")
        self.geometry("410x400")

        def any_to_Json():
            self._text_label_1.configure(text=dumps(list(self._text_Entry.get())))


        self._title_label = CTkLabel(self, text="JSON", font=("TimesNewRoman", 45))
        self._text_Entry = CTkEntry(self, height=100, width=400)
        self._text_label_1 = CTkLabel(self, height=100, width=400, text="", bg_color="black",
                                      text_color="white")
        self._button_anal = CTkButton(self, text="ПРОВЕСТИ АНАЛИЗ", command=any_to_Json,
        width=50, height=50, font=("TimesNewRoman", 20))

        self._button_anal.grid(row=2, column=0, padx=5)
        self._title_label.grid(row=0, column=0, padx=5, pady=5)
        self._text_Entry.grid(row=1, column=0, padx=5, pady=5)
        self._text_label_1.grid(row=3, column=0, padx=5, pady=5)

TextAnalysisWindow().mainloop()