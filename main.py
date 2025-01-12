"""Main file"""

from customtkinter import *

import SySs
from Text_Analysis import TextAnalysisWindow
from about_window import AboutWindow
from autopep8_window import AutoPEP8Window
from colors import ColorsWindow
from json_to_yaml_window import JSONToYAMLWindow
from qr_window import QRWindow
from regex_window import RegexWindow
from utils import center


class MainWindow(CTk):
    """Main application window"""

    def __init__(self):
        """Initialize window and setup UI"""
        super().__init__()
        center(self, 350, 500)
        self.title("Oreshnik-Tools")

        self.columnconfigure(index=0, weight=1)

        common_style = {"sticky": "nswe", "padx": 60, "pady": 4}

        self._title_label = CTkLabel(self, text="Oreshnik-Tools v1")
        self._title_label.grid(row=0, column=0, **common_style)

        self._about_btn = CTkButton(self, text="About", command=self._open_about)
        self._about_btn.grid(row=1, column=0, **common_style)

        self._regex_btn = CTkButton(self, text="Regex", command=self._open_regex)
        self._regex_btn.grid(row=2, column=0, **common_style)

        self._text_btn = CTkButton(self, text="Text_analys", command=self._open_text)
        self._text_btn.grid(row=3, column=0, **common_style)

        self._trans_btn = CTkButton(self, text="any base to any base", command=self._open_transSS)
        self._trans_btn.grid(row=4, column=0, **common_style)

        self._qr_btn = CTkButton(self, text="QR gen", command=self._open_qr_gen)
        self._qr_btn.grid(row=5, column=0, **common_style)

        self._pep8_btn = CTkButton(self, text="Auto PEP8", command=self._open_autopep8)
        self._pep8_btn.grid(row=6, column=0, **common_style)

        self._json_conv_btn = CTkButton(self, text="JSON <-> YAML", command=self._open_json_conv)
        self._json_conv_btn.grid(row=7, column=0, **common_style)

        self._colors_btn = CTkButton(self, text="Color picker", command=self._open_colors)
        self._colors_btn.grid(row=8, column=0, **common_style)

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

    def _open_json_conv(self):
        JSONToYAMLWindow().mainloop()

    def _open_colors(self):
        ColorsWindow().mainloop()


def main():
    """Main function"""
    app = MainWindow()
    app.mainloop()


if __name__ == '__main__':
    main()
