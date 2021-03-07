import tkinter as tk
from PIL import Image, ImageTk
from tkinter import font
import random
import names


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
        self.classes = [self.ArcherFry, self.WarriorFry, self.RogueFry]

        for x in range(7):
            for y in range(8):
                test = random.choice(self.classes)(self)
                test.set_position(200+(x*100), 100+(y*120))

        test2 = self.Mod(self)
        test2.set_position(1300, 500)

    class Entity:
        x = 0
        y = 0
        name = str
        sprite_path = str
        sprite = object
        sprite_scale = tuple
        sprite_flip = False
        nametag = str  # "Basic" or "Boss"
        nametag_offset_x = 0
        nametag_offset_x = 0
        colour = str  # "#ffffff"

        def __init__(self, window):
            self.window = window
            if self.sprite_path:
                self.sprite = self.create_sprite(self.sprite_path)
            if self.nametag:
                self.nametag = self.create_nametag(self.name)

        def create_sprite(self, path, x=0, y=0, anchor="center"):
            img = Image.open(path)
            if self.sprite_scale:
                img = img.resize(self.sprite_scale, 0)
            if self.sprite_flip:
                img = img.transpose(Image.FLIP_LEFT_RIGHT)
            img = ImageTk.PhotoImage(img)
            self.window.image_refs.append(img)
            return self.window.canvas.create_image(x, y, anchor=anchor, image=img)

        def create_nametag(self, text):
            if self.nametag == "Basic":
                return self.window.canvas.create_text(self.x+self.nametag_offset_x, self.y+self.nametag_offset_y, text=text, anchor="center", font=self.window.font_basic, fill=self.colour)
            if self.nametag == "Boss":
                return self.window.canvas.create_text(self.x+self.nametag_offset_x, self.y+self.nametag_offset_y, text=text, anchor="center", font=self.window.font_bigger, fill=self.colour)

        def set_position(self, x, y):
            self.window.canvas.move(self.sprite, x, y)
            self.window.canvas.move(self.nametag, x, y+70)

    class Fry(Entity):
        name = "French Fry"
        sprite_path = "Assets/Sprites/Fry.png"
        sprite_scale = (128, 128)
        sprite_flip = True
        nametag = "Basic"
        colour = "#7030ab"
        nametag_offset_x = 0
        nametag_offset_y = 10
        combat_class = object
        Damage = 1
        Health = 5
        Saves = 8

        def __init__(self, window):
            self.name = names.get_first_name()
            super().__init__(window)

    class WarriorFry(Fry):
        Name = "Warrior"
        Damage = 5
        Health = 20
        Saves = 5
        sprite_path = "Assets/Sprites/Warrior.png"

    class ArcherFry(Fry):
        Name = "Archer"
        Damage = 15
        Health = 10
        Saves = 3
        sprite_path = "Assets/Sprites/Archer.png"

    class RogueFry(Fry):
        Name = "Rogue"
        Damage = 20
        Health = 5
        Saves = 2
        sprite_path = "Assets/Sprites/Rogue.png"

    class Mod(Entity):
        name = "ModCorp Intern"
        sprite_path = "Assets/Sprites/ModCorp.png"
        sprite_scale = (256, 256)
        nametag = "Boss"
        colour = "#ffffff"
        nametag_offset_x = 0
        nametag_offset_y = -200


Game = BaseWindow()
Game.mainloop()
