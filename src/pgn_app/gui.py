#imports
import tkinter as tk
from pathlib import Path
from tkinter import messagebox
from tkinter import ttk
from tkinterdnd2 import DND_FILES, TkinterDnD

#Fenstereinstellungen
root = TkinterDnD.Tk()
root.title("PGN App")
root.minsize(640,430)
root.geometry("640x430")

#Variabeln
height_txt = 9
width_txt = 70
pgn_ger = ""
pgn_eng = ""


#Funktionen
def on_drop(event): #Liest drag-and-drop Textdateien aus und speichert den Inhalt
    global pgn_ger

    pgn_ger = ""

    for path in root.tk.splitlist(event.data):
        with open(path, "r") as file:
            pgn_ger += file.read()

    txt_in.delete("1.0", tk.END)
    txt_in.insert("1.0", pgn_ger)

def ger_eng(input: str) -> str: #Kovertiert deutsches PGN zu englischem
    return input.replace("S", "N").replace("D", "Q").replace("L", "B").replace("T", "R")

def btn_pressed_conv(): #Beim Betätigen des "Konvertieren" Buttons: führt ger_eng() aus, gibt englisches PGN im Ausgabetextfeld aus
    global pgn_eng

    pgn_eng = ger_eng(pgn_ger)

    if pgn_ger == "":
        messagebox.showinfo("Keine Ausgangs-PGN gefunden.")
        return
    txt_out.configure(state="normal")
    txt_out.delete("1.0", tk.END)
    txt_out.insert("1.0", pgn_eng)
    txt_out.configure(state="disabled")

def btn_pressed_clip():
    pass

def btn_pressed_lichess():
    pass 

#Fensterinhalt top->bot
frm_main = ttk.Frame(root, padding=10)
frm_main.pack()

lbl_top = tk.Label(frm_main, text="Deutsches PGN hier einfügen:").grid(column=1, row= 0)

txt_in = tk.Text(frm_main, width=width_txt, height=height_txt)
txt_in.grid(column=0, columnspan=3, row=1)
txt_in.drop_target_register(DND_FILES)
txt_in.dnd_bind('<<Drop>>', on_drop)


btn_submit = tk.Button(frm_main, text="Konvertieren", command=btn_pressed_conv) 
btn_submit.grid(column=1, row=4)

lbl_mid = tk.Label(frm_main, text="Notation im englischen PGN Format:").grid(column=1, row= 5)

txt_out = tk.Text(frm_main, width=width_txt, height=height_txt)
txt_out.grid(column=0, columnspan=3, row=6)
txt_out.configure(state="disabled")

#"Knopfleiste" unter den Ein- und Ausgabefeldern
frm_btn = ttk.Frame(root, padding=10)
frm_btn.pack()
btn_clip = tk.Button(frm_btn, text="In Zwischenablage kopieren", command=btn_pressed_clip) 
btn_clip.pack(side="left", padx=5)
btn_lich = tk.Button(frm_btn, text="Auf Lichess.org analysieren", command=btn_pressed_lichess)
btn_lich.pack(side="left", padx=5)



root.mainloop()
