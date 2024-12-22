from customtkinter import *


class TextAnalysisWindow(CTk):
    def __init__(self):
        super().__init__()
        self.title("Text Analysis")
        self.geometry("410x400")

        def show_result():
            self._text_label_1.configure(text=f"Количество символов:{len("".join(self._text_Entry.get().split()))}")

        def delete():
            self._text_Entry.delete(0,len(self._text_Entry.get()))

        def quantity_of_words():
            self._text_quantity.configure(text=f"Количество символов:{len(self._text_Entry.get().split())}")

        self._title_label = CTkLabel(self, text="АНАЛИЗ ТЕКСТА", font=("TimesNewRoman", 30))
        self._text_Entry = CTkEntry(self, height=10, width=300)
        self._text_label_1 = CTkLabel(self, text="Количество символов:", font=("TimesNewRoman", 30))
        self._button_analiz = CTkButton(self, text="ПРОВЕСТИ АНАЛИЗ", command=show_result,
        width=40, height=50, font=("TimesNewRoman", 30))
        self._button_delete = CTkButton(self, text="ОЧИСТИТЬ СТРОКУ", font=("TimesNewRoman", 30),
        command=delete, height=50)
        self._button_quantity = CTkButton(self, text="КОЛИЧЕСТВО СЛОВ", font=("TimesNewRoman", 30),
        command=quantity_of_words, height=50, width=40 )
        self._text_quantity = CTkLabel(self, text="Количество слов:", font=("TimesNewRoman", 30))

        self._text_quantity.grid(row=3)
        self._button_quantity.grid(row=5, column=0)
        self._button_delete.grid(row=6, column=0)
        self._button_analiz.grid(row=4, column=0, padx=10)
        self._title_label.grid(row=0, column=0, padx=10, pady=5)
        self._text_Entry.grid(row=1, column=0, padx=10, pady=5)
        self._text_label_1.grid(row=2, column=0, padx=10)


TextAnalysisWindow().mainloop()
