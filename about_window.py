from customtkinter import *

from utils import center


class AboutWindow(CTk):
    def __init__(self):
        super().__init__()
        self.title("About")
        center(self, 600, 600)

        self._title_label = CTkLabel(self, text="About Oreshnik-Tools")
        self._text_label = CTkLabel(self, text="(C) Oreshnik team 2024")
        self._title_label.grid(row=0, column=0, padx=5, pady=5)
        self._text_label.grid(row=1, column=0, padx=5, pady=5)


if __name__ == "__main__":
    AboutWindow().mainloop()
