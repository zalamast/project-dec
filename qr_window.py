"""QRcode  window"""

import re

import segno
from customtkinter import *


class QRWindow(CTk):
    def __init__(self):
        super().__init__()
        self.title("Regex")
        self.geometry("600x600")

        font = ("Consolas", 14, "normal")

        self.text_field = CTkEntry(self)
        self.btn = CTkButton(self, text="НАЖМИТЕ ДЛЯ ГЕНЕРАЦИИ QRcode", command=self.click_button)
        self.text_field.pack(fill = "x")
        self.btn.pack(fill = "x")

    def click_button(self):
        path = filedialog.asksaveasfilename(defaultextension="png")
        if path == "" or path is None:
            return
        qrcode = segno.make_qr(self.text_field.get())
        qrcode.save(path, scale=5)


if __name__ == "__main__":
    QRWindow().mainloop()