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
        for x in range(8):
            temp = []
            for y in range(5):
                test = random.choice(self.classes)(self)
                temp.append(test)
                test.set_position(50+(y*100), 50+(x*130))
                test.current_health = random.randint(0, test.health)
            self.fry_list.append(temp)

        self.boss = entities.Mod(self)
        self.boss.set_position(1500, 500)
        self.current_fry_id = 0
        self.current_fry = [None, None, None, None, None]
        self.current_fry_pos = [None, None, None, None, None]
        self.tick()

    def tick(self):
        print(len(self.fry_list))
        
        for i in range(len(self.fry_list)):
            self.next_fry_squad()
        self.after(10, self.tick)

    def next_fry_squad(self):
        for i in range(5):
            if self.current_fry[i]:
                self.current_fry[i].set_position(self.current_fry_pos[i][0], self.current_fry_pos[i][1])
                self.current_fry[i].set_nametag(self.current_fry[i].name, "Basic")
            self.current_fry[i] = self.fry_list[self.current_fry_id][i]
            self.current_fry_pos[i] = (self.current_fry[i].x, self.current_fry[i].y)
            self.current_fry[i].set_position(self.winfo_screenwidth()/2-100, self.winfo_screenheight()/2 + ((i-2.5)*130))
            self.current_fry[i].set_nametag(self.current_fry[i].name, "Healthbar")

        if self.current_fry_id < (len(self.fry_list) -1):
            self.current_fry_id += 1
        else:
            self.current_fry_id = 0

Game = BaseWindow()
Game.mainloop()
