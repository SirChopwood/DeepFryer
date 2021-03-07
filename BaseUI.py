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
        self.classes = [entities.ArcherFry, entities.WarriorFry, entities.RogueFry, entities.NecromancerFry]

        self.fry_list = []
        for x in range(7):
            for y in range(8):
                test = random.choice(self.classes)(self)
                self.fry_list.append(test)
                test.set_position(200+(x*100), 100+(y*120))

        test2 = entities.Mod(self)
        test2.set_position(1300, 500)
        self.current_fry_id = 0
        self.current_fry = [None, None, None, None, None]
        self.current_fry_pos = [None, None, None, None, None]
        random.shuffle(self.fry_list)
        self.tick()

    def tick(self):
        for i in range(5):
            if i < len(self.current_fry):
                if self.current_fry[i]:
                    self.current_fry[i].set_position(self.current_fry_pos[i][0], self.current_fry_pos[i][1])
            self.current_fry[i] = self.fry_list[self.current_fry_id]
            self.current_fry_pos[i] = (self.current_fry[i].x, self.current_fry[i].y)
            self.current_fry[i].set_position(self.winfo_screenwidth()/2, self.winfo_screenheight()/2 + ((i-2.5)*130))
            if self.current_fry_id < ((len(self.fry_list) -1) / 5):
                self.current_fry_id += 1
            else:
                self.current_fry_id = 0

        self.after(1000, self.tick)  # 5 Ticks per second
Game = BaseWindow()
Game.mainloop()
