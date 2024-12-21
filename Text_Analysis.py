from customtkinter import *


class TextAnalysisWindow(CTk):
    def __init__(self):
        super().__init__()
        self.title("Text Analysis")
        self.geometry("410x400")

        def show_what_you_need():
            self._text_label_1.configure(text=f"Количество символов:{len(self._text_Entry.get())}")

        self._title_label = CTkLabel(self, text="АНАЛИЗ ТЕКСТА", font=("TimesNewRoman", 45))
        self._text_Entry = CTkEntry(self, height=10, width=400)
        self._text_label_1 = CTkLabel(self, text="Количество символов:", font=("TimesNewRoman", 25))
        self._button_anal = CTkButton(self, text="ПРОВЕСТИ АНАЛИЗ", command=show_what_you_need,
        width=50, height=50, font=("TimesNewRoman", 20))

        self._button_anal.grid(row=3, column=0, padx=5)
        self._title_label.grid(row=0, column=0, padx=5, pady=5)
        self._text_Entry.grid(row=1, column=0, padx=5, pady=5)
        self._text_label_1.grid(row=2, column=0, padx=5)


TextAnalysisWindow().mainloop()
