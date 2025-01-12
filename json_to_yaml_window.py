"""JSON to YAML window"""
import json
import re
from tkinter import messagebox

import yaml
from customtkinter import *

from utils import center


class JSONToYAMLWindow(CTk):
    """JSON to YAML window"""

    def __init__(self):
        """Create window and UI"""
        super().__init__()
        self.title("JSON <-> YAML")
        self.geometry("600x600")
        center(self)

        font = ("Consolas", 18, "normal")

        self._yaml_box = CTkTextbox(
            self,
            font=font
        )
        self._yaml_title = CTkLabel(self, text="YAML")
        self._yaml_button = CTkButton(
            self,
            text="To YAML",
            command=self._to_yaml
        )

        self._json_box = CTkTextbox(
            self,
            font=font
        )
        self._json_title = CTkLabel(self, text="JSON")
        self._json_button = CTkButton(
            self,
            text="To JSON",
            command=self._to_json
        )

        self.rowconfigure(index=0, weight=1)
        self.rowconfigure(index=1, weight=14)
        self.rowconfigure(index=2, weight=1)
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=1)

        self._yaml_box.grid(row=1, column=0, sticky="nswe", padx=8, pady=8)
        self._json_box.grid(row=1, column=1, sticky="nswe", padx=8, pady=8)
        self._yaml_title.grid(row=0, column=0, sticky="ns", padx=8, pady=8)
        self._json_title.grid(row=0, column=1, sticky="ns", padx=8, pady=8)
        self._yaml_button.grid(row=2, column=1, sticky="nswe", padx=8, pady=8)
        self._json_button.grid(row=2, column=0, sticky="nswe", padx=8, pady=8)

    def _to_json(self) -> None:
        """Convert YAML to JSON"""
        try:
            obj = yaml.safe_load(
                self._yaml_box.get("0.0", "end")
            )
        except yaml.YAMLError as error:
            messagebox.showerror(
                "Error",
                "\n".join(map(str, error.args)) +
                "\n--\n" +
                "\n".join(map(str, error.__notes__))
            )
            return
        json_str = json.dumps(obj, indent=2)
        self._json_box.delete("0.0", "end")
        self._json_box.insert("end", json_str)

    def _to_yaml(self) -> None:
        """Convert JSON to YAML"""
        try:
            obj = json.loads(
                self._json_box.get("0.0", "end")
            )
        except json.JSONDecodeError as error:
            messagebox.showerror(
                "Error",
                f"{error.msg}\n"
                f"At: L{error.lineno} C{error.colno}"
            )
            return
        yaml_str = yaml.dump(obj, indent=2)
        self._yaml_box.delete("0.0", "end")
        self._yaml_box.insert("end", yaml_str)


if __name__ == "__main__":
    JSONToYAMLWindow().mainloop()
