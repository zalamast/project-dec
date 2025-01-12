"""Main file"""

from customtkinter import *

import SySs
from Text_Analysis import TextAnalysisWindow
from about_window import AboutWindow
from autopep8_window import AutoPEP8Window
from qr_window import QRWindow
from regex_window import RegexWindow


class MainWindow(CTk):
    """Main application window"""

    def __init__(self):
        """Initialize window and setup UI"""
        super().__init__()
        self.geometry("600x500")
        self.title("Oreshnik-Tools")

        self._title_label = CTkLabel(self, text="Oreshnik-Tools v1")
        self._title_label.grid(row=0, column=0)

        self._about_btn = CTkButton(self, text="About", command=self._open_about)
        self._about_btn.grid(row=1, column=0)

        self._regex_btn = CTkButton(self, text="Regex", command=self._open_regex)
        self._regex_btn.grid(row=2, column=0)

        self._text_btn = CTkButton(self, text="Text_analys", command=self._open_text)
        self._text_btn.grid(row=3, column=0)

        self._trans_btn = CTkButton(self, text="any base to any base", command=self._open_transSS)
        self._trans_btn.grid(row=4, column=0)

        self._qr_btn = CTkButton(self, text="QR gen", command=self._open_qr_gen)
        self._qr_btn.grid(row=5, column=0)

        self._pep8_btn = CTkButton(self, text="Auto PEP8", command=self._open_autopep8)
        self._pep8_btn.grid(row=6, column=0)

    def _open_about(self):
        AboutWindow().mainloop()

    def _open_regex(self):
        RegexWindow().mainloop()

    def _open_text(self):
        TextAnalysisWindow().mainloop()

    def _open_transSS(self):
        SySs.start_window()

    def _open_qr_gen(self):
        QRWindow().mainloop()

    def _open_autopep8(self):
        AutoPEP8Window().mainloop()

def main():
    """Main function"""
    app = MainWindow()
    app.mainloop()


if __name__ == '__main__':
    main()
