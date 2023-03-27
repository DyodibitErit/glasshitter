from tkinter import ttk
import tkinter as tk
import pygame
import pyautogui
import os
pygame.mixer.init()


def hit():
    hitted.set(hitted.get() + hs.get())
    pygame.mixer.music.load("glass.mp3")
    pygame.mixer.music.play()
def vodka():
    if hitted.get() <= 100:
        pyautogui.alert("Недостаточно разбитых стаканов")
    else:
        hs.set(hs.get() * 2)
        hitted.set(hitted.get() - 100)
        pygame.mixer.music.load("gazirovka.mp3")
        pygame.mixer.music.play()
def angry_pups():
    if hitted.get() <= 150:
        pyautogui.alert("Недостаточно разбитых стаканов")
    else:
        hs.set(hs.get() * 3)
        hitted.set(hitted.get() - 150)
        pygame.mixer.music.load("pups.mp3")
        pygame.mixer.music.play()
def save():
    savename = pyautogui.prompt("Введите имя сохранения", "Сохранение")
    os.system(f"echo.>>{savename}")
    savefile = open(savename, "w")
    savefile.write(f"hitted:{hitted.get()}\n")
    savefile.write(f"hs:{hs.get()}")

win = tk.Tk()
win.title("Разбиватель стаканов")
win.geometry("300x200")
win.resizable(False, False)
hs = tk.IntVar()
hitted = tk.IntVar()
hs.set(1)
hitted.set(0)

ttk.Button(win, text="Разбить стакан", command=hit).pack()
ttk.Label(win, textvariable=hitted).pack()
ttk.Button(win, text="Выпить энэргетик (x2 к ломанию) 100$", command=vodka).pack()
ttk.Button(win, text="Энгри пупс (x3 к ломанию) 150$", command=angry_pups).pack()
ttk.Label(win, text="").pack()
ttk.Button(win, text="Сохранить результат", command=save).pack()
ttk.Label(win, text="ПРИМЕЧАНИЕ: Сохраннение результата не дает \nвозможность продолжить игру после перезапуска").pack()

win.mainloop()