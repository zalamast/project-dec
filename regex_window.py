"""Regex tester window"""

import re
from tkinter import messagebox

from customtkinter import *


class RegexWindow(CTk):
    """Regex tester window"""

    def __init__(self):
        """Create window and UI"""
        super().__init__()
        self.title("Regex")
        self.geometry("600x600")

        font = ("Consolas", 14, "normal")

        self._regex_box = CTkTextbox(
            self, font=font
        )
        self._regex_box.insert("end", "Enter regex")
        self._text_box = CTkTextbox(
            self, font=font
        )
        self._text_box.insert("end", "Enter text")
        self._match_box = CTkTextbox(
            self, state="disabled", font=font
        )
        self._match_btn = CTkButton(
            self, text="Match!", command=self._match
        )

        self.rowconfigure(index=0, weight=3)
        self.rowconfigure(index=1, weight=1)
        self.rowconfigure(index=2, weight=5)
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=1)

        self._regex_box.grid(row=0, column=0, columnspan=2, sticky="nswe", padx=8)
        self._text_box.grid(row=1, column=0, rowspan=2, sticky="nswe", padx=8)
        self._match_btn.grid(row=1, column=1, sticky="nswe", padx=8)
        self._match_box.grid(row=2, column=1, sticky="nswe", padx=8)

    def _match(self) -> None:
        """Perform regex match and display matches"""
        try:
            pattern = re.compile(self._regex_box.get("0.0", "end"))
        except re.error as error:
            messagebox.showerror("Error", str(error))
            return
        matches = pattern.findall(
            self._text_box.get("0.0", "end")
        )
        self._match_box.configure(state="normal")
        self._match_box.delete("0.0", "end")
        for match in matches:
            self._match_box.insert(
                "end",
                str(match) + "\n--\n"
            )
        self._match_box.configure(state="disabled")


if __name__ == "__main__":
    RegexWindow().mainloop()
