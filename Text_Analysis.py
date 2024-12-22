from customtkinter import *


class TextAnalysisWindow(CTk):
    def __init__(self):
        super().__init__()
        self.title("Text Analysis")
        self.geometry("410x400")

        def analiz():
            result = len("".join(self.Textbox.get("0.0", "end").split()))
            self._text_label_1.configure(text=f"Количество символов:{result}")
            self._text_quantity.configure(text=f"Количество слов:"
                                               f"{len(self.Textbox.get("0.0", "end").split())}")
        def delete():
            self.Textbox.delete("0.0", "end")

        self._title_label = CTkLabel(self, text="АНАЛИЗ ТЕКСТА", font=("TimesNewRoman", 45))
        self.Textbox = CTkTextbox(self, height=10, width=300)
        self._text_label_1 = CTkLabel(self, text="Количество символов:", font=("TimesNewRoman", 30))
        self._button_analiz = CTkButton(self, text="ПРОВЕСТИ АНАЛИЗ", command=analiz,
        width=40, height=50, font=("TimesNewRoman", 30))
        self._button_delete = CTkButton(self, text="ОЧИСТИТЬ СТРОКУ", font=("TimesNewRoman", 30),
        command=delete, height=50)
        self._text_quantity = CTkLabel(self, text="Количество слов:", font=("TimesNewRoman", 30))

        self.rowconfigure(index=0, weight=1)
        self.rowconfigure(index=1, weight=10)
        self.rowconfigure(index=2, weight=1)
        self.rowconfigure(index=3, weight=1)
        self.rowconfigure(index=4, weight=1)
        self.rowconfigure(index=5, weight=1)
        self.rowconfigure(index=6, weight=1)
        self.columnconfigure(index=0, weight=1)


        self._text_quantity.grid(row=3)
        self._button_delete.grid(row=6, column=0, sticky="ns")
        self._button_analiz.grid(row=4, column=0, padx=10, sticky="ns")
        self._title_label.grid(row=0, column=0, padx=10, pady=5)
        self.Textbox.grid(row=1, column=0, padx=10, pady=5, sticky="nswe")
        self._text_label_1.grid(row=2, column=0, padx=10)
