"""Main file"""

from customtkinter import *

from about_window import AboutWindow


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

    def _open_about(self):
        AboutWindow().mainloop()


def main():
    """Main function"""
    app = MainWindow()
    app.mainloop()


if __name__ == '__main__':
    main()
