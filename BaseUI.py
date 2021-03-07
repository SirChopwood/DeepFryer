import tkinter as tk
from PIL import Image, ImageTk


class BaseWindow(tk.Tk):
    def __init__(self):
        self.image_refs = []
        super(BaseWindow, self).__init__()
        self.title("Deep Fryer")
        self.attributes("-fullscreen", True)
        self.canvas = tk.Canvas(self, width=self.winfo_screenwidth(), height=self.winfo_screenheight(),
                                     bg="#333337", bd=0, highlightthickness=0, relief='ridge')
        self.canvas.pack()
        self.sprite("Assets/Sprites/Archer.png", x=500, y=500)


    def sprite(self, path, x=0, y=0, anchor="center"):
        img = Image.open(path)
        img = img.resize((256, 256), 0)
        img = ImageTk.PhotoImage(img)
        self.canvas.create_image(x, y, anchor=anchor, image=img)
        self.image_refs.append(img)


Game = BaseWindow()
Game.mainloop()
