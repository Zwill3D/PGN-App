import tkinter as tk
from pathlib import Path
from tkinter import messagebox
from tkinter import ttk
from tkinterdnd2 import DND_FILES, TkinterDnD

#Fenstereinstellungen
root = TkinterDnD.Tk()
root.title("PGN App")
root.minsize(320,240)
root.geometry("640x400")

height_txt = 9
width_txt = 70

#Fensterinhalt top->bot
frm_main = ttk.Frame(root, padding=10)
frm_main.pack()

lbl_top = tk.Label(frm_main, text="Deutsches PGN hier einfügen:").grid(column=1, row= 0)

in_txt = tk.Text(frm_main, width=width_txt, height=height_txt)
in_txt.grid(column=0, columnspan=3, row=1)

lbl_mid = tk.Label(frm_main, text="Notation im englischen PGN Format:").grid(column=1, row= 4)

txt_out = tk.Text(frm_main, width=width_txt, height=height_txt)
txt_out.grid(column=0, columnspan=3, row=5)

#"Knopfleiste" unter den Ein- und Ausgabefeldern
frm_btn = ttk.Frame(root, padding=10)
frm_btn.pack()
btn_clip = tk.Button(frm_btn, text="In Zwischenablage kopieren") 
btn_clip.pack(side="left", padx=5)
btn_lich = tk.Button(frm_btn, text="Auf Lichess.org analysieren")
btn_lich.pack(side="left", padx=5)

root.mainloop()
