"""Main file"""

from customtkinter import *


class MainWindow(CTk):
    """Main application window"""

    def __init__(self):
        """Initialize window and setup UI"""
        super().__init__()
        self.geometry("600x500")
        self.title("Oreshnik-Tools")

        self._title_label = CTkLabel(self, text="Oreshnik-Tools v1")
        self._title_label.grid(row=0, column=0)


def main():
    """Main function"""
    app = MainWindow()
    app.mainloop()


if __name__ == '__main__':
    main()
