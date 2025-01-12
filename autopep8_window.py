"""AutoPEP8 Window"""

import json
from tkinter import messagebox

import autopep8
from customtkinter import *

from utils import center


class AutoPEP8Window(CTk):
    """AutoPEP8 Window"""

    def __init__(self):
        """Create window and UI"""
        super().__init__()
        self.title("AutoPEP8")
        center(self, 600, 600)

        font = ("Consolas", 18, "normal")

        self._code_box = CTkTextbox(self, font=font)
        self._format_button = CTkButton(self, text="Format code", command=self._format)

        self.rowconfigure(index=1, weight=1)
        self.rowconfigure(index=0, weight=14)
        self.columnconfigure(index=0, weight=1)

        self._code_box.grid(row=0, column=0, sticky="nswe", padx=8, pady=8)
        self._format_button.grid(row=1, column=0, sticky="nswe", padx=8, pady=8)

    def _format(self) -> None:
        """Reformat code"""
        result = autopep8.fix_code(self._code_box.get("0.0", "end"))
        self._code_box.delete("0.0", "end")
        self._code_box.insert("end", result)


if __name__ == "__main__":
    AutoPEP8Window().mainloop()
