pyinstaller ^
    --onefile ^
    --paths .\.venv\Lib\site-packages ^
    --hiddenimport tkinter.ttk ^
    --hiddenimport tkkthemes ^
    --clean ^
    --name oreshnik ^
    --noconsole ^
    main.py
