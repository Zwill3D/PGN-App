#imports
import tkinter as tk
from pathlib import Path
from tkinter import messagebox
from tkinter import ttk
from tkinterdnd2 import DND_FILES, TkinterDnD
import webbrowser 
import requests
import pyperclip

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
def ger_eng(input: str) -> str: #Konvertiert deutsche Schachnotation zu PGN 
    return input.replace("S", "N").replace("D", "Q").replace("L", "B").replace("T", "R").replace(":", "-")

def on_drop(event): #Liest drag-and-drop Textdateien aus und speichert den Inhalt
    dnd_txt = ""

    for path in root.tk.splitlist(event.data):
        with open(path, "r") as file:
            dnd_txt += file.read()

    txt_in.delete("1.0", tk.END)
    txt_in.insert("1.0", dnd_txt)

def btn_pressed_conv(): #Beim Betätigen des "Konvertieren" Buttons: führt ger_eng() aus, gibt englischesgültiges PGN im Ausgabetextfeld aus
    global pgn_eng, pgn_ger

    pgn_ger = txt_in.get("1.0", tk.END)

    if pgn_ger == "":
        messagebox.showerror("Fehler", "Keine Ausgangs-Daten gefunden.")
        return

    pgn_eng = ger_eng(pgn_ger)
    
    txt_out.configure(state="normal")
    txt_out.delete("1.0", tk.END)
    txt_out.insert("1.0", pgn_eng)
    txt_out.configure(state="disabled")

def btn_pressed_clip():
    if pgn_eng == "":
        messagebox.showerror("Fehler", "Keine konvertiert PGN gefunden. Bitte deutsche Notation ins obere Textfeld einfügen und 'Konvertieren' drücken.")
        return
    pyperclip.copy(pgn_eng)

def btn_pressed_lichess():
    url = "https://lichess.org/api/import"
    data = {"pgn": pgn_eng}  
    try:
        response = requests.post(url, data=data,headers={
        "Accept": "application/json",
        "User-Agent": "PGN-App/1.0",
    })
        
        if response.status_code == 200:
            game_data = response.json()
            analysis_url = game_data.get("url")
            
            webbrowser.open(analysis_url)
        else:
            messagebox.showerror("Fehler", f"Fehler beim Importieren des Spiels. Lichess Status Code: {response.status_code}\n {response.text}")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Fehler", f"Netzwerkfehler: {e}")

#Fensterinhalt top->bot
frm_main = ttk.Frame(root, padding=10)
frm_main.pack()

lbl_top = tk.Label(frm_main, text="Deutsche Notation hier einfügen:").grid(column=1, row= 0)

txt_in = tk.Text(frm_main, width=width_txt, height=height_txt)
txt_in.grid(column=0, columnspan=3, row=1)
txt_in.drop_target_register(DND_FILES)
txt_in.dnd_bind('<<Drop>>', on_drop)

btn_submit = tk.Button(frm_main, text="Konvertieren", command=btn_pressed_conv) 
btn_submit.grid(column=1, row=4)

lbl_mid = tk.Label(frm_main, text="Die Partie im PGN Format:").grid(column=1, row= 5)

txt_out = tk.Text(frm_main, width=width_txt, height=height_txt)
scroll_out = tk.Scrollbar(frm_main, command=txt_out.yview)
txt_out.configure(yscrollcommand=scroll_out.set)
txt_out.grid(column=0, columnspan=3, row=6)
scroll_out.grid(column=3, row=6, sticky="ns")
txt_out.configure(state="disabled")


#"Knopfleiste" unter den Ein- und Ausgabefeldern
frm_btn = ttk.Frame(root, padding=10)
frm_btn.pack()
btn_clip = tk.Button(frm_btn, text="In Zwischenablage kopieren", command=btn_pressed_clip) 
btn_clip.pack(side="left", padx=5)
btn_lich = tk.Button(frm_btn, text="Auf Lichess.org analysieren", command=btn_pressed_lichess)
btn_lich.pack(side="left", padx=5)

root.mainloop()
