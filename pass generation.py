"""nfiviiibv"""
import json
import re
from collections.abc import generator
from operator import length_hint
from tkinter import messagebox

import random
from customtkinter import *


class passgenerationWindow(CTk):
    """JSON to YAML window"""

    def __init__(self):
        """Create window and UI"""
        super().__init__()
        self.title("passgeneration")
        self.geometry("600x200")

        font = ("Consolas", 18, "normal")

        self._entry = CTkEntry(self, )
        self._button = CTkButton(
            self,
            text="НАЖМИТЕ ЧТОБЫ СГЕНЕРИРОВАТЬ ПОРОЛЬ",
            command=self.generation_password
        )

        self.rowconfigure(index=0, weight=1)
        self.rowconfigure(index=1, weight=1)
        self.columnconfigure(index=0, weight=1)

        self._button.grid(row=1, column=0, sticky="nswe", padx=8, pady=8)
        self._entry.grid(row=0, column=0, sticky="nswe", padx=8, pady=8)

    def generation_password(self):
        length = 69
        characters = 'goida6952₽'
        password = ''.join(random.choice(characters) for i in range(length))
        self._entry.delete("0", "end")
        self._entry.insert("end", password)


if __name__ == "__main__":
    passgenerationWindow().mainloop()
