"""Utils for ui"""


def center(win, width, height):
    """Center a tkinter window"""
    win.update_idletasks()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry(f"{width}x{height}+{x}+{y}")
    win.deiconify()
