import tkinter as tk
from tkinter import font
import random
import entities


class BaseWindow(tk.Tk):
    def __init__(self):
        self.image_refs = []
        super(BaseWindow, self).__init__()
        self.title("Deep Fryer")
        self.attributes("-fullscreen", True)
        self.font_basic = font.Font(family='Bebas Neue', size=20, weight='normal')
        self.font_bigger = font.Font(family='Bebas Neue', size=40, weight='normal')
        self.canvas = tk.Canvas(self, width=self.winfo_screenwidth(), height=self.winfo_screenheight(),
                                     bg="#333337", bd=0, highlightthickness=0, relief='ridge')
        self.canvas.pack()
        self.classes = [entities.ArcherFry, entities.WarriorFry, entities.RogueFry]

        for x in range(7):
            for y in range(8):
                test = random.choice(self.classes)(self)
                test.set_position(200+(x*100), 100+(y*120))

        test2 = entities.Mod(self)
        test2.set_position(1300, 500)

Game = BaseWindow()
Game.mainloop()
