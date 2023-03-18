import sqlite3 
import datetime
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt

con = sqlite3.connect('keuangan.db')
cursor = con.cursor()

cursor.execute('create table if not exists forchart (id integer primary key, hari text not null, keuangan integer not null)')
con.commit()
cursor.execute('create table if not exists user (id integer primary key, username text not null, keuangan integer not null)')
con.commit()
cursor.execute("insert or ignore into user (id, username, keuangan) values (1, 'user', 0)")
con.commit()
cursor.execute('create table if not exists histori (id integer primary key, konteks text not null,method text not null, hari text not null, jumlah integer not null)')
con.commit()



today = datetime.datetime.today()
day_name = today.strftime('%A')
day_names = {
    'Monday': 'Senin',
    'Tuesday': 'Selasa',
    'Wednesday': 'Rabu',
    'Thursday': 'Kamis',
    'Friday': 'Jumat',
    'Saturday': 'Sabtu',
    'Sunday': 'Minggu'
}
day_name_id = day_names.get(day_name, 'Unknown')
print(day_name_id)

root = tk.Tk()
root.geometry("500x500")
root.title("Keuangan")

frame = ttk.Frame(root)
frame.grid(row=0, column=0, padx=10,pady=5)

label = tk.Label(frame, text="Management Keuangan Anda")



root.mainloop()
