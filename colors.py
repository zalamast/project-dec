from customtkinter import *


class ColorsWindow(CTk):
    def __init__(self):
        super().__init__()
        self.title("About")
        self.geometry("400x400")

        self._label_ = CTkLabel(self, bg_color="white", text="", width=180, height=150)
        self._label_1 = CTkLabel(self, text="R", width=20, height=20, font=("TimesNewRoman", 30))
        self._label_2 = CTkLabel(self, text="G", width=20, height=20, font=("TimesNewRoman", 30))
        self._label_3 = CTkLabel(self, text="B", width=20, height=20, font=("TimesNewRoman", 30))
        self._TB_1 = CTkTextbox(self, width=20, height=20)
        self._TB_2 = CTkTextbox(self, width=20, height=20)
        self._TB_3 = CTkTextbox(self, width=20, height=20)

        self._label_.grid(row=0, column=0, padx=5, pady=5)
        self._label_1.grid(row=1, column=0, padx=0, pady=5)
        self._label_2.grid(row=2, column=0, padx=0, pady=5)
        self._label_3.grid(row=3, column=0, padx=0, pady=5)
        self._TB_1.grid(row=1, column=1, padx=5, pady=5)
        self._TB_2.grid(row=2, column=1, padx=5, pady=5)
        self._TB_3.grid(row=3, column=1, padx=5, pady=5)

if __name__ == "__main__":
    ColorsWindow().mainloop()
